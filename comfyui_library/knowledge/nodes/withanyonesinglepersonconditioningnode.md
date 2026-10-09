# WithAnyoneSinglePersonConditioningNode

## 节点类型

`WithAnyoneSinglePersonConditioningNode`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `withAnyone_pipeline:WITHANYONE_PIPELINE`（9 次）
- `ref_img:IMAGE`（9 次）
- `bbox:STRING`（9 次）

## 输出

- `person_conditioning:PERSON_CONDITIONING`（9 次）
- `debug_bbox_image:IMAGE`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[""]`（5 次）
- `[0.2]`（3 次）
- `[0.8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
