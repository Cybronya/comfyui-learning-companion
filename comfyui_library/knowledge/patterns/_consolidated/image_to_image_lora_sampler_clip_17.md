---
name: image_to_image_lora_sampler_clip_17
type: Image To Image
frequency: 2
level: weak
coverage: 0.829
common_nodes: [BetterFilmGrain, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, CR Simple Image Compare, DualCLIPLoader, EsesImageEffectBloom, FluxGuidance, GetImageSizeAndCount, Image Comparer (rgthree), ImageScaleDownToSize, ImageSharpen, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, RH_Captioner, SaveImage, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: [CR Simple Image Compare, LayerUtility: PurgeVRAM V2, Text Concatenate, Text Multiline, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1945516410565218305.json, 视频生成/图生视频/1945516410565218305.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1945516410565218305.json、视频生成/图生视频/1945516410565218305.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BetterFilmGrain`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `CR Simple Image Compare`
- `DualCLIPLoader`
- `EsesImageEffectBloom`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `Image Comparer (rgthree)`
- `ImageScaleDownToSize`
- `ImageSharpen`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.2 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Simple Image Compare、LayerUtility: PurgeVRAM V2、Text Concatenate、Text Multiline、CR SDXL Aspect Ratio
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
