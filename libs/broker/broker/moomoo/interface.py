import moomoo as ft
import typing


class FTModifyOrderConfig(typing.TypedDict):
    order_id: str
    modify_order_op: ft.ModifyOrderOp
    qty: int
    price: float
    adjust_limit: float
    trd_env: ft.TrdEnv
    # For condition order
    acc_id: int
    acc_index: int
    trail_type: ft.TrailType
    trail_value: float
    trail_spread: float
