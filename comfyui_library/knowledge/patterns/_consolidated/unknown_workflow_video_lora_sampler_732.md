---
name: unknown_workflow_video_lora_sampler_732
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9365
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3反推提示词+极速二次采样高质量图_文生视频_2087448718474825729.json, 视频生成/图生视频/minimax h3超级加强！清晰度天花板_2088308372293640194.json, 视频生成/图生视频/v3 minimax h3超级加强！清晰度天花板_2088502342512631810.json, 视频生成/图生视频/v4 minimax h3-Sigmas 区间控制_2089033224172425217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_732

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3反推提示词+极速二次采样高质量图_文生视频_2087448718474825729.json、视频生成/图生视频/minimax h3超级加强！清晰度天花板_2088308372293640194.json、视频生成/图生视频/v3 minimax h3超级加强！清晰度天花板_2088502342512631810.json、视频生成/图生视频/v4 minimax h3-Sigmas 区间控制_2089033224172425217.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `VAEEncodeTiled` —— 3/4 个有
- `ExtendIntermediateSigmas` —— 2/4 个有
- `H3SigmaRefiner` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `Dapao_LlamaCaption` —— 1/4 个有
- `Dapao_LlamaCaptionOptions` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ModelPreviewOverrideKJ` —— 1/4 个有
- `RegexReplace` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `easy promptConcat` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `solarL_VideoFrameRelay` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
