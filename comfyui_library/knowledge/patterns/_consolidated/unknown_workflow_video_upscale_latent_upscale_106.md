---
name: unknown_workflow_video_upscale_latent_upscale_106
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.754333
common_nodes: [AudioCrop, Bjornulf_ShowFloat, Bjornulf_ShowInt, CFGGuider, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVReferenceAudio, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression_UTK, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PainterAudioLength, PreviewImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SeedGenerator, SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SimpleMath+, SolidMask, TTResolutionSelector, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2048028402485043202.json, 视频生成/图生视频/2046304725880016898.json, 音频生成/音频生成/LTX2.3 MV数字人（moss长音频加强面部一致性）_2049272954013360129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_106

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2048028402485043202.json、视频生成/图生视频/2046304725880016898.json、音频生成/音频生成/LTX2.3 MV数字人（moss长音频加强面部一致性）_2049272954013360129.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `Bjornulf_ShowFloat`
- `Bjornulf_ShowInt`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVReferenceAudio`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression_UTK`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PainterAudioLength`
- `PreviewImage`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SeedGenerator`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SimpleMath+`
- `SolidMask`
- `TTResolutionSelector`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `LTXVPreprocess` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `MossTTSModelLoader` —— 1/3 个有
- `MossTTSVoiceDesign` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
