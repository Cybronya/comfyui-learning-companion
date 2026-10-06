# CR Multi-ControlNet Stack

## 节点类型

`CR Multi-ControlNet Stack`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image_1:IMAGE`（2 次）
- `image_2:IMAGE`（2 次）
- `image_3:IMAGE`（2 次）
- `controlnet_stack:CONTROL_NET_STACK`（2 次）

## 输出

- `CONTROLNET_STACK:CONTROL_NET_STACK`（2 次）
- `show_help:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["On", "MistoLine/mistoLine_rank256.safetensors", 1, 0, 1, "On", "diffusers_xl_depth_full.safetensors", 1, 0, 1, "Off", `（1 次）
- `["On", "MistoLine/mistoLine_rank256.safetensors", 1, 0, 1, "On", "diffusers_xl_depth_full.safetensors", 1, 0, 1, "On", "`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
