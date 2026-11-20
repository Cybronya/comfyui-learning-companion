---
name: image_to_image_sampler_clip_unet_187
type: Image To Image
frequency: 3
level: strong
coverage: 0.952333
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/电商商品图换背景V3.0_1963966014377574402.json, 平台全量/Flux-Kontext三图编辑-快速出图_1940593533873008642.json, 平台全量/Flux-Kontext单图双图-快速出图_1940588312438665217.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_187

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/电商商品图换背景V3.0_1963966014377574402.json、平台全量/Flux-Kontext三图编辑-快速出图_1940593533873008642.json、平台全量/Flux-Kontext单图双图-快速出图_1940588312438665217.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `InvertMask` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
