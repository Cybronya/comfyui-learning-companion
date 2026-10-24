---
name: unknown_workflow_video_lora_sampler_762
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.446
common_nodes: [AddLabel, BasicScheduler, CFGGuider, CLIPLoader, ComfyMathExpression, ComfyNumberConvert, ComfySwitchNode, CreateVideo, EmptyAudio, EmptyMiniMaxH3LatentAV, GetImageSize, GetNode, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3AddGuide, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewAny, PrimitiveFloat, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, SolAttnPatch, SomethingToString, StringConcatenate, TextGenerate, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideoFFmpeg, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 风格参考视频风格迁移_2099000699609767937.json, 视频生成/图生视频/MinimaxH3视频角色替换+lms放大_2110649907953627137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_762

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 风格参考视频风格迁移_2099000699609767937.json、视频生成/图生视频/MinimaxH3视频角色替换+lms放大_2110649907953627137.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：45%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `ComfySwitchNode`
- `CreateVideo`
- `EmptyAudio`
- `EmptyMiniMaxH3LatentAV`
- `GetImageSize`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3AddGuide`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `SolAttnPatch`
- `SomethingToString`
- `StringConcatenate`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `GetVideoComponents` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `LTXVConcatAVLatent` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `MinimaxH3LatentUpscaler3D` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `ResizeImageMaskNode` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
