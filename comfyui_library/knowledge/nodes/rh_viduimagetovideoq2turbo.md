# RH_ViduImageToVideoQ2Turbo

## 节点类型

`RH_ViduImageToVideoQ2Turbo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `duration:COMBO`（2 次）
- `resolution:COMBO`（2 次）
- `movementAmplitude:COMBO`（2 次）
- `bgm:BOOLEAN`（2 次）
- `skip_error:BOOLEAN`（2 次）
- `seed:INT`（2 次）

## 输出

- `video:VIDEO`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "5", "720p", "auto", true, false, 883094054864138, "randomize"]`（1 次）
- `["", "8", "1080p", "auto", true, false, 451319291, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
