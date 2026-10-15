# BerniniTextEncodeCached

## 节点类型

`BerniniTextEncodeCached`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_name:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `task_type:COMBO`（1 次）
- `positive_prompt:STRING`（1 次）
- `negative_prompt:STRING`（1 次）
- `quantization:COMBO`（1 次）
- `use_disk_cache:BOOLEAN`（1 次）
- `device:COMBO`（1 次）
- `extender_args:WANVIDEOPROMPTEXTENDER_ARGS`（1 次）

## 输出

- `text_embeds:WANVIDEOTEXTEMBEDS`（1 次）
- `negative_text_embeds:WANVIDEOTEXTEMBEDS`（1 次）
- `positive_prompt:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["umt5-xxl-enc-bf16.safetensors", "bf16", "r2v — 参考主体生视频(Reference to Video)", "将人物的头发换成红色", "bad video", "disabled", tr`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
