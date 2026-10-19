---
name: unknown_workflow_video_inpaint_upscale_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.792
common_nodes: [AIO_Preprocessor, AddLabel, Bjornulf_ShowJson, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, GetImageSizeAndCount, GetNode, Image Blank, ImageConcanate, ImageConcatMulti, ImageCrop+, ImageResizeKJ, ImageToMask, ImageUpscaleWithModel, ImpactInt, InpaintModelConditioning, KSampler, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, MaskToImage, PreviewImage, Primitive integer [Crystools], RHHiddenNodes, RH_Captioner, RH_Translator, SetNode, ShowText|pysssss, StyleModelApply, StyleModelLoader, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy cleanGpuUsed, easy imageSize]
problems: []
missing: []
members: [视频生成/图生视频/1925145300569104386.json, 视频生成/图生视频/1925039804986421249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_upscale_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1925145300569104386.json、视频生成/图生视频/1925039804986421249.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddLabel`
- `Bjornulf_ShowJson`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `GetNode`
- `Image Blank`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageCrop+`
- `ImageResizeKJ`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `RH_Captioner`
- `RH_Translator`
- `SetNode`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
