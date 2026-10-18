# Qwen3ForcedAlign

## 节点类型

`Qwen3ForcedAlign`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `aligner:QWEN3_ALIGNER`（4 次）
- `audio:AUDIO`（4 次）
- `text:STRING`（4 次）
- `language:COMBO`（4 次）
- `segment_by_sentence:BOOLEAN`（3 次）

## 输出

- `timestamps:STRING`（4 次）
- `text_list:STRING`（3 次）
- `start_times:STRING`（3 次）
- `end_times:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "Chinese", true]`（2 次）
- `["", "Chinese"]`（1 次）
- `["我叫陈明，因为庄大运来到这个平行世界，好在及时觉醒了系统，穿越后保住一命，可代价却是我反手欠了系统整整一百个亿。嗯啊啊啊！系统，你除了讨债就没有别的能力了吗？啊啊啊！只要得到足够的打赏还账，就不用变植物人了。要是运气好，能多赚几笔，还能`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
