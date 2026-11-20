# WujiImagePrompt2

## 节点类型

`WujiImagePrompt2`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `助力源:WUJI_LLM`（6 次）
- `reference_images.reference_image_0:IMAGE`（6 次）
- `prompt:STRING`（6 次）
- `constraints:STRING`（6 次）
- `meta_instruction:STRING`（6 次）
- `template_id:STRING`（6 次）
- `material:COMBO`（6 次）
- `output_format:COMBO`（6 次）
- `multi_line:BOOLEAN`（6 次）
- `seed:INT`（6 次）

## 输出

- `图像提示词:STRING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "", "miniature-world-six", "跟随模板", "自动选择", false, 1546314567, "randomize", false]`（1 次）
- `["", "", "", "miniature-world-six", "跟随模板", "自动选择", false, 1888903182, "randomize", false]`（1 次）
- `["", "", "", "portrait-fiveviews", "跟随模板", "自动选择", false, 713104602, "randomize", false]`（1 次）
- `["", "", "", "portrait-fiveviews", "跟随模板", "自动选择", false, 765229841, "randomize", false]`（1 次）
- `["", "", "", "portrait-single", "跟随模板", "自动选择", false, 2012100774, "randomize", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
