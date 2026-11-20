# SDXLPromptStylerAll

## 节点类型

`SDXLPromptStylerAll`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `text_positive:STRING`（2 次）

## 输出

- `positive_prompt_text_g:STRING`（4 次）
- `negative_prompt_text_g:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["high resolution, master piece, realistic", "oil painting, 3d, anime, bad image, low resolution", "none byArtists", "No`（1 次）
- `["", "", "none byArtists", "No", false, false]`（1 次）
- `["comic cover art, poster art, psychedelic art , pop surrealism", "(worst quality, low quality, thumbnail:1.4), signatur`（1 次）
- `["SDXLPromptStyler", "", "Abraham Pether", "No", false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
