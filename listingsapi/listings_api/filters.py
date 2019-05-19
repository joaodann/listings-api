from django.conf import settings


def listings_zap_filter(listings):
    zap_listings = remove_listings_without_location_filter(listings)
    zap_listings = [
        x
        for x in zap_listings
        if (
            int(x.pricingInfos.price) >= 3500
            and x.pricingInfos.businessType == "RENTAL"
        )
        or (
            (
                (
                    x.isInsideZapGroupArea
                    and int(x.pricingInfos.price)
                    >= settings.ZAP_MIN_SALE_PRICE * 0.9
                )
                or int(x.pricingInfos.price) >= settings.ZAP_MIN_SALE_PRICE
            )
            and x.pricingInfos.businessType == "SALE"
            and (
                x.usableAreas == 0
                or x.squareMeterPrice > settings.ZAP_MIN_RENTAL_PRICE
            )
        )
    ]

    return zap_listings


def listings_vivareal_filter(listings):
    zap_listings = remove_listings_without_location_filter(listings)
    vivareal = [
        x
        for x in zap_listings
        if (
            (
                (
                    x.isInsideZapGroupArea
                    and int(x.pricingInfos.price)
                    <= settings.VIVAREAL_MAX_RENTAL_PRICE * 1.5
                )
                or int(x.pricingInfos.price)
                <= settings.VIVAREAL_MAX_RENTAL_PRICE
            )
            and x.pricingInfos.businessType == "RENTAL"
            and (
                not hasattr(x.pricingInfos, "monthlyCondoFee")
                or x.pricingInfos.monthlyCondoFee == 0
                or x.monthlyCondoFeeRentalPercentage < 30
            )
        )
        or (
            int(x.pricingInfos.price) <= settings.VIVAREAL_MAX_SALE_PRICE
            and x.pricingInfos.businessType == "SALE"
        )
    ]

    return vivareal


def remove_listings_without_location_filter(listings):
    filtered_listings = [
        x
        for x in listings
        if (
            x.address.geoLocation.location.lat != 0
            or x.address.geoLocation.location.lon != 0
        )
    ]

    return filtered_listings
