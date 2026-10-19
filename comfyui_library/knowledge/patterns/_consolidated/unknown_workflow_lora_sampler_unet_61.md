---
name: unknown_workflow_lora_sampler_unet_61
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.597667
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, GetNode, GetVideoComponents, KSamplerSelect, LoadAudio, LoadImage, LoadVideo, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, Seed (rgthree), SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/minimax-h3 单采_2100560974238535682.json, 视频生成/文生视频/minimax-h3单采-v2_2093197455679643650.json, 视频生成/文生视频/minimax-h3双采_2103278801034760193.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_61

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/minimax-h3 单采_2100560974238535682.json、视频生成/文生视频/minimax-h3单采-v2_2093197455679643650.json、视频生成/文生视频/minimax-h3双采_2103278801034760193.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetNode`
- `GetVideoComponents`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `Seed (rgthree)`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 2/3 个有
- `BlockSparseAttention` —— 2/3 个有
- `ExtendIntermediateSigmas` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `ManualSigmas` —— 2/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/3 个有
- `MiniMaxH3SigmaShift` —— 2/3 个有
- `ModelPreviewOverrideKJ` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `TrimAudioDuration` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `LTXVConcatAVLatent` —— 1/3 个有
- `LTXVSeparateAVLatent` —— 1/3 个有
- `MiniMaxChunkFeedForward` —— 1/3 个有
- `MiniMaxLowVRAMAttention` —— 1/3 个有
- `MinimaxH3LatentUpscaler3D` —— 1/3 个有
- `ModelAttentionBackend` —— 1/3 个有
- `SplitSigmas` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
