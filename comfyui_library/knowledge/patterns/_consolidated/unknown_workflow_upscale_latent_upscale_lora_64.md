---
name: unknown_workflow_upscale_latent_upscale_lora_64
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.90025
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MinimaxH3LatentUpscaler3D, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax_H3_打斗强化工作流（二采+打斗lora+动作修复）_2092573716482969601.json, 视频生成/文生视频/Minimax H3 多参数视频生成 768p 加速 LoRA 两步生成_2095762977566846977.json, 视频生成/文生视频/Minimax-h3-文生、图生视频+双采+Lantent upscale放大_2091360806108745730.json, 视频生成/文生视频/minimax h3综合型工作流第一人称，男友视角_2108015047955013633.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_64

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMax_H3_打斗强化工作流（二采+打斗lora+动作修复）_2092573716482969601.json、视频生成/文生视频/Minimax H3 多参数视频生成 768p 加速 LoRA 两步生成_2095762977566846977.json、视频生成/文生视频/Minimax-h3-文生、图生视频+双采+Lantent upscale放大_2091360806108745730.json、视频生成/文生视频/minimax h3综合型工作流第一人称，男友视角_2108015047955013633.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MinimaxH3LatentUpscaler3D`
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `MiniMaxH3ReferenceToVideo` —— 3/4 个有
- `MiniMaxH3SigmaShift` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `ModelPreviewOverrideKJ` —— 2/4 个有
- `SplitSigmas` —— 2/4 个有
- `CLIPTextEncode` —— 1/4 个有
- `DisableNoise` —— 1/4 个有
- `ExtendIntermediateSigmas` —— 1/4 个有
- `GetVideoComponents` —— 1/4 个有
- `H3SigmaRefiner` —— 1/4 个有
- `LoadVideo` —— 1/4 个有
- `ManualSigmas` —— 1/4 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/4 个有
- `MiniMaxH3ImageToVideo` —— 1/4 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/4 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/4 个有
- `SolAttnMiniMax` —— 1/4 个有
- `SplitSigmasDenoise` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
