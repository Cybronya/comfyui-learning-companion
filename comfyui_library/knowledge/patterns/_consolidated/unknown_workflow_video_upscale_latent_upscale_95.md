---
name: unknown_workflow_video_upscale_latent_upscale_95
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.57825
common_nodes: [AudioCrop, CFGGuider, CLIPTextEncode, ComfySwitchNode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, ImageScaleBy, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, ManualSigmas, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewAudio, PreviewImage, PrimitiveFloat, RHHiddenNodes, RandomNoise, SamplerCustomAdvanced, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SimpleMath+, SolidMask, TrimAudioDuration, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3低显存提速版—超强高质量画音同步+图生视频+MV数字人_2034220843508703234.json, 视频生成/图生视频/迄今超强高质量画音同步LTX2.3-KJ版低显存提速版图生视频支持竖屏MV数字人制作工作流_1897892598386741250.json, 视频生成/图生视频/迄今超强高质量画音同步LTX2.3低显存提速版图生视频上传多分镜图制作万物数字人（无限时长）可超长MV制作循环工作流_1959793923826855938.json, 视频生成/文生视频/迄今超强高质量画音同步LTX2.3 KJ版低显存提速版文+音频生MV视频分镜支持横竖屏自定义分镜时间_1955807480933597185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_95

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX2.3低显存提速版—超强高质量画音同步+图生视频+MV数字人_2034220843508703234.json、视频生成/图生视频/迄今超强高质量画音同步LTX2.3-KJ版低显存提速版图生视频支持竖屏MV数字人制作工作流_1897892598386741250.json、视频生成/图生视频/迄今超强高质量画音同步LTX2.3低显存提速版图生视频上传多分镜图制作万物数字人（无限时长）可超长MV制作循环工作流_1959793923826855938.json、视频生成/文生视频/迄今超强高质量画音同步LTX2.3 KJ版低显存提速版文+音频生MV视频分镜支持横竖屏自定义分镜时间_1955807480933597185.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioCrop`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `ManualSigmas`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `PreviewImage`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SimpleMath+`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AudioEvenSplitNode` —— 1/4 个有
- `AudioSelectNode` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `ImageStringBatch` —— 1/4 个有
- `ImpactMinMax` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `LTXAVTextEncoderLoader` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `LoadDiffusionModelShared //Inspire` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `Qwen3_VQA_Plus` —— 1/4 个有
- `SelectImageString` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `SoundFlow_GetLength` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有
- `easy convertAnything` —— 1/4 个有
- `easy forLoopEnd` —— 1/4 个有
- `easy forLoopStart` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
