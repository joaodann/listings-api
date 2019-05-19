def listings_zap_filter(listings):
    zap_listings = [x for x in listings if (int(x.pricingInfos.price) >= 3500
                                            and x.pricingInfos.businessType == "RENTAL")
                    or (int(x.pricingInfos.price) >= 600000
                        and x.pricingInfos.businessType == "SALE")]

    return zap_listings


def listings_vivareal_filter(listings):
    vivareal = [x for x in listings if (int(x.pricingInfos.price) <= 4000
                                        and x.pricingInfos.businessType == "RENTAL")
                or (int(x.pricingInfos.price) <= 700000
                    and x.pricingInfos.businessType == "SALE")]

    return vivareal
