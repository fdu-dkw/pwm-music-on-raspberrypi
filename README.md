# pwm-music-on-raspberrypi

用电导课小车来演奏音乐🎵Turn your IES car into an instrument🎵

# 设备要求

1. 树莓派4B+

2. 复旦大学电子系统导论课程智能小车套件（[内容清单1](https://docs.qq.com/doc/DY3RHa0laV09oQmRY)、[内容清单2](https://docs.qq.com/doc/DY3F2QnNZeGR4TkFh)）

# 部署方式

## 小车组装与接线

> 省流：拼小车的第一节课教过。注意遵守相同的接线规则。

请参考复旦大学电子系统导论课程文档操作：

- [9.小车组装](https://docs.qq.com/pdf/DRUtjUUJkdFdCUGNN?)
- [10.PWM直流电机](https://docs.qq.com/pdf/DRUtQZ25zcXBvWUpr?)

## 安装`RPi.GPIO`库和`wiringpi`库

> 省流：学期第一、第二节课教过

在树莓派的命令行中运行以下代码：

```
pip3 install RPi.GPIO
pip3 install wiringpi
```

## 下载本项目代码

- （可能更新不及时）[百度网盘下载链接]()
- [zip下载链接](https://codeload.github.com/fdu-dkw/pwm-music-on-raspberrypi/zip/refs/heads/main)
- 命令行`cd`到预期安装目录后，运行如下代码：

  ```
  git clone ...
  ```

# 使用方法

## 测试音准

## 调音

为了更好的听觉体验，代码在不同的树莓派小车上部署后都需要手动调音。~~，否则就准备体验一遍魔音贯耳罢！~~

0. 调音是一项大工程，做好心理准备！

1. 打开一个全音域的调音器设备。它可以是一台专用设备，也可以搜索微信小程序“钢琴调音器”。

2. 固定住树莓派小车的轮子，推荐的做法是让它抵住一面墙。

3. 运行`pwmTuna.py`。命令行中将显示：
   ```
   freq=
   ```
   
4. 输入一个频率，树莓派将输出此频率的PWM波，电机被驱动发生振动。

5. 调音器上会显示实际振动频率、最接近它的音名及其频率。实际频率大概率与你输入的频率值 天 差 地 别。

6. 反复修改输入的频率值，寻找与每个音最接近的频率值，并记录。

7. 结束`pwmTuna.py`。打开`pwmMusic.py`，更改`FREQ`内的频率值，保存，重新运行音准测试。

## 书写乐谱

## 参数说明

## 正在演奏时……

# Bugs以及解决方案

# 关于

## 作者

- 林荫，复旦大学计算机科学与技术(拔尖人才试验班)，2022级
- 邓开文，复旦大学技术科学试验班，2022级
- 俞霁洲，复旦大学技术科学试验班，2022级

联系我们：kwdeng22@m.fudan.edu.cn

## 复旦大学电子系统导论课程
