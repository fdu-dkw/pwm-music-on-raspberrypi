# pwm-music-on-raspberrypi

用电导课小车来演奏音乐🎵Turn your IES car into an instrument🎵

[仓库首页](https://github.com/fdu-dkw/pwm-music-on-raspberrypi) | [下载链接](#下载本项目源码) | [关于作者](#关于)

---

# 设备要求

1. 树莓派4B+

2. 复旦大学电子系统导论课程智能小车套件（[内容清单1](https://docs.qq.com/doc/DY3RHa0laV09oQmRY)、[内容清单2](https://docs.qq.com/doc/DY3F2QnNZeGR4TkFh)）

# 部署方式

## 小车组装与接线

> 省流：拼小车的第一节课教过。注意遵守相同的接线规则。

请参考复旦大学电子系统导论课程文档操作：

- [9.小车组装](https://docs.qq.com/pdf/DRUtjUUJkdFdCUGNN?)
- [10.PWM直流电机](https://docs.qq.com/pdf/DRUtQZ25zcXBvWUpr?)（第23页，键盘控制那个接法）

##  安装`RPi.GPIO`库和`wiringpi`库

> 省流：第一、第二节课教过

在树莓派的命令行中运行以下代码：

```
pip3 install RPi.GPIO
pip3 install wiringpi
```

## 下载本项目源码

- 方式一：[百度网盘下载](https://pan.baidu.com/s/1rBAckSr3fAgxznHPdlaxww?pwd=wqrp)（可能更新不及时）
- 方式二：[zip下载](https://codeload.github.com/fdu-dkw/pwm-music-on-raspberrypi/zip/refs/heads/main)
- 方式三：命令行`cd`到预期安装目录后，运行如下代码：

  ```
  git clone https://github.com/fdu-dkw/pwm-music-on-raspberrypi.git
  ```

# 使用方法

## 测试音准

打开`pwmMusic.py`，直接运行。如果正常运行，你会听到从C4到B6的音阶，每个音高的声音都是“dah-di-di-di-dit”。如果音准有误，需要手动[调音](#调音)。

## 调音

为了更好的听觉体验，代码在不同的树莓派小车上部署后都需要手动调音。~~否则就准备体验一遍魔音贯耳罢！~~

0. 调音是一项大工程，做好心理准备！

1. 打开一个**全音域的**调音器设备。它可以是一台专用设备，也可以搜索微信小程序“钢琴调音器”。

2. **固定住树莓派小车的轮子**，推荐的做法是让它抵住一面墙。

3. 运行`pwmTuna.py`。命令行中将显示：
   ```
   freq=
   ```
   
4. 输入一个频率，树莓派将输出此频率的PWM波，电机被驱动发生振动。

5. 调音器上会显示实际振动频率、最接近它的音名及其频率。实际频率大概率与你输入的频率值 天 差 地 别。

6. 反复修改输入的频率值，寻找与每个音最接近的频率值，并记录。

7. 结束`pwmTuna.py`。打开`pwmMusic.py`，更改`FREQ`内的频率值，保存，重新运行音准测试。

## 书写乐谱

乐谱用音符的列表来描述。音符用包含音名、拍数、断音选项(optional) 的列表来描述。

### 示例

李斯特《钟》节选：

```python
# in La_Campanella.py

SECTION1 = [
    ['f_5', 1/2, HOLD],
    ['f_6', 1/2], ['f_6', 1/2], ['e6', 1/2],
    ['d6', 1/2], ['d6', 1/2], ['c_6', 7/16, HOLD], ['b5', 1/32, HOLD], ['c_6', 1/32, HOLD],
    ['b5', 1/2], ['a_5', 1/2], ['b5', 1/2],
    ['c_6', 1/2, HOLD], ['f_5', 1/2], ['f_5', 7/16, HOLD], ['g5', 1/32, HOLD], ['a5', 1/32, HOLD],
    ['g5', 1/2], ['f_5', 1/2], ['e5', 1/2],
    ['d5', 1/2], ['c_5', 1/2], ['b4', 7/16, HOLD], ['d5', 1/32, HOLD], ['e5', 1/32, HOLD],
    ['d5', 1/2], ['c_5', 1/2], ['b4', 1/2],
    ['f_4', 1]
]
```

`SECTION1`就是一段乐谱。`['f_5', 1/2, HOLD]`和`['f_6', 1/2]`都是音符，前者填入了断音选项，后者省略了。

音名中的下划线`_`代表升号`#`，暂不支持降号。所有支持的音名请见`pwmMusic.py`中的`FREQ`字典。

断音选项可不填，此时默认值为`1`（预设拍数的前$\frac78$奏响，后$\frac18$休止）。若希望在预设拍数期间持续奏响，可以在音符的第三个元素填入`HOLD`（或`0`或`False`）。

## 修改参数

使用`pwmMusic.set()`和`pwmMusic.reset()`方法。

### `pwmMusic.set()`方法

函数声明：

```python
def set(*, ea, i2, i1, eb, i4, i3, bpm, init_freq, duty)
```

**注意：看见第一个参数是星号`*`了吗？直接传递的参数是无效的，一定要使用`参数名=值`的语法来传递参数！**

参数说明：

- `ea, i2, i1, eb, i4, i3`：驱动板各针脚所连的GPIO针脚编号，默认值为`ea=13, i2=19, i1=26, eb=16, i4=20, i3=21`。
  **注意：修改这些数值后，PWM设备会重新初始化，这需要消耗一定时间。**

- `bpm`：速度（每分钟拍数）。

- ~~`init_freq`：启动频率（已弃用）。~~

- `duty`：默认占空比，建议不要超过40。

  > 占空比越小，发声时小车越稳定，但音量越小；
  >
  > 占空比越大，音量越大，但发声时小车可能出现乱窜、摇晃、烧胎等怪象。

### `pwmMusic.reset()`方法

将所有参数恢复默认（并在需要时重启PWM设备）。

默认值：`ea=13, i2=19, i1=26, eb=16, i4=20, i3=21, bpm=60, init_freq=FREQ['b6'], duty=10`。

### 示例

```python
# in La_Campanella.py

pwmMusic.set(bpm=94, duty=10)
```

这行代码设置了速度为每分钟94拍，占空比为10%（这个占空比下小车很稳定，甚至不需要用力固定它），其余为默认值。

**注意：一定要使用`参数名=值`的语法来修改参数！直接传递的参数是无效的。**

## 演奏

使用`pwmMusic.play()`和`pwmMusic.stop()`方法。

### `pwmMusic.play()`方法

还记得之前的乐谱吗？`pwmMusic.play()`方法的参数就是乐谱！

### `pwmMusic.stop()`方法

**注意：千万记得在程序的末尾加上它！** 否则小车可能会 暴 走 。

### 示例

《某科学的超电磁炮》节选：

```python
# in Only_My_Railgun.py

if __name__ == '__main__':
    pwmMusic.set(bpm=135, duty=25)
    pwmMusic.play(SECTION0)
    pwmMusic.play(SECTION1)
    pwmMusic.play(SECTION2)
    pwmMusic.play(SECTION1)
    pwmMusic.stop()
```

其中`SECTION0`、`SECTION1`、`SECTION2`是编写好的乐谱。

演示视频：（[能不能趁机求个三连？👍🪙⭐](https://www.bilibili.com/video/BV1rs4y1m7L4/)）

<iframe src="//player.bilibili.com/player.html?bvid=BV1rs4y1m7L4&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

# Bugs以及解决方案

> 写不动了……出问题[发邮件](#联系我)问吧。

# 关于

## 作者

- 林荫，复旦大学，计算机科学与技术，2022级
- 邓开文，复旦大学，技术科学试验班，2022级
- 俞霁洲，复旦大学，技术科学试验班，2022级

### 联系我
📧e-mail：kwdeng22@m.fudan.edu.cn

## 复旦大学电子系统导论课程

《以开源软硬件为平台，以`Python`为主要编程语言，讲授电子系统的组成和运行原理，包括信号的产生、采集、处理、传输与控制五大模块的基本概念，让学生动手实践并开展自主设计》
