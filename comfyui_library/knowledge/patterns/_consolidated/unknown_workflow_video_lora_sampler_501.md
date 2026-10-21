---
name: unknown_workflow_video_lora_sampler_501
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8395
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3极速二采高质量图_文生视频_2086658165340463105.json, 视频生成/图生视频/MiniMax+H3 图生视频+首尾帧+ 超级加速版_2087338012370890753.json, 视频生成/图生视频/MiniMax-H3 图生视频！ 加速版！_2085683743284621314.json, 视频生成/图生视频/MiniMax_H3反推提示词+极速二次采样高质量图_文生视频_2087448718474825729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_501

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3极速二采高质量图_文生视频_2086658165340463105.json、视频生成/图生视频/MiniMax+H3 图生视频+首尾帧+ 超级加速版_2087338012370890753.json、视频生成/图生视频/MiniMax-H3 图生视频！ 加速版！_2085683743284621314.json、视频生成/图生视频/MiniMax_H3反推提示词+极速二次采样高质量图_文生视频_2087448718474825729.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
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
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `BasicScheduler` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `KSamplerSelect` —— 2/4 个有
- `Label (rgthree)` —— 2/4 个有
- `PT_H3ConcatAVLatent` —— 2/4 个有
- `Text` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `Dapao_LlamaCaption` —— 1/4 个有
- `Dapao_LlamaCaptionOptions` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `LoadVideo` —— 1/4 个有
- `RegexReplace` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `easy promptConcat` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
