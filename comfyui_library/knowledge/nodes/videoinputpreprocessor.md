# VideoInputPreprocessor

## 节点类型

`VideoInputPreprocessor`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `face_processor:FACE_PROCESSOR`（1 次）
- `images:IMAGE`（1 次）
- `face_rgba:IMAGE`（1 次）
- `denoise_strength:FLOAT`（1 次）
- `confidence_threshold:FLOAT`（1 次）
- `face_crop_scale:FLOAT`（1 次）
- `dilation_kernel_size:INT`（1 次）
- `with_neck:BOOLEAN`（1 次）
- `face_only_mode:BOOLEAN`（1 次）
- `feather_amount:INT`（1 次）

## 输出

- `processed_images:IMAGE`（1 次）
- `denoise_strength:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.5, 0.5, 1.5, 10, true, false, 21, 0.05]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
