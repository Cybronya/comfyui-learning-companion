---
name: unknown_workflow_sampler_vae_40
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8585
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax-h3首尾帧工作流_2078283699623391233.json, 视频生成/图生视频/minimax-h3首尾帧工作流_2086646638457737217.json, 视频生成/图生视频/minimaxH3 FL2VA 首尾帧_2093654739836825602.json, 视频生成/图生视频/minimaxH3 ref2va多参工作流_2084130906889089025.json, 视频生成/图生视频/minimax_H3_r2v 2倍加速_2084977611708657665.json, 视频生成/图生视频/minimax_H3_r2v 4步lora加速_2085423519835447298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_40

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/minimax-h3首尾帧工作流_2078283699623391233.json、视频生成/图生视频/minimax-h3首尾帧工作流_2086646638457737217.json、视频生成/图生视频/minimaxH3 FL2VA 首尾帧_2093654739836825602.json、视频生成/图生视频/minimaxH3 ref2va多参工作流_2084130906889089025.json、视频生成/图生视频/minimax_H3_r2v 2倍加速_2084977611708657665.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `LoadAudio` —— 3/6 个有
- `MiniMaxH3ReferenceToVideo` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `EasyCache` —— 2/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/6 个有
- `ResizeImageMaskNode` —— 2/6 个有
- `ResizeImagesByLongerEdge` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `AudioCrop` —— 1/6 个有
- `EmptyMiniMaxH3LatentAV` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `LoraLoaderBypassModelOnly` —— 1/6 个有
- `MiniMaxH3SigmaShift` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
