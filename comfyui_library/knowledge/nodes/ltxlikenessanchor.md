# LTXLikenessAnchor

## 节点类型

`LTXLikenessAnchor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `reference_info:REFERENCE_INFO`（2 次）
- `strength:FLOAT`（2 次）
- `reference_source:COMBO`（2 次）
- `frame_0_bbox:STRING`（2 次）
- `similarity_threshold:FLOAT`（2 次）
- `decay_with_distance:FLOAT`（2 次）
- `bypass:BOOLEAN`（2 次）
- `debug:BOOLEAN`（2 次）
- `advanced_mode:BOOLEAN`（2 次）

## 输出

- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.5, "auto", "", 0.5, 0, false, false, false, "middle", "", 8, "", 0, "directional", 0.4]`（1 次）
- `[0.25, "auto", "", 0.22, 0, false, false, false, "middle", "", 8, "", 0, "directional", 0.4]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
