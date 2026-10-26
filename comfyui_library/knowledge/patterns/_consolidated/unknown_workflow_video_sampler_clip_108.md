---
name: unknown_workflow_video_sampler_clip_108
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.705833
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PathchSageAttentionKJ, PreviewAudio, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, TrimAudioDuration, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/LTX2 高动态音图生视频数字人_2009430936194125826.json, 视频生成/图生视频/LTX-2音频+图片生成视频数字人工作流_2009554904033009666.json, 视频生成/图生视频/LTX2 AI2V音图生视频数字人V1_2009218877204471809.json, 视频生成/图生视频/LTX2 AI2V高动态音图生视频数字人V1_2009236735267442690.json, 视频生成/图生视频/LTX2 audio image to video KJ流_2009128874055045121.json, 视频生成/图生视频/高动态音图生视频数字人LTX2 Ai2V_2009631227556405249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_108

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/LTX2 高动态音图生视频数字人_2009430936194125826.json、视频生成/图生视频/LTX-2音频+图片生成视频数字人工作流_2009554904033009666.json、视频生成/图生视频/LTX2 AI2V音图生视频数字人V1_2009218877204471809.json、视频生成/图生视频/LTX2 AI2V高动态音图生视频数字人V1_2009236735267442690.json、视频生成/图生视频/LTX2 audio image to video KJ流_2009128874055045121.json…）

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
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `VAEDecodeTiled` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `JWInteger` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `RH_LLMAPI_Pro_Node` —— 3/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `VRAMReserver` —— 2/6 个有
- `AudioCrop` —— 1/6 个有
- `Int` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LayerMask: MaskPreview` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `Textbox` —— 1/6 个有
- `VAEDecode` —— 1/6 个有
- `easy float` —— 1/6 个有
- `easy mathFloat` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
