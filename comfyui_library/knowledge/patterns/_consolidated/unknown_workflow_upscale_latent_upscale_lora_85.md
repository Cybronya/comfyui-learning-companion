---
name: unknown_workflow_upscale_latent_upscale_lora_85
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7035
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, DisableNoise, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LatentUpscaleBy, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MINIMAXH3高速无损高清放大【三采】【latent放大】【单次解码无解码损失】_2088904401149845505.json, 视频生成/文生视频/MiniMax H3 latent放大双采+8步lora 顶级质量和速度 全能参考工作流_2088909288264785922.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_85

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MINIMAXH3高速无损高清放大【三采】【latent放大】【单次解码无解码损失】_2088904401149845505.json、视频生成/文生视频/MiniMax H3 latent放大双采+8步lora 顶级质量和速度 全能参考工作流_2088909288264785922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `DisableNoise`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LatentUpscaleBy`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 1/2 个有
- `ExtendIntermediateSigmas` —— 1/2 个有
- `H3LatentUpscaleByJingchen573` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `MiniMaxChunkFeedForward` —— 1/2 个有
- `MiniMaxH3HybridLoader` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `SigmasToFloat` —— 1/2 个有
- `easy boolean` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
