---
name: unknown_workflow_video_lora_sampler_949
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8515
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/文生分镜脚本直出短视频H3_2107358424408350721.json, 视频生成/文生视频/超好用🔥Minimax文生视频V2（双时钟-高质量加速LORA）_2090308200510869505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_949

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/文生分镜脚本直出短视频H3_2107358424408350721.json、视频生成/文生视频/超好用🔥Minimax文生视频V2（双时钟-高质量加速LORA）_2090308200510869505.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `easy saveText` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
