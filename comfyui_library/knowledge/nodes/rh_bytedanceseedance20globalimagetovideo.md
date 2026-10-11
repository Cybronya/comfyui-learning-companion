# RH_BytedanceSeedance20GlobalImageToVideo

## 节点类型

`RH_BytedanceSeedance20GlobalImageToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `first_frame:IMAGE`（1 次）
- `last_frame:IMAGE`（1 次）
- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `resolution:COMBO`（1 次）
- `duration:COMBO`（1 次）
- `prompt:STRING`（1 次）
- `generateAudio:BOOLEAN`（1 次）
- `ratio:COMBO`（1 次）
- `realPersonMode:BOOLEAN`（1 次）
- `skip_error:BOOLEAN`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）
- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["720p", "10", "起始画面为女生漂浮在泳池水面，面部铺满水波流动光影，发丝半浸水中，水面漂浮浅色花朵；镜头缓慢向下缓缓推入水面，画面随镜头运镜自然沉入水下空间，水流缓缓晃动，发丝与白色衣衫随水体轻柔舒展飘散，细碎气泡缓缓向上升`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
