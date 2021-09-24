from fastapi import APIRouter

from parsers.vin_parsers.vpic_nhtsa_dot_gov_parser.parser import parse

router = APIRouter()


@router.get("/info")
def test_func(vin: str):
    info_auto = parse(vin)
    return info_auto
