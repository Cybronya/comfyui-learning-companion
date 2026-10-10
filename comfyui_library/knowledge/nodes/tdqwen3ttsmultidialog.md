# TDQwen3TTSMultiDialog

## 节点类型

`TDQwen3TTSMultiDialog`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:QWEN3_TTS_MODEL`（1 次）
- `speaker_list:SPEAKER_LIST`（1 次）
- `speaker_1:SPEAKER`（1 次）
- `text:STRING`（1 次）
- `interval:FLOAT`（1 次）
- `seed:INT`（1 次）
- `speaker_2:SPEAKER`（1 次）
- `speaker_3:SPEAKER`（1 次）
- `speaker_4:SPEAKER`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["李追远:你好，今天天气真不错。\n崔桂英:是啊，桃子你打算去哪里玩。\n李追远:不知道啊，土豆你想去哪里。\n崔桂英:我们去肥西的家里吧。", 0.5, 62556003384494, "fixed"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
