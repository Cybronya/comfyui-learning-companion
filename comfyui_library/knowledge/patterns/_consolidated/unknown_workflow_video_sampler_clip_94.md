---
name: unknown_workflow_video_sampler_clip_94
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.711833
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PathchSageAttentionKJ, PreviewAudio, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, TrimAudioDuration, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2009554904033009666.json, 视频生成/图生视频/2009218877204471809.json, 视频生成/图生视频/2009236735267442690.json, 视频生成/图生视频/2012440624145899522.json, 视频生成/图生视频/2009128874055045121.json, 视频生成/图生视频/2009631227556405249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_94

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2009554904033009666.json、视频生成/图生视频/2009218877204471809.json、视频生成/图生视频/2009236735267442690.json、视频生成/图生视频/2012440624145899522.json、视频生成/图生视频/2009128874055045121.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetNode`
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
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `CR Prompt Text` —— 3/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `JWInteger` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `Int` —— 2/6 个有
- `RH_LLMAPI_Pro_Node` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `AudioCrop` —— 1/6 个有
- `Float` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LayerMask: MaskPreview` —— 1/6 个有
- `RH_GetAudioDuration` —— 1/6 个有
- `Textbox` —— 1/6 个有
- `VRAMReserver` —— 1/6 个有
- `easy float` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
