# NTCosyVoiceCrossLingualSampler

## 节点类型

`NTCosyVoiceCrossLingualSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `audio:AUDIO`（6 次）

## 输出

- `tts_speech:AUDIO`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "T8,我现在越来越厉害了，我觉得我能同时操作3个，你快想想办法，现在只能一开，太慢啦"]`（2 次）
- `[1, "大家好，我是贞贞，今天又要给大家新数字人啦"]`（2 次）
- `[1, "大家好，我是高允贞，"]`（1 次）
- `[1, "がよかったので"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
