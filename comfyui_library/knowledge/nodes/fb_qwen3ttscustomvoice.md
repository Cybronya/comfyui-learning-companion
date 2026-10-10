# FB_Qwen3TTSCustomVoice

## 节点类型

`FB_Qwen3TTSCustomVoice`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `custom_speaker:CUSTOM_SPEAKER`（1 次）
- `config:TTS_CONFIG`（1 次）
- `text:STRING`（1 次）
- `speaker:COMBO`（1 次）
- `model_choice:COMBO`（1 次）
- `device:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `language:COMBO`（1 次）
- `seed:INT`（1 次）
- `instruct:STRING`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["你龟儿太过分了，把我的东西都搞坏了，还晓不晓得认错，硬是要把我整冒火你才安逸嗦，莫再烦老子爬球开。", "Vivian", "1.7B", "auto", "bf16", "Auto", 231755699589752, "random`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
