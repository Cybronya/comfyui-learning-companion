# SparkTTS_VoiceCreator

## 节点类型

`SparkTTS_VoiceCreator`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `text:STRING`（1 次）
- `gender:COMBO`（1 次）
- `pitch:COMBO`（1 次）
- `speed:COMBO`（1 次）
- `batch_texts:STRING`（1 次）

## 输出

- `audio:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["那你帮我去把竞品的发财树浇死", "female", "moderate", "moderate", ""]`（1 次）
- `["王大炮！我爱你！我的人，和我的心，和我的整个灵魂，都在说！我选你！", "female", "moderate", "moderate", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
