# RH_HiggsfieldSoulImageToImage

## 节点类型

`RH_HiggsfieldSoulImageToImage`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `api_config:RH_OPENAPI_CONFIG`（3 次）
- `prompt:STRING`（3 次）
- `size:COMBO`（2 次）
- `quality:COMBO`（2 次）
- `style:COMBO`（2 次）
- `strength:FLOAT`（2 次）
- `skip_error:BOOLEAN`（2 次）
- `seed:INT`（2 次）

## 输出

- `image:IMAGE`（3 次）
- `url:STRING`（3 次）
- `response:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "1152*2048", "high", "Realistic", 1, false, 0, "randomize"]`（1 次）
- `["", "1152*2048", "high", "Realistic", 1, false, 1491163130, "randomize"]`（1 次）
- `["", "1152*2048", "high", "Realistic", 1, false, 1214166411, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
