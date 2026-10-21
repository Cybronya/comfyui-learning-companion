---
name: unknown_workflow_video_lora_sampler_286
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.848625
common_nodes: [BasicGuider, CLIPLoader, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3｜VSA 4步_2098331619802308610.json, 视频生成/文生视频/minimax三图工作流_2090738092591378434.json, 视频生成/文生视频/minimax三图工作流_2091847130888630274.json, 视频生成/文生视频/minimax九图工作流_2091582636920758274.json, 视频生成/文生视频/minimax九图工作流_2092593622448427010.json, 视频生成/文生视频/minimax九图工作流_2102148767163183105.json, 视频生成/文生视频/万象AI--MiniMax H3 多参生视频-V2（加速版）_2085937471304585218.json, 视频生成/文生视频/万象AI--MiniMax H3 多参生视频-V3（加速提示词优化版）_2086606105207205889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_286

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3｜VSA 4步_2098331619802308610.json、视频生成/文生视频/minimax三图工作流_2090738092591378434.json、视频生成/文生视频/minimax三图工作流_2091847130888630274.json、视频生成/文生视频/minimax九图工作流_2091582636920758274.json、视频生成/文生视频/minimax九图工作流_2092593622448427010.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 7/8 个有
- `MiniMaxH3DualClockSamplerT8` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `MiniMaxH3AudioConditioningT8` —— 6/8 个有
- `CR Prompt Text` —— 5/8 个有
- `MiniMaxH3ImageToVideo` —— 2/8 个有
- `MiniMaxH3ReferenceToVideo` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `MiniMaxH3FastH34StepSetupT8Advanced` —— 1/8 个有
- `MiniMaxH3LoRACompatibilityLoaderT8Advanced` —— 1/8 个有
- `RHLLMChatNode` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
