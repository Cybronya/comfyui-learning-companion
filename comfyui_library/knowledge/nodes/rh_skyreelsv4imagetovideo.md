# RH_SkyreelsV4ImageToVideo

## 节点类型

`RH_SkyreelsV4ImageToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `first_frame_image:IMAGE`（2 次）
- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `sound:BOOLEAN`（2 次）
- `duration:INT`（2 次）
- `mode:COMBO`（2 次）
- `skip_error:BOOLEAN`（2 次）
- `seed:INT`（2 次）

## 输出

- `video:VIDEO`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["女子在跳舞", false, 3, "std", false, 886681311657661, "randomize"]`（1 次）
- `["", false, 5, "std", false, 30766717856197, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
