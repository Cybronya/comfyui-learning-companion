# AV_ControlNetEfficientStackerSimple

## 节点类型

`AV_ControlNetEfficientStackerSimple`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `cnet_stack:CONTROL_NET_STACK`（1 次）
- `timestep_keyframe:TIMESTEP_KEYFRAME`（1 次）

## 输出

- `CNET_STACK:CONTROL_NET_STACK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SDXL-union_promax.safetensors", 0.6000000000000001, "depth_anything_v2", "None", 1024, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
