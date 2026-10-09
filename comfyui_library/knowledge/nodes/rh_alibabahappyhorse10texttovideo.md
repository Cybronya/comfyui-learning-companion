# RH_AlibabaHappyhorse10TextToVideo

## 节点类型

`RH_AlibabaHappyhorse10TextToVideo`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `resolution:COMBO`（2 次）
- `duration:COMBO`（2 次）
- `aspectRatio:COMBO`（2 次）
- `seed:INT`（2 次）
- `skip_error:BOOLEAN`（2 次）

## 输出

- `video:VIDEO`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["大远景开场，低机位贴近海面起步，镜头向前缓缓推进并小幅上摇，视角慢慢抬升，快艇驶入画面中心，破浪匀速航行，海浪层层涌动，海天开阔，空间感强烈，镜头柔和移动，全程丝滑无断层。", "720p", "10", "16:9", 1321387`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
