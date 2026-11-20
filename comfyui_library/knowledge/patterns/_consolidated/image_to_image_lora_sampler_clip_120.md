---
name: image_to_image_lora_sampler_clip_120
type: Image To Image
frequency: 2
level: weak
coverage: 0.885
common_nodes: [BetterFilmGrain, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, CR Simple Image Compare, DualCLIPLoader, EsesImageEffectBloom, FluxGuidance, GetImageSizeAndCount, Image Comparer (rgthree), ImageScaleDownToSize, ImageSharpen, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, RH_Captioner, SaveImage, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/Flux反推图+wan2.1更真实和洗图_细节增强_1946819522431971329.json, 图片生成/文生图/Flux+wan2.1更真实修复和洗图_细节增强_1945516410565218305.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_120

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/Flux反推图+wan2.1更真实和洗图_细节增强_1946819522431971329.json、图片生成/文生图/Flux+wan2.1更真实修复和洗图_细节增强_1945516410565218305.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

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

**可变部分**（部分 workflow 才有）：
- `LayerFilter: FilmV2` —— 1/2 个有

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
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
