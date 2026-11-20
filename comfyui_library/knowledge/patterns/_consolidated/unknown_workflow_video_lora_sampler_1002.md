---
name: unknown_workflow_video_lora_sampler_1002
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8525
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSize, GrowMaskWithBlur, ImageCompositeMasked, ImageConcanate, ImageFromBatch+, ImpactInt, InspyrenetRembg, KSamplerAdvanced, LayerMask: SAM2VideoUltra, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelSamplingSD3, PathchSageAttentionKJ, RH_Captioner, RebatchImages, SimpleMath+, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVaceToVideo, easy showAnything]
problems: []
missing: []
members: [平台全量/🤡视频主体替换wan2_2 VACE【猴子炒菜 奥特曼跳舞等】🤡_1959802114639867905.json, 视频生成/图生视频/主体替换视频_1960314251325992961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1002

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/🤡视频主体替换wan2_2 VACE【猴子炒菜 奥特曼跳舞等】🤡_1959802114639867905.json、视频生成/图生视频/主体替换视频_1960314251325992961.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSize`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageFromBatch+`
- `ImpactInt`
- `InspyrenetRembg`
- `KSamplerAdvanced`
- `LayerMask: SAM2VideoUltra`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_Captioner`
- `RebatchImages`
- `SimpleMath+`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `JWImageResizeByLongerSide` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `MaskPreview` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PDIMAGE_LongerSize` —— 1/2 个有
- `Pick From Batch (mtb)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `Textbox` —— 1/2 个有
- `easy promptConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | lcm | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
