# HAIGC_VideoTransition

## 节点类型

`HAIGC_VideoTransition`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `视频A:IMAGE`（3 次）
- `视频B:IMAGE`（3 次）
- `过渡类型:COMBO`（3 次）
- `过渡时长帧数:INT`（3 次）
- `过渡位置:COMBO`（3 次）
- `缓动函数:COMBO`（3 次）
- `边缘羽化:INT`（3 次）

## 输出

- `合成视频:IMAGE`（3 次）
- `总帧数:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["交叉淡化", 30, "两者中间", "缓入缓出", 0]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
