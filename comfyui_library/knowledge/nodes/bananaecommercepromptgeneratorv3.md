# BananaEcommercePromptGeneratorV3

## 节点类型

`BananaEcommercePromptGeneratorV3`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `llm_config:SYNVOW_LLM_CONFIG`（1 次）
- `product_image_1:IMAGE`（1 次）
- `product_image_2:IMAGE`（1 次）
- `product_image_3:IMAGE`（1 次）
- `product_image_4:IMAGE`（1 次）
- `product_image_5:IMAGE`（1 次）
- `product_image_6:IMAGE`（1 次）
- `product_image_7:IMAGE`（1 次）
- `product_image_8:IMAGE`（1 次）
- `ref_image_1:IMAGE`（1 次）

## 输出

- `prompts_list:STRING`（1 次）
- `prompts_count:INT`（1 次）
- `debug_info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["google/gemini-3.5-flash", "女裙", "睡衣", "简约 Ins 风", "生活方式使用场景（人物/手部交互）", "自动检测 (Auto)", 382858387, "fixed", 12]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
