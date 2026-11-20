# Sam2VideoSegmentation

## 节点类型

`Sam2VideoSegmentation`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `sam2_model:SAM2MODEL`（5 次）
- `inference_state:SAM2INFERENCESTATE`（5 次）
- `keep_model_loaded:BOOLEAN`（3 次）

## 输出

- `mask:MASK`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true]`（4 次）
- `[false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
