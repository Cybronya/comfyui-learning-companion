---
name: unknown_workflow_video_lora_sampler_949
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.721
common_nodes: [BasicScheduler, CLIPLoader, CR Text, ConditioningZeroOut, Fast Groups Bypasser (rgthree), GetNode, H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MemoryCleaner, MiniMaxChunkFeedForward, MiniMaxH3Unified, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewImage, RH_DLSS5Enhance, ResolutionSelector, SelfLiftH3Sampler, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_SelectImages, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/反推提示词/minimax_h3_多图AI提示词_导演台_12秒视频7分钟4K直出-优化版_2116912393824587778.json, 平台全量/Minimax Pika H3 直出 4K LoRA 去油化 + H3 统一插件 +  自提升渐进式采样工作流_2117649280277245953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_949

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/minimax_h3_多图AI提示词_导演台_12秒视频7分钟4K直出-优化版_2116912393824587778.json、平台全量/Minimax Pika H3 直出 4K LoRA 去油化 + H3 统一插件 +  自提升渐进式采样工作流_2117649280277245953.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MemoryCleaner`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3Unified`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewImage`
- `RH_DLSS5Enhance`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_SelectImages`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `BlockSparseAttention` —— 1/2 个有
- `ComfyMathExpression` —— 1/2 个有
- `Fast Muter (rgthree)` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `QwenH3PromptLocal` —— 1/2 个有
- `VedaSparseAttention` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
