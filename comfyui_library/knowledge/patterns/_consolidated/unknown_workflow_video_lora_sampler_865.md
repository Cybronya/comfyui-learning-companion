---
name: unknown_workflow_video_lora_sampler_865
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7625
common_nodes: [Anything Everywhere, Audio Duration (mtb), Audio Remixer, AudioCombine, AudioCrop, AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CR Text, ColorCorrectOfUtils, GetNode, ImageCASharpening+, ImageResize+, ImpactSwitch, Int, LayerUtility: PurgeVRAM V2, Load Audio Separation Model, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PreviewAudio, PreviewImage, RH_Translator, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddS2VEmbeds, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/【歌曲翻唱】Wan2.2图生视频-S2V数字人骨骼控制_1962038882978172929.json, 视频生成/图生视频/视频-【S2V数字人】Wan2.2图生视频-语音克隆_1978783026970824706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_865

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/【歌曲翻唱】Wan2.2图生视频-S2V数字人骨骼控制_1962038882978172929.json、视频生成/图生视频/视频-【S2V数字人】Wan2.2图生视频-语音克隆_1978783026970824706.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Audio Duration (mtb)`
- `Audio Remixer`
- `AudioCombine`
- `AudioCrop`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CR Text`
- `ColorCorrectOfUtils`
- `GetNode`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactSwitch`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `Load Audio Separation Model`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PreviewAudio`
- `PreviewImage`
- `RH_Translator`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddS2VEmbeds`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `IndexTTSRun` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `SeedVCRun` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `WanVideoTextEncodeCached` —— 1/2 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
