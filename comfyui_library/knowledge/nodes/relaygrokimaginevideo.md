# RelayGrokImagineVideo

## 节点类型

`RelayGrokImagineVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `api_key:STRING`（1 次）
- `resolution:COMBO`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `duration:COMBO`（1 次）
- `after_control:COMBO`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `task_id:STRING`（1 次）
- `response:STRING`（1 次）
- `video_url:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["0-3秒，女孩边打游戏边介绍鼠标垫\n3-5秒，手握住鼠标滑过鼠标垫\n5-7秒，女孩伸懒腰\n7-10秒，给一个全景特写", "grok-imagine-video", "sk-6yFPQADrWJ2dlhNScPnCEo3Lwfat`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
