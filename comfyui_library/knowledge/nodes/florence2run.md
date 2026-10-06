# Florence2Run

## 节点类型

`Florence2Run`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `florence2_model:FL2MODEL`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `mask:MASK`（3 次）
- `caption:STRING`（3 次）
- `data:JSON`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["hair", "caption_to_phrase_grounding", true, false, 1024, 3, true, "", 42, "fixed"]`（1 次）
- `["", "more_detailed_caption", true, false, 1024, 3, true, "", 443091948470476, "fixed"]`（1 次）
- `["", "more_detailed_caption", true, false, 1024, 3, true, "", 420340816912160, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
