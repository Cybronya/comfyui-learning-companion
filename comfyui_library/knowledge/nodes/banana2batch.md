# Banana2Batch

## 节点类型

`Banana2Batch`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_1.1:IMAGE`（1 次）
- `image_1.2:IMAGE`（1 次）
- `image_1.3:IMAGE`（1 次）
- `image_1.4:IMAGE`（1 次）
- `prompt_1:STRING`（1 次）
- `image_2.1:IMAGE`（1 次）
- `image_2.2:IMAGE`（1 次）
- `image_2.3:IMAGE`（1 次）
- `image_2.4:IMAGE`（1 次）
- `prompt_2:STRING`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `urls:STRING`（1 次）
- `responses:STRING`（1 次）
- `group1_image:IMAGE`（1 次）
- `group1_url:STRING`（1 次）
- `group1_response:INT`（1 次）
- `group1_info:STRING`（1 次）
- `group2_image:IMAGE`（1 次）
- `group2_url:STRING`（1 次）
- `group2_response:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["comfly", "https://ai.comfly.chat", "", "nano-banana-2", "Img2Img", "auto", "url", "2K", 1, 704987747574982, "randomize`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
