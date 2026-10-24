---
name: unknown_workflow_video_lora_sampler_446
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8394
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/（自编排-Confucius4-R2T2）MiniMax H3数字人加速版V1_2104777855577186305.json, 视频生成/图生视频/（自编排数字人音频MV-Confucius4-R2T2）MiniMax H3数字人加速_2105353404636811266.json, 视频生成/文生视频/Minimax4步lora+双时钟-超快速工作流_2085689486171787265.json, 视频生成/文生视频/Minimax文生视频（Lightx2v正式版8步lora+双时钟）_2087718430937014273.json, 视频生成/文生视频/minimaxH3文生视频（light2v8步lora+双时钟）_2087529767288524801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_446

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/（自编排-Confucius4-R2T2）MiniMax H3数字人加速版V1_2104777855577186305.json、视频生成/图生视频/（自编排数字人音频MV-Confucius4-R2T2）MiniMax H3数字人加速_2105353404636811266.json、视频生成/文生视频/Minimax4步lora+双时钟-超快速工作流_2085689486171787265.json、视频生成/文生视频/Minimax文生视频（Lightx2v正式版8步lora+双时钟）_2087718430937014273.json、视频生成/文生视频/minimaxH3文生视频（light2v8步lora+双时钟）_2087529767288524801.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 4/5 个有
- `LoadAudio` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `Float to Int` —— 2/5 个有
- `MiniMaxH3PromptEnhancerT8` —— 2/5 个有
- `R2T2GGUFLoader` —— 2/5 个有
- `R2T2Transcribe` —— 2/5 个有
- `SolAttnMiniMax` —— 2/5 个有
- `StringConcatenate` —— 2/5 个有
- `T8PerformanceDirectorConfig` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `easy showAnything` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
