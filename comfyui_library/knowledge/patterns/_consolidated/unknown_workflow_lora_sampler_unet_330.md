---
name: unknown_workflow_lora_sampler_unet_330
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8445
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MotionContext, MiniMaxH3MotionContextLoadLatent, MiniMaxH3MotionContextSaveLatent, MiniMaxH3MotionContextTrim, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo]
problems: []
missing: []
members: [视频生成/图生视频/【遇见AI】Minimax H3 连续衔接插件 H3 Motion Context REF加无限循环_2113847877008187394.json, 视频生成/图生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context REF2V_2090326053301612546.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_330

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/【遇见AI】Minimax H3 连续衔接插件 H3 Motion Context REF加无限循环_2113847877008187394.json、视频生成/图生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context REF2V_2090326053301612546.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextLoadLatent`
- `MiniMaxH3MotionContextSaveLatent`
- `MiniMaxH3MotionContextTrim`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `GoohaiAnySwitch` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `easy textIndexSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
