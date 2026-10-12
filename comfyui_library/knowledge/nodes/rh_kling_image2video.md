# RH_Kling_Image2Video

## 节点类型

`RH_Kling_Image2Video`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `image_tail:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `model_name:COMBO`（1 次）
- `imagination:FLOAT`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `mode:COMBO`（1 次）
- `duration:COMBO`（1 次）
- `num_videos:INT`（1 次）
- `negative_prompt:STRING`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `video_url:STRING`（1 次）
- `task_id:STRING`（1 次）
- `video_id:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["【在此输入编辑提示词】", "kling-v1-6", 0.5, "9:16", "std", "5", 1, "", 1832832653, "randomize", "", "none", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
