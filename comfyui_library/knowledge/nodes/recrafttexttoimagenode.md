# RecraftTextToImageNode

## 节点类型

`RecraftTextToImageNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `recraft_style:RECRAFT_V3_STYLE`（4 次）
- `negative_prompt:STRING`（4 次）
- `recraft_controls:RECRAFT_CONTROLS`（4 次）
- `prompt:STRING`（1 次）

## 输出

- `IMAGE:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A young boy performing a dynamic skateboard trick in a sunlit skate park. He's wearing a white t-shirt and green short`（1 次）
- `["A young boy performing a dynamic skateboard trick in a sunlit skate park. He's wearing a white t-shirt and green short`（1 次）
- `["A soft-focus, painterly vintage photograph of David's marble bust, surrounded by an abundant, lush tapestry of antique`（1 次）
- `["extreme wide shot of an grand colosseum, dynamic angled composition", "1024x1024", 1, 0, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
