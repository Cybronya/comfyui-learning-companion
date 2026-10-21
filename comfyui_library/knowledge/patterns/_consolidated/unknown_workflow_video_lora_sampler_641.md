---
name: unknown_workflow_video_lora_sampler_641
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.861
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSize, GrowMaskWithBlur, ImageCompositeMasked, ImageConcanate, ImageFromBatch+, InspyrenetRembg, KSamplerAdvanced, LayerMask: SAM2VideoUltra, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelSamplingSD3, PDIMAGE_LongerSize, PathchSageAttentionKJ, PreviewImage, RH_Captioner, RebatchImages, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVaceToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1957475437662367746.json, 视频生成/图生视频/1958077284689334273.json, 视频生成/图生视频/1960314251325992961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_641

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1957475437662367746.json、视频生成/图生视频/1958077284689334273.json、视频生成/图生视频/1960314251325992961.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSize`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageFromBatch+`
- `InspyrenetRembg`
- `KSamplerAdvanced`
- `LayerMask: SAM2VideoUltra`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingSD3`
- `PDIMAGE_LongerSize`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RH_Captioner`
- `RebatchImages`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `ImageMirror` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `InvertMask` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `LayerMask: LoadFlorence2Model` —— 2/3 个有
- `LayerMask: ObjectDetectorFL2` —— 2/3 个有
- `ShowText` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `easy promptConcat` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `MaskPreview` —— 1/3 个有
- `Pick From Batch (mtb)` —— 1/3 个有
- `Textbox` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | lcm | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
