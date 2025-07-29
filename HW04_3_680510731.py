#!/usr/bin/env python3
# Phutthachat Sawatnsthi (champagne)
# 680510731
# HW04_3
# 204111 Sec 002

def divide_plot(x: int, y: int, z: int, start: str) -> str:
    ops = ''
    a = (x-1)
    b = (z-1)
    c = (x+y+z)//3

    if start == 'A' :
        p = 'RIGHT'

    if start == 'B' :
        p = ''

    if start == 'C' :
        p = 'LEFT'

    if (x == y == z) :
        ops = ''

    if x != 1 and z != 1:
        ops = concat_ops(p, f'PUSH_LEFT {a}')
        ops = concat_ops(ops, f'PUSH_RIGHT {b}')
        ops = concat_ops(ops, 'RIGHT')
        ops = concat_ops(ops, f'PUSH_LEFT {c-1}')
        ops = concat_ops(ops, 'LEFT')
        ops = concat_ops(ops, 'LEFT')
        ops = concat_ops(ops, f'PUSH_RIGHT {c-1}')

    if x == 1 and z == 1 :
        ops = concat_ops(p, 'RIGHT')
        ops = concat_ops(ops, f'PUSH_LEFT {c-1}')
        ops = concat_ops(ops, 'LEFT')
        ops = concat_ops(ops, 'LEFT')
        ops = concat_ops(ops, f'PUSH_RIGHT {c-1}')

    if x == 1 and z != 1 :
        ops = concat_ops(p, f'PUSH_RIGHT {b}')
        ops = concat_ops(ops, 'RIGHT')
        ops = concat_ops(ops, f'PUSH_LEFT {c-1}')
        ops = concat_ops(ops, 'LEFT')
        ops = concat_ops(ops, 'LEFT')
        ops = concat_ops(ops, f'PUSH_RIGHT {c-1}')

    if x != 1 and z == 1 :
        ops = concat_ops(p, f'PUSH_LEFT {a}')
        ops = concat_ops(ops, 'RIGHT')
        ops = concat_ops(ops, f'PUSH_LEFT {c-1}')
        ops = concat_ops(ops, 'LEFT')
        ops = concat_ops(ops, 'LEFT')
        ops = concat_ops(ops, f'PUSH_RIGHT {c-1}')



    # แนะนำให้ใช้ฟังก์ชัน concat_ops() เพื่อนำสองชุดคำสั่งมาต่อกันแล้วคั่นด้วย comma
    # ไม่ควรทำ string concatenate แล้วบันทึกลงตัวแปรเดิม เช่น
    # ops += 'RIGHT' หรือ ops = ops + 'RIGHT' (ศึกษาได้จาก slide เรื่อง String)





    # ไม่แก้บรรทัดนี้
    return ops.strip(', ')





def concat_ops(op1: str, op2: str) -> str:
    """
    ต่อข้อความคำสั่งสองชุดเข้าด้วยกันโดยเว้นด้วยเครื่องหมายคอมมาและเว้นวรรค

    ฟังก์ชันนี้จะรับข้อความคำสั่งสองชุด (เช่น "LEFT", "PUSH_RIGHT 3") แล้วรวมเข้าด้วยกัน
    ด้วยเครื่องหมายคอมมาและช่องว่าง (", ") อย่างถูกต้อง ถ้าชุดใดชุดหนึ่งว่างเปล่า
    จะคืนค่าอีกชุดหนึ่งแทนโดยไม่เติมคอมมา หากทั้งสองชุดว่างเปล่า จะคืนค่าว่าง

    พารามิเตอร์:
        op1 (str): ข้อความคำสั่งชุดแรก
        op2 (str): ข้อความคำสั่งชุดที่สอง

    คืนค่า:
        str: ข้อความคำสั่งที่ถูกรวมเข้าด้วยกันอย่างถูกต้อง

    ตัวอย่าง:
        >>> concat_ops("LEFT", "PUSH_RIGHT 3")
        'LEFT, PUSH_RIGHT 3'
        >>> concat_ops("", "RIGHT")
        'RIGHT'
        >>> concat_ops("LEFT", "")
        'LEFT'
        >>> concat_ops("", "")
        ''
    """
    if not op1 and not op2:
        return ''
    if not op1:
        return op2
    if not op2:
        return op1

    return ', '.join([op1, op2])


if __name__ == '__main__':
    from HW04_3_helper import simulate_operations
    ops = divide_plot(5, 3, 1, 'A')
    result = simulate_operations(5, 3, 1, 'A', ops)
    print(result)

