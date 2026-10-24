---
name: unknown_workflow_sampler_vae_48
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.78325
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3+图生视频_首尾帧低显存加速版(6~8GB)_2085705273888559106.json, 视频生成/图生视频/MinimaxH3-图生视频_2088576094667632642.json, 视频生成/图生视频/minimax图出视频_2084274641455112193.json, 视频生成/文生视频/MINIMAX-H3 sage+sol att双加速低显存全功能工作流_2084920261798879233.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_48

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3+图生视频_首尾帧低显存加速版(6~8GB)_2085705273888559106.json、视频生成/图生视频/MinimaxH3-图生视频_2088576094667632642.json、视频生成/图生视频/minimax图出视频_2084274641455112193.json、视频生成/文生视频/MINIMAX-H3 sage+sol att双加速低显存全功能工作流_2084920261798879233.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `UniBlockSwap` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `DiffusionModelLoaderKJ` —— 1/4 个有
- `Int` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `LoraLoaderBypassModelOnly` —— 1/4 个有
- `MiniMaxH3ReferenceToVideo` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `SolAttnPatch` —— 1/4 个有
- `UniBlockSwapTE` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
