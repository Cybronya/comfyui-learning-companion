# Qwen3VLAPINode

## 节点类型

`Qwen3VLAPINode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `video:VIDEO`（1 次）
- `text_prompt:STRING`（1 次）
- `provider:COMBO`（1 次）
- `api_key:STRING`（1 次）
- `model_name:COMBO`（1 次）
- `max_tokens:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `stream:BOOLEAN`（1 次）

## 输出

- `text_output:STRING`（1 次）
- `raw_response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["描述这张图片。", "硅基流动API", "sk-hedsrwhrhqlggkseqkkvcfxkjkpcuhbizmtpgifolmjgslpm", "[siliconflow]Qwen/Qwen3-VL-235B-A22B-Inst`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
