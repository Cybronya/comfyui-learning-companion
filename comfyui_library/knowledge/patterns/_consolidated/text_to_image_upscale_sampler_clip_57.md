---
name: text_to_image_upscale_sampler_clip_57
type: Text To Image
frequency: 2
level: weak
coverage: 0.816
common_nodes: [AdvancedLyingSigmaSampler, BasicGuider, BasicScheduler, CLIPTextEncode, CR Simple Image Compare, DepthAnythingV2Preprocessor, DualCLIPLoader, EmptyLatentImage, FluxGuidance, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LayerFilter: FilmV2, PreviewImage, RandomNoise, SamplerCustom, SamplerCustomAdvanced, SaveImage, Seed_, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [平台全量/Flux Sigma采样器细节提升 Flux Add Detail_1854955804221968385.json, 平台全量/Flux细节提升：Flux Add Detail & Realistic Skin_1868916738820816897.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_57

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Flux Sigma采样器细节提升 Flux Add Detail_1854955804221968385.json、平台全量/Flux细节提升：Flux Add Detail & Realistic Skin_1868916738820816897.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `AdvancedLyingSigmaSampler`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Simple Image Compare`
- `DepthAnythingV2Preprocessor`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LayerFilter: FilmV2`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustom`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed_`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `RH_Prompter` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
