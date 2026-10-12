# InteractAvatar_SM_Model

## 节点类型

`InteractAvatar_SM_Model`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `dit:COMBO`（4 次）
- `gguf:COMBO`（4 次）
- `lora:COMBO`（4 次）
- `back_append_frame:COMBO`（4 次）
- `offload:BOOLEAN`（4 次）

## 输出

- `model:MODEL`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["interact-avatar.safetensors", "none", "none", 1, true]`（2 次）
- `["interact-avatar-long.safetensors", "none", "none", 2, true]`（1 次）
- `["interact-avatar.safetensors", "none", "none", 2, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
