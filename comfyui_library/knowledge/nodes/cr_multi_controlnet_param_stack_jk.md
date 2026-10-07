# CR Multi-ControlNet Param Stack JK

## 节点类型

`CR Multi-ControlNet Param Stack JK`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `controlnet_0:CONTROL_NET`（1 次）
- `image_0:IMAGE`（1 次）
- `controlnet_1:CONTROL_NET`（1 次）
- `image_1:IMAGE`（1 次）
- `controlnet_2:CONTROL_NET`（1 次）
- `image_2:IMAGE`（1 次）
- `controlnet_3:CONTROL_NET`（1 次）
- `image_3:IMAGE`（1 次）
- `controlnet_4:CONTROL_NET`（1 次）
- `image_4:IMAGE`（1 次）

## 输出

- `CONTROLNET_STACK:CONTROL_NET_STACK`（1 次）
- `ContrlNet_Switch:BOOLEAN`（1 次）
- `ContrlNet0_Switch:BOOLEAN`（1 次）
- `ContrlNet1_Switch:BOOLEAN`（1 次）
- `ContrlNet2_Switch:BOOLEAN`（1 次）
- `ContrlNet3_Switch:BOOLEAN`（1 次）
- `ContrlNet4_Switch:BOOLEAN`（1 次）
- `ContrlNet5_Switch:BOOLEAN`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, true, 1, 0, 1, true, 1, 0, 1, false, 1, 0, 1, false, 1, 0, 1, false, 1, 0, 1, false, 1, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
