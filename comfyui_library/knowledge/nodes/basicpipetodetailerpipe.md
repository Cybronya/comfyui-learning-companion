# BasicPipeToDetailerPipe

## 节点类型

`BasicPipeToDetailerPipe`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `basic_pipe:BASIC_PIPE`（1 次）
- `bbox_detector:BBOX_DETECTOR`（1 次）
- `sam_model_opt:SAM_MODEL`（1 次）
- `segm_detector_opt:SEGM_DETECTOR`（1 次）
- `detailer_hook:DETAILER_HOOK`（1 次）

## 输出

- `detailer_pipe:DETAILER_PIPE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "Select the LoRA to add to the text", "Select the Wildcard to add to the text"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
