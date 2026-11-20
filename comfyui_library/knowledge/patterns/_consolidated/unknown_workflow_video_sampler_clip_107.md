---
name: unknown_workflow_video_sampler_clip_107
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.764
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoadImage, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, TrimAudioDuration, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [数字人/数字人/LTX--数字人（改了小豹老师原流的clip及采样参数）效果很好_2010141378457636865.json, 数字人/数字人/【Supermate 】 LTX--高清数字人_2010182339548160001.json, 视频生成/图生视频/LTX2 KJ 加速_2012440624145899522.json, 视频生成/图生视频/LTX2+对口型_2021873842758619137.json, 视频生成/图生视频/LTX2.0数字人 自适应音频 效果还可以_2010630264770269185.json, 视频生成/图生视频/LTX2.3+参考图片+参考音频（对口型+多人对话）_2034521088973082625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_107

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/LTX--数字人（改了小豹老师原流的clip及采样参数）效果很好_2010141378457636865.json、数字人/数字人/【Supermate 】 LTX--高清数字人_2010182339548160001.json、视频生成/图生视频/LTX2 KJ 加速_2012440624145899522.json、视频生成/图生视频/LTX2+对口型_2021873842758619137.json、视频生成/图生视频/LTX2.0数字人 自适应音频 效果还可以_2010630264770269185.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 5/6 个有
- `ImageScaleBy` —— 5/6 个有
- `LTXVLatentUpsampler` —— 5/6 个有
- `LatentUpscaleModelLoader` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `INTConstant` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `SimpleMath+` —— 4/6 个有
- `MelBandRoFormerModelLoader` —— 3/6 个有
- `MelBandRoFormerSampler` —— 3/6 个有
- `PreviewAudio` —— 3/6 个有
- `Float` —— 2/6 个有
- `ImageUpscaleWithModel` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `Note Plus (mtb)` —— 2/6 个有
- `UpscaleModelLoader` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `easy showTensorShape` —— 2/6 个有
- `AudioSeparation` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `Int` —— 1/6 个有
- `LTXVGemmaCLIPModelLoader` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `RH_GetAudioDuration` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
