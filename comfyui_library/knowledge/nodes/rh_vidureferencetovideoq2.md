# RH_ViduReferenceToVideoQ2

## 节点类型

`RH_ViduReferenceToVideoQ2`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image1:IMAGE`（2 次）
- `image2:IMAGE`（2 次）
- `image3:IMAGE`（2 次）
- `image4:IMAGE`（2 次）
- `image5:IMAGE`（2 次）
- `image6:IMAGE`（2 次）
- `image7:IMAGE`（2 次）
- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `aspectRatio:COMBO`（2 次）

## 输出

- `video:VIDEO`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "3:4", "1080p", "5", "auto", false, 721529722015373, "randomize"]`（1 次）
- `["", "9:16", "540p", "5", "auto", false, 1078036430, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
