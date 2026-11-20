---
name: unknown_workflow_lora_sampler_unet_336
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.511
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, H3SigmaRefiner, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SolAttnMiniMax, UNETLoader, VAELoader, VHS_LoadVideo, 孤海注释]
problems: []
missing: []
members: [视频生成/文生视频/🔪🔪H3突破15秒！长视频不劣化！工作流拆解系列06集_2093951850499366914.json, 视频生成/文生视频/🔪🔪阶段总结版！MiniMax H3全功能加速工作流拆解系列04集_2091383371724316673.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_336

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/🔪🔪H3突破15秒！长视频不劣化！工作流拆解系列06集_2093951850499366914.json、视频生成/文生视频/🔪🔪阶段总结版！MiniMax H3全功能加速工作流拆解系列04集_2091383371724316673.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`
- `VHS_LoadVideo`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ExtendIntermediateSigmas` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `MiniMaxH3AVDecodeT8` —— 1/2 个有
- `MiniMaxH3AddGuide` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
