# RH_RhartImageGTextToImage

## 节点类型

`RH_RhartImageGTextToImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `aspectRatio:COMBO`（1 次）
- `skip_error:BOOLEAN`（1 次）
- `seed:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["这些图和你给的描述，核心不是普通“通勤列车抓拍”，而是非常明确的几个要素叠加：\n\n- 拥挤地铁/通勤列车环境\n- 斜后方、略微仰拍的乘客视角\n- 单人女性主体，白色轻薄上衣 + 浅色包臀裙\n- 低马尾、碎发、通勤妆、精致五官\`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
