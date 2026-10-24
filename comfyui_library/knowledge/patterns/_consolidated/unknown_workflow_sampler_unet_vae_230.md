---
name: unknown_workflow_sampler_unet_vae_230
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.6595
common_nodes: [Any Switch (rgthree), CLIPLoader, ComfySwitchNode, EmptyLatentImage, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), Image Comparer (rgthree), ImageConcanate, ImageConcatMulti, ImageScaleToTotalPixels, KSampler, LoadImage, PathchSageAttentionKJ, PreviewAny, PrimitiveStringMultiline, QwenImage21Cache, ResolutionSelector, SaveImage, SaveImageAdvanced, Seed (rgthree), TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen image 2.1 多合一图像编辑 加速工作流 V1.5_2104920188973051905.json, 图片生成/图生图/Qwen image 2.1 多合一图像编辑 加速工作流_2102626139150831618.json, 图片生成/图生图/Qwen_image_2.1_多合一图像编辑_加速工作流_2108746804220219393.json, 图片生成/图生图/Qwen_image_2.1_多合一图像编辑_加速工作流_2110192979620225025.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_230

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1 多合一图像编辑 加速工作流 V1.5_2104920188973051905.json、图片生成/图生图/Qwen image 2.1 多合一图像编辑 加速工作流_2102626139150831618.json、图片生成/图生图/Qwen_image_2.1_多合一图像编辑_加速工作流_2108746804220219393.json、图片生成/图生图/Qwen_image_2.1_多合一图像编辑_加速工作流_2110192979620225025.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `Seed (rgthree)`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 3/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 40 | 40 - 40 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 40 - 40，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
