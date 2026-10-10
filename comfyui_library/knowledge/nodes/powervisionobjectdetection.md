# PowerVisionObjectDetection

## 节点类型

`PowerVisionObjectDetection`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `qwen_model:QWEN_MODEL`（1 次）
- `image:IMAGE`（1 次）
- `target:STRING`（1 次）
- `bbox_selection:STRING`（1 次）
- `score_threshold:FLOAT`（1 次）
- `merge_boxes:BOOLEAN`（1 次）
- `unload_model:BOOLEAN`（1 次）

## 输出

- `detection_result:JSON`（1 次）
- `bboxes:BBOX`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["object", "all", 0.3500000000000001, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
