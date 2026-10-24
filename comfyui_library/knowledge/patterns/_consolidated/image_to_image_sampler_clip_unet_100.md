---
name: image_to_image_sampler_clip_unet_100
type: Image To Image
frequency: 5
level: strong
coverage: 0.9012
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux kontext 局部重绘（ inpainting）_1962171826392776705.json, 图片生成/图生图/flux-kontext-画面精准控制_1945126183988285441.json, 图片生成/图生图/【遇见AI】flux-kontext 单图编辑工作流_2050856923859308546.json, 图片生成/图生图/一致性dev版本_1945764160510554113.json, 图片生成/图生图/万物8K高清放大增强版-无痕去水印logo_1979887403118792705.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_100

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/flux kontext 局部重绘（ inpainting）_1962171826392776705.json、图片生成/图生图/flux-kontext-画面精准控制_1945126183988285441.json、图片生成/图生图/【遇见AI】flux-kontext 单图编辑工作流_2050856923859308546.json、图片生成/图生图/一致性dev版本_1945764160510554113.json、图片生成/图生图/万物8K高清放大增强版-无痕去水印logo_1979887403118792705.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `DifferentialDiffusion` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImpactImageBatchToImageList` —— 1/5 个有
- `Kontext Inpainting Conditioning` —— 1/5 个有
- `LayerStyle: ColorOverlay` —— 1/5 个有
- `MaskBlur+` —— 1/5 个有
- `UltimateSDUpscale` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
