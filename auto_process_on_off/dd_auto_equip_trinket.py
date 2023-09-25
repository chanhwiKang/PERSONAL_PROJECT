import pyautogui
EQUIP_L = (490, 663)
# 중앙 560, 658
# 오른 627, 663

pyautogui.click(EQUIP_L)
pyautogui.dragTo(EQUIP_L, 2, button='left')