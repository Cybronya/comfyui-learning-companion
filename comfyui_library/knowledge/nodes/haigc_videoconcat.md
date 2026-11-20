# HAIGC_VideoConcat

## 节点类型

`HAIGC_VideoConcat`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video_1:HAIGC_VIDEOINFO`（1 次）
- `video_2:HAIGC_VIDEOINFO`（1 次）
- `video_3:HAIGC_VIDEOINFO`（1 次）
- `video_4:HAIGC_VIDEOINFO`（1 次）
- `video_5:HAIGC_VIDEOINFO`（1 次）
- `video_6:HAIGC_VIDEOINFO`（1 次）
- `video_7:HAIGC_VIDEOINFO`（1 次）
- `video_8:HAIGC_VIDEOINFO`（1 次）
- `video_9:HAIGC_VIDEOINFO`（1 次）
- `video_10:HAIGC_VIDEOINFO`（1 次）

## 输出

- `拼接图像:IMAGE`（1 次）
- `拼接音频:AUDIO`（1 次）
- `video_info:HAIGC_VIDEOINFO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 0, "contain"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
