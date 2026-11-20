---
name: unknown_workflow_video_sampler_clip_38
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.986462
common_nodes: [AudioCrop, AudioSeparation, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoadImage, ManualSigmas, MathExpression|pysssss, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy float, easy getNode, easy setNode]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3图片数字人_2041815038444441602.json, 图片生成/图生图/图+音频生唱歌：LTX 2.3_2069371802400419841.json, 数字人/数字人/LTX2.3图片数字人_2037856663717289985.json, 数字人/数字人/LTX2.3超强一致性数字人_2044379214362714113.json, 数字人/数字人/LTX2.3超强一致性数字人_2046938947288305665.json, 数字人/数字人/LTX2.3超强一致性数字人去字幕优化版v2_2046132644798275586.json, 数字人/数字人/图片数字人(LTX2.3)_2041738934023102466.json, 视频生成/图生视频/LTX2.3 数字人_2041853931457880066.json, 视频生成/图生视频/LTX2.3单图数字人_2064665242105372674.json, 视频生成/图生视频/LTX2.3图片数字人_2069015764195176450.json, 视频生成/图生视频/LTX2.3超强一致性数字人去字幕过渡超高质量lora但速度慢v2_2046558500209299457.json, 视频生成/图生视频/LTX2.3超强一致性数字人去字幕过渡超高质量lora但速度慢v2_2048669501297790977.json, 视频生成/图生视频/LTX2.3（kj版）首帧-数字人（动效好，速度快)_2079548676040646657.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_38

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/LTX2.3图片数字人_2041815038444441602.json、图片生成/图生图/图+音频生唱歌：LTX 2.3_2069371802400419841.json、数字人/数字人/LTX2.3图片数字人_2037856663717289985.json、数字人/数字人/LTX2.3超强一致性数字人_2044379214362714113.json、数字人/数字人/LTX2.3超强一致性数字人_2046938947288305665.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 13 个 workflow 都包含：
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
- `Audio Duration (mtb)` —— 12/13 个有
- `CR Float To Integer` —— 12/13 个有
- `DiffusionModelLoaderKJ` —— 12/13 个有
- `easy int` —— 12/13 个有
- `LTXVScheduler` —— 11/13 个有
- `LatentUpscaleModelLoader` —— 11/13 个有
- `LTXVChunkFeedForward` —— 8/13 个有
- `LTXVImgToVideoInplace` —— 8/13 个有
- `VRAMReserver` —— 7/13 个有
- `LoraLoaderModelOnly` —— 6/13 个有
- `easy showAnything` —— 6/13 个有
- `LTXVCropGuides` —— 5/13 个有
- `LTXVImgToVideoInplaceKJ` —— 5/13 个有
- `JWFloat` —— 3/13 个有
- `JWIntegerToString` —— 3/13 个有
- `1hew_AudioDuration` —— 1/13 个有
- `Bjornulf_FreeVRAM` —— 1/13 个有
- `CR Text` —— 1/13 个有
- `Fast Groups Muter (rgthree)` —— 1/13 个有
- `FlashVSRInitPipe` —— 1/13 个有
- `FlashVSRNodeAdv` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `MelBandRoFormerModelLoader` —— 1/13 个有
- `MelBandRoFormerSampler` —— 1/13 个有
- `SaveAudioMP3` —— 1/13 个有
- `TTResolutionSelector` —— 1/13 个有
- `UNETLoader` —— 1/13 个有
- `VHS_LoadVideo` —— 1/13 个有
- `easy anythingIndexSwitch` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
