# RelayLLMText

## 节点类型

`RelayLLMText`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `image4:IMAGE`（1 次）
- `image5:IMAGE`（1 次）
- `image6:IMAGE`（1 次）
- `image7:IMAGE`（1 次）
- `image8:IMAGE`（1 次）
- `video:VIDEO`（1 次）
- `audio:AUDIO`（1 次）

## 输出

- `text:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["text", "GeminiText", "v1beta/models", "https://api.llaiapi.host", "gemini-3-flash-preview", "", "形容一下这张图女人头部状态", "", 4`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
