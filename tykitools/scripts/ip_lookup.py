import requests


def ip_lookup_from_string(ip: str) -> str:
    """
    Given an IP address, return all Informations.
    """
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        response.raise_for_status()
        data = response.json()
        country = data.get("country", "Pays inconnu")
        region = data.get("regionName", "Région inconnue")
        city = data.get("city", "Ville inconnue")
        lat = data.get("lat", "Latitude inconnue")
        lon = data.get("lon", "Longitude inconnue")
        return f"Le pays est : {country}\nLa région est : {region}\nLa ville est : {city}\nLa latitude est : {lat}\nLa longitude est : {lon}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
