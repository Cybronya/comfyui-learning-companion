---
name: image_to_image_sampler_clip_unet_109
type: Image To Image
frequency: 4
level: strong
coverage: 0.93325
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, RH_Translator, ReferenceLatent, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/23种风格图片转绘神器(KontextDEV）_1941686269858705409.json, 图片生成/图生图/Change painting into a real photo_1942229372625686530.json, 图片生成/图生图/Flux Kontext Dev一句话编辑图像（单图）+放大_1938864631316144129.json, 图片生成/图生图/flux_dev-fp8_1938610130756030465.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_109

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/23种风格图片转绘神器(KontextDEV）_1941686269858705409.json、图片生成/图生图/Change painting into a real photo_1942229372625686530.json、图片生成/图生图/Flux Kontext Dev一句话编辑图像（单图）+放大_1938864631316144129.json、图片生成/图生图/flux_dev-fp8_1938610130756030465.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 3/4 个有
- `ImageResize` —— 2/4 个有
- `Compare` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImpactStringSelector` —— 1/4 个有
- `PMRF` —— 1/4 个有
- `Primitive integer [Crystools]` —— 1/4 个有
- `RandomInt` —— 1/4 个有
- `String Replace (mtb)` —— 1/4 个有
- `easy ifElse` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
