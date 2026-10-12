# DeepFuzeAdavance

## 节点类型

`DeepFuzeAdavance`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `audio:AUDIO`（1 次）
- `meta_batch:VHS_BatchManager`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `frame_count:INT`（1 次）
- `audio:AUDIO`（1 次）
- `video_info:VHS_VIDEOINFO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["gfpgan_1.4", "real_esrgan_x2", 0, 0, 0, 0, 0, 0, "cuda", 25, 0, "deepfuze", false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
