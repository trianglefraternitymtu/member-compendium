import logging
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .utils import filter_command

logger = logging.getLogger('basicLogger')

format_ethic = "{}. {}.".format

@require_POST
def command(request):
    logger.info('Code of Ethics slash command')

    response = filter_command(request)
    if response:
        return response

    coeText = {1: "Observe the precepts of the Fraternity as set forth in the Ritual",
        2: "Accept cheerfully my full share of any task, however menial, involved in maintaining a chapter home",
        3: "Preserve and promote the chosen ideals of my Fraternity",
        4: "Pay all personal bills promptly, and always live within my means",
        5: "Help create in my chapter home an environment in which enduring friendships may be formed",
        6: "Maintain a creditable scholastic record",
        7: "Promote the welfare of my profession",
        8: "Maintain my self-respect by proper conduct at all times",
        9: "Uphold faithfully the traditions and program of my Alma Mater",
        10: "Pay the price of success in honest effort"}

    all_ethics = [{"title":format_ethic(*e), "color":"#8a1538", "fallback":format_ethic(*e)} for e in coeText.items()]
    args = request.POST.get("text").split(maxsplit=1)

    try:
        ethic = int(args[0])
    except ValueError:
        logger.info('Invalid ethic selected, returning all of them.')
        return JsonResponse({"attachments":all_ethics})

    if ethic in coeText:
        logger.info('Printing ethic {}'.format(ethic))
        return JsonResponse({"attachments":[{"title":format_ethic(ethic, coeText[ethic]), "color":"#8a1538", "fallback":format_ethic(ethic, coeText[ethic])}]})
    elif ethic > len(coeText) and len(args) > 1:
        logger.info('Printing fake ethic {}'.format(ethic))
        return JsonResponse({"attachments":[{"title":format_ethic(ethic, args[1]), "color":"#8a1538", "fallback":format_ethic(ethic, args[1])}]})

    return JsonResponse({"attachments":all_ethics})
