# RH_YouchuanTextToImageV6

## 节点类型

`RH_YouchuanTextToImageV6`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `cref:IMAGE`（1 次）
- `sref:IMAGE`（1 次）
- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `chaos:INT`（1 次）
- `quality:COMBO`（1 次）
- `stylize:INT`（1 次）
- `weird:INT`（1 次）
- `raw:BOOLEAN`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["海面和天空，乌云密布，平视视角，远处悠天上洒下来的光束", 0, "1", 0, 0, false, 1, 100, 100, 4, 100, false, "9:16", false, 374220802, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
