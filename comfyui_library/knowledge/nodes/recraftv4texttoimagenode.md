# RecraftV4TextToImageNode

## 节点类型

`RecraftV4TextToImageNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `recraft_controls:RECRAFT_CONTROLS`（4 次）
- `style_references.style_reference0:IMAGE`（2 次）
- `style_id:STRING`（1 次）

## 输出

- `IMAGE:IMAGE`（4 次）
- `style_id:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Extreme low-angle shot of a female athlete stretching under an overpass, emphasizing a prominent light-colored running`（1 次）
- `["portrait of a young man with a short buzzed platinum blonde fade haircut, silver mirrored wraparound futuristic sport `（1 次）
- `["A dramatic silhouette portrait of an elegant neck in profile against a luminous, deep midnight-purple background. The `（1 次）
- `["Full-length stunning model in long black dress, with thin belt, black hat and boots high fashion, face is bowed down, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
