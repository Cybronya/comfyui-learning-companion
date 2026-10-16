# MiniMaxH3SolEngineDraftToLTXT8Advanced

## 节点类型

`MiniMaxH3SolEngineDraftToLTXT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `frames:IMAGE`（1 次）
- `target_width:INT`（1 次）
- `target_height:INT`（1 次）
- `frame_policy:COMBO`（1 次）
- `fps:FLOAT`（1 次）

## 输出

- `ltx_encoder_frames:IMAGE`（1 次）
- `encoder_width:INT`（1 次）
- `encoder_height:INT`（1 次）
- `kept_frames:INT`（1 次）
- `dropped_tail_frames:INT`（1 次）
- `output_duration_seconds:FLOAT`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1920, 1088, "trim_to_8n_plus_1", 24]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
