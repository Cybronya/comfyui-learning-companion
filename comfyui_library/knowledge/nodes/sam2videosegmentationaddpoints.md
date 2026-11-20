# Sam2VideoSegmentationAddPoints

## 节点类型

`Sam2VideoSegmentationAddPoints`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `sam2_model:SAM2MODEL`（5 次）
- `coordinates_positive:STRING`（5 次）
- `image:IMAGE`（5 次）
- `coordinates_negative:STRING`（5 次）
- `prev_inference_state:SAM2INFERENCESTATE`（5 次）
- `frame_index:INT`（3 次）
- `object_index:INT`（3 次）

## 输出

- `sam2_model:SAM2MODEL`（5 次）
- `inference_state:SAM2INFERENCESTATE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0]`（2 次）
- `[0, 1]`（1 次）
- `["", 0, 1, ""]`（1 次）
- `["", 0, 0, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
