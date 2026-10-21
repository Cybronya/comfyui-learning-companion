# RH_AlibabaQwenImage20ProTextToImage

## 节点类型

`RH_AlibabaQwenImage20ProTextToImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `negativePrompt:STRING`（2 次）
- `size:COMBO`（2 次）
- `imageNum:COMBO`（2 次）
- `promptExtend:BOOLEAN`（2 次）
- `skip_error:BOOLEAN`（2 次）
- `seed:INT`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["【在此输入图片提示词】", "", "1024*1024", "1", true, false, 794249277519893, "randomize"]`（1 次）
- `["", "", "1024*1024", "1", true, false, 391567488066647, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
