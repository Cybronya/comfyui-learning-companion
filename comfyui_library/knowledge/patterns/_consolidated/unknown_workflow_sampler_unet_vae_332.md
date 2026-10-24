---
name: unknown_workflow_sampler_unet_vae_332
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8655
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/战斗双采首尾帧模式_2094373774731862018.json, 视频生成/文生视频/智能版minimax+H3+开源版+文生视频+T2VA文生_2084150373744472066.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_332

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/战斗双采首尾帧模式_2094373774731862018.json、视频生成/文生视频/智能版minimax+H3+开源版+文生视频+T2VA文生_2084150373744472066.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DisableNoise` —— 1/2 个有
- `ExtendIntermediateSigmas` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MiniMaxH3BlockCacheT8` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `SplitSigmasDenoise` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
