---
name: image_to_image_sampler_clip_unet_208
type: Image To Image
frequency: 2
level: weak
coverage: 0.815
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, KSampler, LoadImage, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Z-Image快速洗图_2048561756397641730.json, 视频生成/图生视频/MOSS_Image_SFT洗图_2115313167839621121.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_208

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-Image快速洗图_2048561756397641730.json、视频生成/图生视频/MOSS_Image_SFT洗图_2115313167839621121.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 31 | - | 2 | 39% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 50% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 0.705 | - | 2 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 31，样本不足，未给区间，2 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 0.705，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
