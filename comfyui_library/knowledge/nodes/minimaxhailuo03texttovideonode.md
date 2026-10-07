# MinimaxHailuo03TextToVideoNode

## 节点类型

`MinimaxHailuo03TextToVideoNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model.prompt:STRING`（2 次）

## 输出

- `VIDEO:VIDEO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["MiniMax H3 Max", "", "768P", "16:9", 5, "balanced", 2967573614, "randomize", false]`（1 次）
- `["MiniMax H3 Max Turbo", "integrated_multimodal_description: [Shot 1] Cinematic, low-angle wide shot with a fast Push In`（1 次）
- `["MiniMax H3", "Single continuous shot, 5 seconds, one take, no cuts. Cinematic oner, third-person chase camera, steadic`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
