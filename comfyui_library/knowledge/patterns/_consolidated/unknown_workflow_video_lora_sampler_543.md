---
name: unknown_workflow_video_lora_sampler_543
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.695
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/FastH3 VSA文生视频优化版V1_2096244135350067201.json, 视频生成/文生视频/H3-文生视频（16：9）_2085696662042931202.json, 视频生成/文生视频/H3基础文生视频工作流_2101289589221715969.json, 视频生成/文生视频/MINIMAX-H3 一键生成叙事短片_2085916314648014849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_543

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/FastH3 VSA文生视频优化版V1_2096244135350067201.json、视频生成/文生视频/H3-文生视频（16：9）_2085696662042931202.json、视频生成/文生视频/H3基础文生视频工作流_2101289589221715969.json、视频生成/文生视频/MINIMAX-H3 一键生成叙事短片_2085916314648014849.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `UniBlockSwap` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `MiniMaxH3FastH34StepSetupT8Advanced` —— 1/4 个有
- `MiniMaxH3LoRACompatibilityLoaderT8Advanced` —— 1/4 个有
- `ModelPreviewOverrideKJ` —— 1/4 个有
- `RHLLMChatNode` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
