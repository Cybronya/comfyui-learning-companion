---
name: unknown_workflow_video_upscale_latent_upscale_150
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.515
common_nodes: [1hew_AnySwitchSelect, Any Switch (rgthree), Astra, BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, CreateVideo, Fast Groups Muter (rgthree), Float, GetNode, GetVideoComponents, H3SigmaRefiner, INTConstant, ImageConcanate, ImageScaleToTotalPixels, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RHLLMChatNode, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SolAttnMiniMax, SplitSigmas, StringConcatenate, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy positive, easy showAnything, 忽略多组孤海]
problems: []
missing: []
members: [平台全量/哆啦哇咔全能流合集_2117160459651600385.json, 视频生成/图生视频/哆啦哇咔全能流(自用)_2113353471985537026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_150

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/哆啦哇咔全能流合集_2117160459651600385.json、视频生成/图生视频/哆啦哇咔全能流(自用)_2113353471985537026.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 2 个 workflow 都包含：
- `1hew_AnySwitchSelect`
- `Any Switch (rgthree)`
- `Astra`
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `Fast Groups Muter (rgthree)`
- `Float`
- `GetNode`
- `GetVideoComponents`
- `H3SigmaRefiner`
- `INTConstant`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RHLLMChatNode`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SolAttnMiniMax`
- `SplitSigmas`
- `StringConcatenate`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy positive`
- `easy showAnything`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 1/2 个有
- `LTXVAudioVAEEncode` —— 1/2 个有
- `LoadAudioUI` —— 1/2 个有
- `Pick From Batch (mtb)` —— 1/2 个有
- `QwenH3PromptLocal` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `SolidMask` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
