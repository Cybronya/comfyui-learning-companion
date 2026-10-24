# easy controlnetStack

## 节点类型

`easy controlnetStack`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `optional_controlnet_stack:CONTROL_NET_STACK`（3 次）
- `image_1:IMAGE`（3 次）
- `image_2:IMAGE`（3 次）
- `image_3:IMAGE`（3 次）
- `toggle:BOOLEAN`（2 次）
- `mode:COMBO`（2 次）
- `num_controlnet:INT`（2 次）
- `controlnet_1:COMBO`（2 次）
- `controlnet_1_strength:FLOAT`（2 次）
- `start_percent_1:FLOAT`（2 次）

## 输出

- `controlnet_stack:CONTROL_NET_STACK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "advanced", 3, "control_v1p_sd15_qrcode_monster.safetensors", 1.1700000000000002, 0, 1, 1, "control_v1p_sd15_brig`（2 次）
- `[false, "simple", 2, "OpenPoseXL2.safetensors", 0.7000000000000002, 0, 1, 1, "controlnet-sd-xl-1.0-softedge-dexined.safe`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
