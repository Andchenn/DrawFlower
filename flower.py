import turtle
import math


def p_line(t, n, length, angle):
    """画n个线段
    t:龟对象
    n:线段数量
    length：每个部分的长度
    angle:段之间的度数
    """
    for i in range(n):
        # 向前
        t.fd(length)
        # 左转
        t.lt(angle)


def polygon(t, n, length):
    """画具有n个边的多边形
    t:龟
    n:双方数量
    length：每边的长度
    """
    # 正n多边形的外角为360/n度
    angle = 360 / n
    p_line(t, n, length, angle)


def arc(t, r, angle):
    """画具有给定半径和角度的圆弧
    t:龟
    r:半径
    角度：弧所对应的角度，以度为单位
    """
    # 扇形的弧长
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # 开始减速之前，稍微左转
    # 由弧线性逼近引起的误差
    t.lt(step_angle / 2)
    p_line(t, n, step_length, step_angle)
    # rt右转
    t.rt(step_angle / 2)


def petal(t, r, angle):
    """用两个弧画一个花瓣"""
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, n, r, angle, p):
    """用n个花瓣画一朵花"""
    for i in range(n):
        petal(t, r, angle)
        t.lt(p / n)


def leaf(t, r, angle, p):
    """画一个叶子并填充它"""
    # 开始填充内容
    t.begin_fill()
    t.down()
    flower(t, 1, r, angle, p)
    t.end_fill()


def main():
    # 创建一个屏幕
    window = turtle.Screen()
    window.bgcolor("gray")
    window.title("draw a flower")
    lucy = turtle.Turtle()
    lucy.shape("turtle")
    lucy.color("red")
    lucy.width(3)

    # 画花
    flower(lucy, 6, 60, 100, 360)

    # 画花梗
    lucy.color("brown")
    lucy.rt(90)
    lucy.fd(200)

    # 画叶1
    lucy.width(1)
    lucy.rt(270)
    lucy.color("green")
    leaf(lucy, 40, 80, 180)
    lucy.rt(140)
    lucy.color("black")
    lucy.fd(30)
    lucy.lt(180)
    lucy.fd(30)

    # 叶2
    lucy.rt(120)
    lucy.color("green")
    leaf(lucy, 40, 80, 100)
    lucy.color("black")
    lucy.rt(140)
    lucy.fd(30)
    lucy.ht()  # 隐藏龟
    window.exitonclick()


if __name__ == '__main__':
    main()
