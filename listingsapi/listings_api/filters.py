def listings_zap_filter(listings):
    zap_listings = remove_listings_without_location_filter(listings)
    zap_listings = [x for x in zap_listings if (int(x.pricingInfos.price) >= 3500
                                            and x.pricingInfos.businessType == "RENTAL")
                    or (int(x.pricingInfos.price) >= 600000
                        and x.pricingInfos.businessType == "SALE"
                        and (x.usableAreas == 0 or x.squareMeterPrice > 3500))]

    return zap_listings


def listings_vivareal_filter(listings):
    zap_listings = remove_listings_without_location_filter(listings)
    vivareal = [x for x in zap_listings if (int(x.pricingInfos.price) <= 4000
                                        and x.pricingInfos.businessType == "RENTAL")
                or (int(x.pricingInfos.price) <= 700000
                    and x.pricingInfos.businessType == "SALE")]

    return vivareal


def remove_listings_without_location_filter(listings):
    filtered_listings = [x for x in listings if
                         (x.address.geoLocation.location.lat != 0 or x.address.geoLocation.location.lon != 0)]

    return filtered_listings
