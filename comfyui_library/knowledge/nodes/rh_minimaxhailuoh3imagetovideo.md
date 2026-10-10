# RH_MinimaxHailuoH3ImageToVideo

## 节点类型

`RH_MinimaxHailuoH3ImageToVideo`

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
- `prompt:STRING`（1 次）
- `resolution:COMBO`（1 次）
- `duration:COMBO`（1 次）
- `skip_error:BOOLEAN`（1 次）
- `seed:INT`（1 次）
- `aigc_watermark:BOOLEAN`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["阳光明媚的海滩上，白裙美女沿着海岸缓慢行走。海风轻轻吹动长发和裙摆，海浪自然拍打沙滩。她从面向镜头微笑，逐渐低下头，抬手将头发拨到耳后，自然过渡至尾帧姿势。镜头平稳缓慢推进，人物、服装和背景保持一致，动作柔和流畅，清新浪漫的电影质感。"`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
