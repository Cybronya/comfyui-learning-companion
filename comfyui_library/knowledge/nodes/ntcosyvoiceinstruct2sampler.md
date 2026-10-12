# NTCosyVoiceInstruct2Sampler

## 节点类型

`NTCosyVoiceInstruct2Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `audio:AUDIO`（9 次）
- `speed:FLOAT`（4 次）
- `text:STRING`（4 次）
- `instruct:STRING`（4 次）

## 输出

- `tts_speech:AUDIO`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "大家好，我是高允贞，", ""]`（5 次）
- `[1, "", ""]`（2 次）
- `[1, "Myshell friends, thank you for your continued support for Myshell. Thank you. Thank you also to our classmate Bobo,`（1 次）
- `[1, "你好，我是你的专属数字人，有什么可以帮到你", "a female host with beautiful voice"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
