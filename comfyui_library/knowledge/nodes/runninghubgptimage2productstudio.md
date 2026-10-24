# RunningHubGptImage2ProductStudio

## 节点类型

`RunningHubGptImage2ProductStudio`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（6 次）
- `reference_image:IMAGE`（6 次）
- `mask:MASK`（6 次）
- `llm_config:SYNVOW_LLM_CONFIG`（6 次）
- `mode:COMBO`（6 次）
- `model_type:COMBO`（6 次）
- `quality:COMBO`（6 次）
- `resolution:COMBO`（6 次）
- `aspect_ratio:COMBO`（6 次）
- `seed:INT`（6 次）

## 输出

- `images:IMAGE`（6 次）
- `final_prompt:STRING`（6 次）
- `status:STRING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["模糊图片高清", "gpt-image-2-低价通道", "auto", "1K", "auto", 999, "fixed", "关闭", "", ""]`（1 次）
- `["产品融入场景", "gpt-image-2-低价通道", "auto", "1K", "auto", 1751212327, "randomize", "关闭", "", ""]`（1 次）
- `["移除物品", "gpt-image-2-低价通道", "auto", "1K", "auto", 999, "fixed", "关闭", "", ""]`（1 次）
- `["增加光效", "gpt-image-2-低价通道", "auto", "1K", "auto", 999, "fixed", "关闭", "", ""]`（1 次）
- `["扩图", "gpt-image-2-低价通道", "auto", "1K", "auto", 999, "fixed", "关闭", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
