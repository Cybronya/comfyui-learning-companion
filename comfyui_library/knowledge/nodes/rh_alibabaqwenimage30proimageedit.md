# RH_AlibabaQwenImage30ProImageEdit

## 节点类型

`RH_AlibabaQwenImage30ProImageEdit`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 10 个 workflow 中。

## 输入

- `image1:IMAGE`（10 次）
- `image2:IMAGE`（10 次）
- `image3:IMAGE`（10 次）
- `api_config:RH_OPENAPI_CONFIG`（10 次）
- `prompt:STRING`（10 次）
- `negativePrompt:STRING`（1 次）
- `size:COMBO`（1 次）
- `imageNum:COMBO`（1 次）
- `promptExtend:BOOLEAN`（1 次）
- `seed:INT`（1 次）

## 输出

- `image:IMAGE`（10 次）
- `url:STRING`（10 次）
- `response:STRING`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "custom", "1", true, 0, "randomize", false, "direct", true]`（9 次）
- `["", "", "custom", "1", true, 1836063661, "randomize", false, "direct", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
