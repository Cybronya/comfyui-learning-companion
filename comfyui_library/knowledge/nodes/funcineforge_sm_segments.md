# FunCineForge_SM_Segments

## 节点类型

`FunCineForge_SM_Segments`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `conds:CONDITIONING`（2 次）
- `refer_audio:AUDIO`（2 次）
- `text:STRING`（2 次）
- `clue:STRING`（2 次）
- `start_time:FLOAT`（2 次）
- `end_time:FLOAT`（2 次）
- `age_input:COMBO`（2 次）
- `gender_input:COMBO`（2 次）
- `spk:COMBO`（2 次）

## 输出

- `conds:CONDITIONING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["触发词已经打好了,现在，只要我念出这个词，你必须立刻给我反应。", "一位成熟的女性御姐角色，以诱惑和极具攻击性的语调来述说", 0, 11.000000000000002, "青年", "女", 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
