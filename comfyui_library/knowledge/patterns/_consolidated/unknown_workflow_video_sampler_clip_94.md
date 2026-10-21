---
name: unknown_workflow_video_sampler_clip_94
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9805
common_nodes: [AudioCrop, AudioSeparation, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoadImage, ManualSigmas, MathExpression|pysssss, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy float, easy getNode, easy setNode]
problems: []
missing: []
members: [视频生成/图生视频/2041853931457880066.json, 视频生成/图生视频/2064665242105372674.json, 视频生成/图生视频/2069015764195176450.json, 视频生成/图生视频/2046558500209299457.json, 视频生成/图生视频/2048669501297790977.json, 视频生成/图生视频/2079548676040646657.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_94

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2041853931457880066.json、视频生成/图生视频/2064665242105372674.json、视频生成/图生视频/2069015764195176450.json、视频生成/图生视频/2046558500209299457.json、视频生成/图生视频/2048669501297790977.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `ManualSigmas`
- `MathExpression|pysssss`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy float`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 5/6 个有
- `CR Float To Integer` —— 5/6 个有
- `DiffusionModelLoaderKJ` —— 5/6 个有
- `easy int` —— 5/6 个有
- `LTXVChunkFeedForward` —— 4/6 个有
- `LTXVImgToVideoInplace` —— 4/6 个有
- `LTXVScheduler` —— 4/6 个有
- `LatentUpscaleModelLoader` —— 4/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `VRAMReserver` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `JWFloat` —— 2/6 个有
- `JWIntegerToString` —— 2/6 个有
- `LTXVCropGuides` —— 2/6 个有
- `LTXVImgToVideoInplaceKJ` —— 2/6 个有
- `1hew_AudioDuration` —— 1/6 个有
- `Bjornulf_FreeVRAM` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `FlashVSRInitPipe` —— 1/6 个有
- `FlashVSRNodeAdv` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `MelBandRoFormerModelLoader` —— 1/6 个有
- `MelBandRoFormerSampler` —— 1/6 个有
- `SaveAudioMP3` —— 1/6 个有
- `TTResolutionSelector` —— 1/6 个有
- `UNETLoader` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `easy anythingIndexSwitch` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
