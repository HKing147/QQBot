from pydantic import Extra, BaseSettings


class Config(BaseSettings):
    superusers = ["1470042308", "1600321769", "987654321"]
    setu2_cd = 10
    setu2_enable_groups = [127792558, 984075022]
    proxies_socks5 = 'socks5://127.0.0.1:1089'

    class Config:
        extra = Extra.ignore
        case_sensitive = False
