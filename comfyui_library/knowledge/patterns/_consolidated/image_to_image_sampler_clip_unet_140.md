---
name: image_to_image_sampler_clip_unet_140
type: Image To Image
frequency: 4
level: weak
coverage: 0.9455
common_nodes: [AnimaLLLiteApply, CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Anima -动漫局部重绘_2061789555824615425.json, 图片生成/图生图/Anima-aesthetic-v1.1-局部重绘_2078101582297788417.json, 图片生成/图生图/Anima-动漫局部重绘+图像反推_2069046278197174274.json, 平台全量/Anima-aesthetic-v1.1-局部重绘_2078551615627423745.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_140

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Anima -动漫局部重绘_2061789555824615425.json、图片生成/图生图/Anima-aesthetic-v1.1-局部重绘_2078101582297788417.json、图片生成/图生图/Anima-动漫局部重绘+图像反推_2069046278197174274.json、平台全量/Anima-aesthetic-v1.1-局部重绘_2078551615627423745.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `AnimaLLLiteApply`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `ModelPatchLoader` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Mask Fill Holes` —— 2/4 个有
- `MaskFillHoles` —— 2/4 个有
- `ToriiGateT8_GroundingBuilder` —— 1/4 个有
- `ToriiGateT8_LlamaCppVisionGenerate` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 40 | 4 | 13% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 4 | 19% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 40，4 个样本，取值分散，一致性仅 13%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
