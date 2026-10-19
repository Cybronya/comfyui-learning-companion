---
name: unknown_workflow_video_upscale_latent_upscale_102
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.767333
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetImageSizeAndCount, GetNode, ImageResizeKJv2, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, TrimAudioDuration, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2021873842758619137.json, 视频生成/图生视频/2010630264770269185.json, 视频生成/图生视频/2034521088973082625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_102

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2021873842758619137.json、视频生成/图生视频/2010630264770269185.json、视频生成/图生视频/2034521088973082625.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
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
- `INTConstant` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `AudioSeparation` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `Float` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
