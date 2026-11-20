---
name: unknown_workflow_video_upscale_latent_upscale_146
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.852
common_nodes: [Bool, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, Int, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAddVideoICLoRAGuideAdvanced, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LTXVSpatioTemporalTiledVAEDecode, LatentUpscaleModelLoader, LoadAudio, LoadImage, ManualSigmas, MathExpression|pysssss, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SeedGenerator, SetLatentNoiseMask, SolidMask, TextInput_, TrimAudioDuration, UNETLoader, VAELoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy convertAnything, easy ifElse]
problems: []
missing: []
members: [平台全量/LTX-2.3 视频编辑： 运镜+视频人物替换+自定义音频_2046642168843997185.json, 视频生成/图生视频/LTX-2.3 运镜参考图生视频_2044414119499010050.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_146

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/LTX-2.3 视频编辑： 运镜+视频人物替换+自定义音频_2046642168843997185.json、视频生成/图生视频/LTX-2.3 运镜参考图生视频_2044414119499010050.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `Bool`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAddVideoICLoRAGuideAdvanced`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `ManualSigmas`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SeedGenerator`
- `SetLatentNoiseMask`
- `SolidMask`
- `TextInput_`
- `TrimAudioDuration`
- `UNETLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy convertAnything`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowFloat` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAEDecodeTiled` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | - | 2 | 100% |
| 高度 | 24 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
