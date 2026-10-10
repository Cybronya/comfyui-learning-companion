# MiniMaxH3ChainReview

## 节点类型

`MiniMaxH3ChainReview`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `state:H3_CHAIN_STATE`（1 次）
- `segment:H3_CHAIN_SEGMENT`（1 次）
- `audio:AUDIO`（1 次）
- `source_audio:AUDIO`（1 次）
- `enabled:BOOLEAN`（1 次）
- `play_notification_sound:BOOLEAN`（1 次）
- `auto_continue_timeout_minutes:FLOAT`（1 次）
- `unload_models_while_waiting:BOOLEAN`（1 次）
- `assemble_partial_on_stop:BOOLEAN`（1 次）
- `partial_audio_source:COMBO`（1 次）

## 输出

- `segment:H3_CHAIN_SEGMENT`（1 次）
- `status:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, false, 0, false, true, "checkpointed"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
