---
name: unknown_workflow_lora_sampler_unet_189
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.845
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3-超自然服装细节展示-自动优化提示词-.json, 视频生成/图生视频/h3 Singularity + pika trubo 4步+ 提示词增强 多参视频_2116784854103846913.json, 视频生成/图生视频/minimax_h3变装秀_2097724749970493442.json, 视频生成/图生视频/minimax_h3复刻短视频爆款_2096558185426546690.json, 视频生成/图生视频/超自然超细节-H3的服装展示(singularity)_2101287029765136386.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_189

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3-超自然服装细节展示-自动优化提示词-.json、视频生成/图生视频/h3 Singularity + pika trubo 4步+ 提示词增强 多参视频_2116784854103846913.json、视频生成/图生视频/minimax_h3变装秀_2097724749970493442.json、视频生成/图生视频/minimax_h3复刻短视频爆款_2096558185426546690.json、视频生成/图生视频/超自然超细节-H3的服装展示(singularity)_2101287029765136386.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
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
- `BasicScheduler` —— 4/5 个有
- `MiniMaxH3PromptEnhancerT8` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `easy seed` —— 4/5 个有
- `BlockSparseAttention` —— 3/5 个有
- `INTConstant` —— 2/5 个有
- `LoraLoaderBypassModelOnly` —— 2/5 个有
- `MiniMaxChunkFeedForward` —— 2/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/5 个有
- `Int2String` —— 1/5 个有
- `ManualSigmas` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 1/5 个有
- `StrToCombo` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `easy int` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
