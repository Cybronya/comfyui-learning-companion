---
name: unknown_workflow_sampler_unet_vae_267
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.442
common_nodes: [Any Switch (rgthree), CLIPLoader, DapaoImagePadDirectionNode, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, PreviewImage, PrimitiveFloat, RHHiddenNodes, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2511完美扩图｜百分比可控扩图，精准延展画面_2104456136303931394.json, 图片生成/图生图/Qwen 2511扩图_2112104727579283457.json, 图片生成/图生图/Qwen-Image-2.1 按百分比可控扩图，精准延展画布，一键放大画布。_2104128616580866050.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_267

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen 2511完美扩图｜百分比可控扩图，精准延展画面_2104456136303931394.json、图片生成/图生图/Qwen 2511扩图_2112104727579283457.json、图片生成/图生图/Qwen-Image-2.1 按百分比可控扩图，精准延展画布，一键放大画布。_2104128616580866050.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `DapaoImagePadDirectionNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `QwenImage21Cache` —— 1/3 个有
- `TextEncodeQwenImage21` —— 1/3 个有
- `TextGenerateLTX2Prompt` —— 1/3 个有
- `easy imageSizeByLongerSide` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 3 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，3 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
