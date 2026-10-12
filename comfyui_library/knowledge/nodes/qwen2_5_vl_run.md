# Qwen2_5_VL_Run

## 节点类型

`Qwen2_5_VL_Run`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `Qwen2_5_VL_model:QWEN2_5_VL_MODEL`（1 次）
- `image:IMAGE`（1 次）
- `video:VIDEO`（1 次）
- `BatchImage:BatchImage`（1 次）
- `text:STRING`（1 次）
- `video_decode_method:COMBO`（1 次）
- `max_new_tokens:INT`（1 次）
- `min_pixels:INT`（1 次）
- `max_pixels:INT`（1 次）
- `total_pixels:INT`（1 次）

## 输出

- `text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["请你扮演一位专业的电影分析师和顶尖的AI提示词工程师。你的核心任务是，基于我刚刚上传的视频文件，对其进行分镜解构，并为每个关键分镜逆向推导出其对应的、能够生成该画面的运镜提示词，要求：\n\n提示词=运动(运动描述)+镜头语言。不要描述`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
