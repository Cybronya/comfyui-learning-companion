---
name: unknown_workflow_sampler_unet_vae_113
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.691333
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1：图像编辑_2101759280482447361.json, 图片生成/文生图/CGD_qwen-image-2.1-rh-t2i_2104813454950486018.json, 图片生成/文生图/QWen2.1文生图_2102420206202216450.json, 图片生成/文生图/Qwen Image 2.1：文生图_2101751274873122818.json, 图片生成/文生图/Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786.json, 图片生成/文生图/qwen_image_2_1_TI2I 二合一工作流（带提示词增强）_2102589892604813314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_113

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1：图像编辑_2101759280482447361.json、图片生成/文生图/CGD_qwen-image-2.1-rh-t2i_2104813454950486018.json、图片生成/文生图/QWen2.1文生图_2102420206202216450.json、图片生成/文生图/Qwen Image 2.1：文生图_2101751274873122818.json、图片生成/文生图/Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 5/6 个有
- `SaveImageAdvanced` —— 5/6 个有
- `LoadImage` —— 3/6 个有
- `JjkText` —— 2/6 个有
- `PrimitiveBoolean` —— 2/6 个有
- `SeedNode` —— 2/6 个有
- `StringConcatenate` —— 2/6 个有
- `BatchImagesNode` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ImageCompare` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `Textbox` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1536 | 6 | 80% |
| 采样步数 | 25 | 25 - 35 | 6 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，6 个样本
- 采样步数 中位数 25，观测区间 25 - 35，6 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
