# MOSSImageLayoutPrompt

## 节点类型

`MOSSImageLayoutPrompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `element:ARRAY`（3 次）
- `prompt:STRING`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `character_boxes:STRING`（3 次）

## 输出

- `prompt:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["moss_vgouache_style,小金毛从对面透过鱼缸玻璃，看鱼缸内的观赏小鱼。", 1024, 1024, ""]`（1 次）
- `["Goal: Create a photorealistic social-media promo image showing a young woman presenting a large GitHub repository page`（1 次）
- `["Anime illustration of a very cute girl with massive fennec fox ears, a big fluffy tail, long wavy blonde hair and brig`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
