# MiniMaxH3TopazFrameInterpolationEXPT8

## 节点类型

`MiniMaxH3TopazFrameInterpolationEXPT8`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `topaz_runtime:T8_OFFICIAL_TOPAZ_RUNTIME`（1 次）
- `source_video:VIDEO`（1 次）
- `model_id:COMBO`（1 次）
- `multiplier:COMBO`（1 次）
- `duplicate_threshold:FLOAT`（1 次）
- `vram_fraction:FLOAT`（1 次）
- `output_directory:STRING`（1 次）
- `custom_model_id:STRING`（1 次）
- `engine_instances:INT`（1 次）
- `output_profile:COMBO`（1 次）

## 输出

- `interpolated_video:VIDEO`（1 次）
- `source_video:VIDEO`（1 次）
- `saved_path:STRING`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["apo-8", "2x", 0.01, 0.8, "", "", 0, "delivery_h264", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
