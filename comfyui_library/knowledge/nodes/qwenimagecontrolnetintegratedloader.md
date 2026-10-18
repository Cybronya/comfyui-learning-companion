# QwenImageControlNetIntegratedLoader

## 节点类型

`QwenImageControlNetIntegratedLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `controlnet_data:CONTROL_NET_DATA`（2 次）
- `control_net_name:COMBO`（2 次）
- `control_type:COMBO`（2 次）
- `strength:FLOAT`（2 次）
- `start_percent:FLOAT`（2 次）
- `end_percent:FLOAT`（2 次）

## 输出

- `ControlNet 数据/ControlNet Data:CONTROL_NET_DATA`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["InstantX_Qwen-Image-ControlNet-Union.safetensors", "openpose", 2, 0, 0.5]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
