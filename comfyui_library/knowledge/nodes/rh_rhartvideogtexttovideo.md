# RH_RhartVideoGTextToVideo

## 节点类型

`RH_RhartVideoGTextToVideo`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `aspectRatio:COMBO`（1 次）
- `resolution:COMBO`（1 次）
- `duration:INT`（1 次）
- `skip_error:BOOLEAN`（1 次）
- `seed:INT`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一只可爱蓬松黑猫，明亮的浅绿色大眼睛、长毛、尖耳朵，站在柔和的蓝色纯色背景前。全身镜头，黑猫随着轻快、有节奏感的流行舞曲跳舞：先左右轻轻踏步，前爪交替摆动，然后扭动身体、甩甩蓬松的尾巴，做一个可爱的转圈，最后面向镜头举起两只前爪，定格成`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
