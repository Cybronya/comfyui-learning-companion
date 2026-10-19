---
name: unknown_workflow_video_lora_sampler_205
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8316
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/(贞贞lora-双时钟-8步高质量极速)Minimax文生视频V1_2086638410957148161.json, 视频生成/文生视频/10Eros Beta+Lightx2v正式版Minimax双时钟图生视频V1_2087829000017244161.json, 视频生成/文生视频/10Eros Beta+Lightx2v正式版Minimax双时钟文生视频V1_2087432709114261505.json, 视频生成/文生视频/720P双时钟高质量加速 0.8_2087157302087471105.json, 视频生成/文生视频/8步高质量极速Minimax海螺h3图生视频加速优化版t8_2085586436685910018.json, 视频生成/文生视频/DG_H3 双时钟 图生视频V1 bf16_2087807546869501953.json, 视频生成/文生视频/Dasiwa-MiniMax H3-动态最强-单采-文生视频_2094938114493083650.json, 视频生成/文生视频/H3-最优加速工作流_2085603426867695618.json, 视频生成/文生视频/Minimax-H3极速视频编辑(双时钟-8步lora)_2086326048232398850.json, 视频生成/文生视频/Minimax多参(双时钟8步高质量极速)V2_2093869475740344321.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_205

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/(贞贞lora-双时钟-8步高质量极速)Minimax文生视频V1_2086638410957148161.json、视频生成/文生视频/10Eros Beta+Lightx2v正式版Minimax双时钟图生视频V1_2087829000017244161.json、视频生成/文生视频/10Eros Beta+Lightx2v正式版Minimax双时钟文生视频V1_2087432709114261505.json、视频生成/文生视频/720P双时钟高质量加速 0.8_2087157302087471105.json、视频生成/文生视频/8步高质量极速Minimax海螺h3图生视频加速优化版t8_2085586436685910018.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
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
- `CR Prompt Text` —— 8/10 个有
- `LoadImage` —— 8/10 个有
- `ModelAttentionBackend` —— 4/10 个有
- `VHS_LoadVideo` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `Getter` —— 1/10 个有
- `ImageConcatMulti` —— 1/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `LoraLoaderModelOnly` —— 1/10 个有
- `MiniMaxH3SigmaShift` —— 1/10 个有
- `ModelPreviewOverrideKJ` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `Setter` —— 1/10 个有
- `孤海注释` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
