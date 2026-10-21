---
name: unknown_workflow_sampler_vae_36
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8006
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3+图生视频_首尾帧低显存加速版(6~8GB)_2085705273888559106.json, 视频生成/图生视频/MinimaxH3-图生视频_2088576094667632642.json, 视频生成/文生视频/MiniMax+H3+T2V+文生视频+加速版_2084297867275096065.json, 视频生成/文生视频/MiniMax+H3+T2V+文生视频低显存加速版（6~8GB）_2085705254150168577.json, 视频生成/文生视频/MiniMax+H3+开源版！文生视频！_2084526946423234561.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_36

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3+图生视频_首尾帧低显存加速版(6~8GB)_2085705273888559106.json、视频生成/图生视频/MinimaxH3-图生视频_2088576094667632642.json、视频生成/文生视频/MiniMax+H3+T2V+文生视频+加速版_2084297867275096065.json、视频生成/文生视频/MiniMax+H3+T2V+文生视频低显存加速版（6~8GB）_2085705254150168577.json、视频生成/文生视频/MiniMax+H3+开源版！文生视频！_2084526946423234561.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `DiffusionModelLoaderKJ` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `ResolutionSelector` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `UNETLoader` —— 2/5 个有
- `UniBlockSwap` —— 2/5 个有
- `DuckHideNode` —— 1/5 个有
- `Int` —— 1/5 个有
- `LoraLoaderBypassModelOnly` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
