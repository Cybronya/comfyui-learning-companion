---
name: unknown_workflow_video_lora_sampler_564
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7585
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/万象AI--MiniMax H3 多参生视频-V2（加速版）_2085937471304585218.json, 视频生成/文生视频/万象AI--MiniMax H3 多参生视频-V3（加速提示词优化版）_2086606105207205889.json, 视频生成/文生视频/加速版 只需4步，300s，0.9倍百万像素 minimax h3 4步加速lightx2v_2086649957204979713.json, 视频生成/文生视频/打斗专用工作流MINIMAX-H3_2089439571347066881.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_564

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/万象AI--MiniMax H3 多参生视频-V2（加速版）_2085937471304585218.json、视频生成/文生视频/万象AI--MiniMax H3 多参生视频-V3（加速提示词优化版）_2086606105207205889.json、视频生成/文生视频/加速版 只需4步，300s，0.9倍百万像素 minimax h3 4步加速lightx2v_2086649957204979713.json、视频生成/文生视频/打斗专用工作流MINIMAX-H3_2089439571347066881.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3DualClockSamplerT8` —— 3/4 个有
- `MiniMaxH3ReferenceToVideo` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `BasicScheduler` —— 2/4 个有
- `KSamplerSelect` —— 2/4 个有
- `MiniMaxH3ImageToVideo` —— 2/4 个有
- `LoadAudio` —— 1/4 个有
- `MiniMaxH3AudioConditioningT8` —— 1/4 个有
- `PT_H3ConcatAVLatent` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `RHLLMChatNode` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `VAEEncode` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
