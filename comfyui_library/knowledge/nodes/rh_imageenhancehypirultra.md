# RH_ImageEnhanceHypirUltra

## 节点类型

`RH_ImageEnhanceHypirUltra`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `shortEdgeSize:INT`（1 次）
- `longEdgeSize:INT`（1 次）
- `textureLevel:COMBO`（1 次）
- `creativityLevel:COMBO`（1 次）
- `upscale:INT`（1 次）
- `seed:INT`（1 次）
- `skip_error:BOOLEAN`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["restore natural skin texture, realistic pores, keep identity", -1, -1, 5, 0, 2, 1528, "randomize", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
