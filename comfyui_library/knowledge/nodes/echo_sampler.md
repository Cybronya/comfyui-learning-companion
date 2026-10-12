# Echo_Sampler

## 节点类型

`Echo_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `audio:AUDIO`（4 次）
- `model:MODEL_PIPE_E`（4 次）
- `face_detector:MODEL_FACE_E`（4 次）
- `visualizer:MODEL_VISUAL_E`（4 次）
- `video_images:IMAGE`（4 次）

## 输出

- `image:IMAGE`（4 次）
- `audio:AUDIO`（4 次）
- `frame_rate:FLOAT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["none", 99522024, "randomize", 2.5, 30, 25, 16000, 0.1, 0.8, 12, 3, 120, 512, 512, false]`（1 次）
- `["none", 1931580885, "randomize", 2.5, 30, 25, 16000, 0.1, 0.8, 12, 3, 120, 512, 512, false]`（1 次）
- `["none", 731438432, "randomize", 2.5, 30, 25, 16000, 0.1, 0.8, 12, 3, 120, 512, 512, false]`（1 次）
- `["none", 215702086, "randomize", 2.5, 30, 25, 16000, 0.1, 0.8, 12, 3, 120, 768, 768, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
