---
name: unknown_workflow_lora_sampler_unet_196
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84925
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/58.MiniMax H3 全能参考加速极简_2087136892977504257.json, 视频生成/文生视频/minimaxH3多参考视频工作流（超级加速版）_2080928622717784066.json, 视频生成/文生视频/【Gensor-AI】MINIMAX-H3工作流合集【加速版】_2085550246054162433.json, 视频生成/文生视频/【遇见AI】minimax H3 高动态打斗场景武术动作二采修复+提示词skill工作流_2095684866888257537.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_196

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/58.MiniMax H3 全能参考加速极简_2087136892977504257.json、视频生成/文生视频/minimaxH3多参考视频工作流（超级加速版）_2080928622717784066.json、视频生成/文生视频/【Gensor-AI】MINIMAX-H3工作流合集【加速版】_2085550246054162433.json、视频生成/文生视频/【遇见AI】minimax H3 高动态打斗场景武术动作二采修复+提示词skill工作流_2095684866888257537.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
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

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 3/4 个有
- `KSamplerSelect` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Label (rgthree)` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `DisableNoise` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/4 个有
- `ModelPreviewOverrideKJ` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `SpectrumSDXL` —— 1/4 个有
- `SplitSigmas` —— 1/4 个有
- `TextInput` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
