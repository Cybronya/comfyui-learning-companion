# RunningHub StepAudioEditX Sampler(Clone)

## 节点类型

`RunningHub StepAudioEditX Sampler(Clone)`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `model:RHSAEditXModel`（6 次）
- `prompt_audio:AUDIO`（6 次）
- `prompt_text:STRING`（6 次）
- `generated_text:STRING`（6 次）
- `seed:INT`（6 次）

## 输出

- `audio:AUDIO`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["原音频内容", "我是一只聪明的猫猫", 1071729073849561, "randomize"]`（1 次）
- `["原音频内容", "大家好啊，[Dissatisfaction-Oh] 今天是2025年11月18日，我们会越来越好的", 480469020463341, "randomize"]`（1 次）
- `["原音频内容", "我是一只聪明的猫猫", 833682373367182, "randomize"]`（1 次）
- `["原音频内容", "希望生成的内容", 153050056247615, "randomize"]`（1 次）
- `["原音频内容", "", 846959495099056, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
