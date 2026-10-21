# Krea2StyleSemanticConditioning

## 节点类型

`Krea2StyleSemanticConditioning`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）
- `style_image:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `style_strength:COMBO`（2 次）
- `vision_resolution:INT`（2 次）
- `custom_instruction:STRING`（2 次）

## 输出

- `条件:CONDITIONING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "平衡", 384, ""]`（1 次）
- `["", "轻微", 768, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
