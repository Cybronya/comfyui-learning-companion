# MiniMaxH3ChainPlan

## 节点类型

`MiniMaxH3ChainPlan`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `plan_json_input:STRING`（1 次）
- `plan_json:STRING`（1 次）
- `run_name:STRING`（1 次）
- `generation_fingerprint:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `context_length:COMBO`（1 次）
- `encode_mode:COMBO`（1 次）
- `anchor_mode:COMBO`（1 次）
- `crop:COMBO`（1 次）

## 输出

- `plan:H3_CHAIN_PLAN`（1 次）
- `summary:STRING`（1 次）
- `clip_count:INT`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `video_blend_frames:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["{\n  \"prompt_prefix\": [],\n  \"shots\": [\n    {\n      \"id\": \"reference_delivery\",\n      \"prompt\": [\n      `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
