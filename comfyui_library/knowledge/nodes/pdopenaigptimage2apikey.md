# PDOpenAIGPTImage2APIKey

## 节点类型

`PDOpenAIGPTImage2APIKey`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `files:GEMINI_INPUT_FILES`（1 次）
- `api_key:STRING`（1 次）
- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `seed:INT`（1 次）
- `quality:COMBO`（1 次）
- `background:COMBO`（1 次）
- `size:COMBO`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `info:STRING`（1 次）
- `price:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "帮我把图1 的ip形象生成一个街头背景和排版，参考图2，并且去图2的机器人，增加一些版式如 pandy style 图2 的风格", "gpt-image-2", 362313094, "randomize", "auto", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
