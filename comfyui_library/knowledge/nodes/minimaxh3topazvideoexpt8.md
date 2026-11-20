# MiniMaxH3TopazVideoEXPT8

## 节点类型

`MiniMaxH3TopazVideoEXPT8`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `topaz_runtime:T8_OFFICIAL_TOPAZ_RUNTIME`（1 次）
- `source_video:VIDEO`（1 次）
- `model_id:COMBO`（1 次）
- `scale:COMBO`（1 次）
- `vram_fraction:FLOAT`（1 次）
- `parameters_json:STRING`（1 次）
- `size_mode:COMBO`（1 次）
- `target_width:INT`（1 次）
- `target_height:INT`（1 次）
- `output_directory:STRING`（1 次）

## 输出

- `enhanced_video:VIDEO`（1 次）
- `source_video:VIDEO`（1 次）
- `saved_path:STRING`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["iris-3", "2x", 0.8, "{}", "scale", 0, 0, "", "", "delivery_h264", "model_defaults", 8, 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
