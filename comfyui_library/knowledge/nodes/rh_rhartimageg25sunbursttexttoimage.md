# RH_RhartImageG25SunburstTextToImage

## 节点类型

`RH_RhartImageG25SunburstTextToImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（3 次）
- `prompt:STRING`（3 次）
- `aspectRatio:COMBO`（3 次）
- `resolution:COMBO`（3 次）
- `skip_error:BOOLEAN`（3 次）
- `seed:INT`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `url:STRING`（3 次）
- `response:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "16:9", "4k", false, 800143356, "randomize"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
