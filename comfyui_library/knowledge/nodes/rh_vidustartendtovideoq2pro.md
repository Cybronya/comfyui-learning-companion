# RH_ViduStartEndToVideoQ2Pro

## 节点类型

`RH_ViduStartEndToVideoQ2Pro`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `first_image:IMAGE`（1 次）
- `last_image:IMAGE`（1 次）
- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `duration:COMBO`（1 次）
- `resolution:COMBO`（1 次）
- `movementAmplitude:COMBO`（1 次）
- `bgm:BOOLEAN`（1 次）
- `skip_error:BOOLEAN`（1 次）
- `seed:INT`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "5", "720p", "auto", true, false, 44897794199474, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
