# SparkTTS_AdvVoiceClone

## 节点类型

`SparkTTS_AdvVoiceClone`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `reference_audio:AUDIO`（3 次）
- `text:STRING`（3 次）
- `reference_text:STRING`（3 次）
- `pitch:COMBO`（2 次）
- `speed:COMBO`（2 次）
- `max_tokens:INT`（2 次）
- `batch_texts:STRING`（2 次）
- `temperature:FLOAT`（2 次）
- `top_k:INT`（2 次）
- `top_p:FLOAT`（2 次）

## 输出

- `audio:AUDIO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["This is the SparkTTS advanced voice clone node, you can clone the voice from a reference audio with control over pitch`（2 次）
- `["那你帮我去把竞品的发财树浇死", "左手都不用从车把上抬起来，我低头看了一眼表，现在是早上八点半。虽然车速高达六十英里，但是迎面而来的风依旧潮热难忍。我不禁想，一大早就已经这么闷热，到了下午可该如何是好啊！", "moderate", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
