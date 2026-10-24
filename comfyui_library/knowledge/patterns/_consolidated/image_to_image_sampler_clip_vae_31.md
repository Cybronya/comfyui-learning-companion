---
name: image_to_image_sampler_clip_vae_31
type: Image To Image
frequency: 5
level: strong
coverage: 0.811
common_nodes: [Anything Everywhere3, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, NunchakuFluxDiTLoader, PreviewImage, RH_Translator, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Kontext 局部重绘，融图重绘，双图局部重绘（指定物品，加速）_1957337322624839682.json, 图片生成/图生图/Kontext局部重绘加速体（二合一版，可文字，可融图）_1961617656002580482.json, 图片生成/图生图/Kontext，一句话改图。_1970665673284329473.json, 图片生成/图生图/Kontext，一句话改图。_2073218617499537410.json, 图片生成/文生图/Kontext，一句话改图。_2070705333793804290.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_31

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext 局部重绘，融图重绘，双图局部重绘（指定物品，加速）_1957337322624839682.json、图片生成/图生图/Kontext局部重绘加速体（二合一版，可文字，可融图）_1961617656002580482.json、图片生成/图生图/Kontext，一句话改图。_1970665673284329473.json、图片生成/图生图/Kontext，一句话改图。_2073218617499537410.json、图片生成/文生图/Kontext，一句话改图。_2070705333793804290.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `PreviewImage`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Text` —— 3/5 个有
- `FluxKontextImageScale` —— 2/5 个有
- `GrowMaskWithBlur` —— 2/5 个有
- `Kontext Inpainting Conditioning` —— 2/5 个有
- `MaskPreview` —— 2/5 个有
- `easy imageRemBg` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Note _O` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | dpmpp_sde | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
