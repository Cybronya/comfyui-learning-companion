# WhisperTurboRun

## 节点类型

`WhisperTurboRun`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `audio:AUDIO`（2 次）
- `max_num_words_per_page:INT`（2 次）
- `logprob_threshold:FLOAT`（2 次）
- `no_speech_threshold:FLOAT`（2 次）
- `timestamp:BOOLEAN`（2 次）
- `word_timestamps:BOOLEAN`（2 次）
- `unload_model:BOOLEAN`（2 次）

## 输出

- `text:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, -0.1, 0.03, false, false, false]`（1 次）
- `[24, -0.1, 0.03, true, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
