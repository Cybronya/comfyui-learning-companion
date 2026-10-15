# R2T2Transcribe

## 节点类型

`R2T2Transcribe`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:R2T2_MODEL`（1 次）
- `audio:AUDIO`（1 次）
- `mode:COMBO`（1 次）
- `language:COMBO`（1 次）
- `context:STRING`（1 次）
- `hotwords:STRING`（1 次）
- `channel:COMBO`（1 次）
- `auto_gain:BOOLEAN`（1 次）
- `stream_chunk_ms:INT`（1 次）

## 输出

- `text:STRING`（1 次）
- `language:STRING`（1 次）
- `result_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["offline", "Auto", "", "", "mean", false, 160]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
