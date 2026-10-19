---
name: unknown_workflow_lora_sampler_unet_88
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MotionContext, MiniMaxH3MotionContextLoadLatent, MiniMaxH3MotionContextSaveLatent, MiniMaxH3MotionContextTrim, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/测试_2105592631140110338.json, 视频生成/文生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context FL2VA_2090325146975424514.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_88

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/测试_2105592631140110338.json、视频生成/文生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context FL2VA_2090325146975424514.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextLoadLatent`
- `MiniMaxH3MotionContextSaveLatent`
- `MiniMaxH3MotionContextTrim`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockSparseAttention` —— 1/2 个有
- `GetVideoComponents` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `MiniMaxH3ImageToVideo` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `MiniMaxH3MotionContextChain` —— 1/2 个有
- `MiniMaxH3ReferenceToVideo` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `ViggleAnimateConditioningWindowed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
