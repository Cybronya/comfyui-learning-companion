# GPTImage2PromptSelector

## 节点类型

`GPTImage2PromptSelector`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `category:COMBO`（4 次）
- `prompt_selection:COMBO`（4 次）
- `edit_prompt:STRING`（4 次）

## 输出

- `prompt:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["all", "[preset_62] [comparison] Vertical Artistic Portrait of a Young Eastern Woman (@zhiyangzhu22222)", "9:16 竖向构图，单人`（2 次）
- `["poster", "[preset_154] [poster] New Chinese Ink Landscape Poster (@liyue_ai)", "克苏鲁风格新中式水墨山水海报，竖版9:16构图，东方极简美学风格，大面积留白`（1 次）
- `["poster", "[preset_198] [poster] Peacock Botanical Vintage Symmetrical Art Print (@dotey)", "克苏鲁风格的孔雀，有触手，symmetrical d`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
