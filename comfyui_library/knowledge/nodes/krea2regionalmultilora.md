# Krea2RegionalMultiLoRA

## 节点类型

`Krea2RegionalMultiLoRA`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `bboxes:BOUNDING_BOX`（1 次）
- `canvas_width:INT`（1 次）
- `canvas_height:INT`（1 次）
- `regions_json:STRING`（1 次）
- `split_mode:COMBO`（1 次）
- `seam_feather:FLOAT`（1 次）
- `blend_override:FLOAT`（1 次）
- `base_strength:FLOAT`（1 次）

## 输出

- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `masks:KREA2_MASKS`（1 次）
- `data:KREA2_DATA`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 1024, "[\n  {\n    \"lora\": \"None\",\n    \"strength\": 1.1,\n    \"enable\": false\n  }\n]", "bbox", 0.03, 0, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
