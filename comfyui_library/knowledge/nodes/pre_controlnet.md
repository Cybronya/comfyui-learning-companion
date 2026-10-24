# pre_controlnet

## 节点类型

`pre_controlnet`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `context:RUN_CONTEXT`（1 次）
- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `controlnet1:COMBO`（1 次）
- `strength1:FLOAT`（1 次）
- `start_percent1:FLOAT`（1 次）
- `end_percent1:FLOAT`（1 次）
- `controlnet2:COMBO`（1 次）
- `strength2:FLOAT`（1 次）

## 输出

- `context:RUN_CONTEXT`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["None", 0.5, 0, 1, "None", 1.0100000000000002, 0, 1, "None", 0.5, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
