# VideoCombine_Adv

## 节点类型

`VideoCombine_Adv`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_batch:IMAGE`（1 次）
- `frame_rate:INT`（1 次）
- `loop_count:INT`（1 次）
- `filename_prefix:STRING`（1 次）
- `format:COMBO`（1 次）
- `pingpong:BOOLEAN`（1 次）
- `save_image:BOOLEAN`（1 次）
- `metadata:BOOLEAN`（1 次）

## 输出

- `scenes_video:SCENE_VIDEO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[25, 0, "Comfyui", "video/h264-mp4", false, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
