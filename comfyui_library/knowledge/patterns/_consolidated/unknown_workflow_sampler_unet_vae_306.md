---
name: unknown_workflow_sampler_unet_vae_306
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7855
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/海螺H3八步极速生成文图首尾帧视频3合一工作流_2088515866974576641.json, 视频生成/文生视频/MiniMax H3 加速版 图生视频 首尾帧生视频_2086653248143978497.json, 视频生成/文生视频/MiniMax H3 图生视频 首尾帧生视频_2085441158259494913.json, 视频生成/文生视频/MinimaxH3文生_图生多合一工作流【开源版】_2084181479239802882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_306

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/海螺H3八步极速生成文图首尾帧视频3合一工作流_2088515866974576641.json、视频生成/文生视频/MiniMax H3 加速版 图生视频 首尾帧生视频_2086653248143978497.json、视频生成/文生视频/MiniMax H3 图生视频 首尾帧生视频_2085441158259494913.json、视频生成/文生视频/MinimaxH3文生_图生多合一工作流【开源版】_2084181479239802882.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
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
- `AnyBooleanSwitch` —— 2/4 个有
- `EmptyImage` —— 2/4 个有
- `ImpactConditionalBranch` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `MiniMaxH3BlockCacheT8` —— 2/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/4 个有
- `CM_BoolBinaryOperation` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `PainterVRAM` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `Switch image [Crystools]` —— 1/4 个有
- `easy boolean` —— 1/4 个有
- `easy convertAnything` —— 1/4 个有
- `easy float` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
