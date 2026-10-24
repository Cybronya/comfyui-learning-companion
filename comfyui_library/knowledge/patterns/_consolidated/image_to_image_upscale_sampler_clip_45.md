---
name: image_to_image_upscale_sampler_clip_45
type: Image To Image
frequency: 2
level: weak
coverage: 0.855
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), ImageScaleBy, KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/洗图+放大_2066770140041142273.json, 图片生成/文生图/Krea2图生花型_2112443963813752833.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/洗图+放大_2066770140041142273.json、图片生成/文生图/Krea2图生花型_2112443963813752833.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `ImageSharpen` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1.5 | - | 2 | 67% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.175 | - | 2 | 57% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1.5，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.175，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
