---
name: unknown_workflow_video_lora_sampler_378
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.854833
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minmax生图工作流_2097534784162582529.json, 视频生成/图生视频/【官模】Lightx2v正式版+8步加速+_+Minimax双时钟参考生视频V1_2087816150808879105.json, 视频生成/图生视频/双时钟采样4步无损加速｜MiniMAX-H3-T8图生视频_2096460092848828418.json, 视频生成/图生视频/（4步极速转化版) Minimax开源 双时钟图生视频快速生视频_2086025973031587841.json, 视频生成/文生视频/H3-最优加速工作流_2085603426867695618.json, 视频生成/文生视频/极速版 MinimaxH3 首尾帧 图生视频 文生视频 T8版_2085915545450401793.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_378

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/minmax生图工作流_2097534784162582529.json、视频生成/图生视频/【官模】Lightx2v正式版+8步加速+_+Minimax双时钟参考生视频V1_2087816150808879105.json、视频生成/图生视频/双时钟采样4步无损加速｜MiniMAX-H3-T8图生视频_2096460092848828418.json、视频生成/图生视频/（4步极速转化版) Minimax开源 双时钟图生视频快速生视频_2086025973031587841.json、视频生成/文生视频/H3-最优加速工作流_2085603426867695618.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
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
- `CR Prompt Text` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `CM_IntToFloat` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `MiniMaxH3TurboLoRA` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
