---
name: unknown_workflow_video_inpaint_upscale_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6485
common_nodes: [CR Text, GetNode, GrowMaskWithBlur, ImageConcanate, ImageScaleToMegapixels, ImpactInt, InpaintPreprocessor, Int, LayerUtility: GeminiV2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, PrimitiveInt, SeedVR2, SeedVR2BlockSwap, SetNode, SimpleMath+, Text Concatenate, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/视频换装 V1.0_2011797155371032577.json, 平台全量/视频稳定换脸 Wan2_2 Fun VACE Video Face Swap V1_1992494088291241985.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_upscale_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频换装 V1.0_2011797155371032577.json、平台全量/视频稳定换脸 Wan2_2 Fun VACE Video Face Swap V1_1992494088291241985.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageScaleToMegapixels`
- `ImpactInt`
- `InpaintPreprocessor`
- `Int`
- `LayerUtility: GeminiV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `PrimitiveInt`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SetNode`
- `SimpleMath+`
- `Text Concatenate`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AutoCropFaces` —— 1/2 个有
- `LayerMask: HumanPartsUltra` —— 1/2 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/2 个有
- `WanVideoUni3C_embeds` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
