---
name: image_to_image_sampler_clip_unet_166
type: Image To Image
frequency: 2
level: weak
coverage: 0.8075
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Z-Image快速洗图_2048561756397641730.json, 图片生成/图生图/干问3反推洗图_1999295995408154626.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_166

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-Image快速洗图_2048561756397641730.json、图片生成/图生图/干问3反推洗图_1999295995408154626.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 11 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 0.875 | - | 2 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 0.875，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
