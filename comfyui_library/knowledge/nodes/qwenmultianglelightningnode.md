# QwenMultiangleLightningNode

## 节点类型

`QwenMultiangleLightningNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `light_azimuth:INT`（1 次）
- `light_elevation:INT`（1 次）
- `light_intensity:FLOAT`（1 次）
- `light_color_hex:STRING`（1 次）
- `cinematic_mode:BOOLEAN`（1 次）

## 输出

- `lighting_prompt:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[9, -90, 0.9, "#d8c3df", true, "", "[{\"azimuth\":9,\"elevation\":-90,\"intensity\":0.9,\"color\":\"#d8c3df\"}]"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
