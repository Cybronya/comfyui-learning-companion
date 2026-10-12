# RH_Veo31_Fast_Image2Video_Official

## 节点类型

`RH_Veo31_Fast_Image2Video_Official`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `last_image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `duration:COMBO`（1 次）
- `resolution:COMBO`（1 次）
- `generate_audio:BOOLEAN`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `negative_prompt:STRING`（1 次）
- `seed:INT`（1 次）

## 输出

- `video:VIDEO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "8", "720p", true, "16:9", "", 2025875594, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
