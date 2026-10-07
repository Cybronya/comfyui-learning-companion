# QwenVLDetection

## 节点类型

`QwenVLDetection`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `qwen_model:QWEN_MODEL`（4 次）
- `image:IMAGE`（4 次）
- `target:STRING`（4 次）
- `bbox_selection:STRING`（4 次）
- `score_threshold:FLOAT`（4 次）
- `merge_boxes:BOOLEAN`（4 次）

## 输出

- `text:JSON`（4 次）
- `bboxes:BBOX`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["深黄衣服黑头发的女人", "all", 0, false]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
