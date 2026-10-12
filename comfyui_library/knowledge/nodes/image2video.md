# Image2Video

## 节点类型

`Image2Video`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images:IMAGE`（2 次）
- `fps:INT`（2 次）
- `img_frame_size:INT`（2 次）
- `filename_prefix:STRING`（2 次）

## 输出

- `视频文件名:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[20, 1, "comfyUI", "视频保存成功文件地址：/data/ComfyUI/personal/b81e105509634463c8d86683b129f600/output/video/comfyUI_00001_.mp4"]`（1 次）
- `[20, 1, "comfyUI", "视频保存成功文件地址：/data/ComfyUI/personal/a69eb7d1be6d0b446b05bbd399d62a9a/output/video/comfyUI_00001_.mp4"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
