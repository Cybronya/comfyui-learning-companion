# FB_Qwen3TTSVoiceDesign

## 节点类型

`FB_Qwen3TTSVoiceDesign`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `config:TTS_CONFIG`（2 次）
- `text:STRING`（2 次）
- `instruct:STRING`（2 次）
- `model_choice:COMBO`（2 次）
- `device:COMBO`（2 次）
- `precision:COMBO`（2 次）
- `language:COMBO`（2 次）
- `seed:INT`（2 次）
- `max_new_tokens:INT`（2 次）
- `top_p:FLOAT`（2 次）

## 输出

- `audio:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["算了吧……我都已经，不在乎了。", "", "1.7B", "auto", "bf16", "Auto", 925098855635403, "randomize", 2048, 0.8, 20, 1, 1.05, "auto", fa`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
