---
name: unknown_workflow_sampler_unet_vae_141
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.888286
common_nodes: [CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux3-Klein-图像编辑_2111109110757412866.json, 图片生成/图生图/FusionX 稳定修手_1947821442744336385.json, 图片生成/图生图/Klein-9b-人像皮肤精修_2060713950316154882.json, 图片生成/图生图/Moss-image-局部重绘_2112544404337676289.json, 图片生成/图生图/Qwen-image2.1-万能局部重绘_2108164582689824769.json, 图片生成/图生图/Qwen-image2.1-万能局部重绘_2110648449984196609.json, 图片生成/图生图/Qwen-image2.1-万能局部重绘_2111278068961730562.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_141

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux3-Klein-图像编辑_2111109110757412866.json、图片生成/图生图/FusionX 稳定修手_1947821442744336385.json、图片生成/图生图/Klein-9b-人像皮肤精修_2060713950316154882.json、图片生成/图生图/Moss-image-局部重绘_2112544404337676289.json、图片生成/图生图/Qwen-image2.1-万能局部重绘_2108164582689824769.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `InpaintModelConditioning` —— 5/7 个有
- `Mask Fill Holes` —— 4/7 个有
- `CLIPTextEncode` —— 3/7 个有
- `TextEncodeQwenImage21` —— 3/7 个有
- `Int` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `PainterFluxImageEdit` —— 1/7 个有
- `ReferenceMultiLatent` —— 1/7 个有
- `YC Color Match` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 50 | 7 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 57% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 0.25 - 1 | 7 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 50，7 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，7 个样本
