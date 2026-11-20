---
name: unknown_workflow_lora_sampler_unet_239
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.435
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, 孤海注释, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流_2086774898759917569.json, 视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频工作流_2086348400169148418.json, 视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V4.0_2094319638514593793.json, 视频生成/文生视频/自用版  Minimax H3 文生+图参生视频二采高清放大工作流（支持数字人）V4.1_2095775074598088705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_239

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流_2086774898759917569.json、视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频工作流_2086348400169148418.json、视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V4.0_2094319638514593793.json、视频生成/文生视频/自用版  Minimax H3 文生+图参生视频二采高清放大工作流（支持数字人）V4.1_2095775074598088705.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `孤海注释`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `Int` —— 3/4 个有
- `MiniMaxChunkFeedForward` —— 3/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `MiniMaxLowVRAMAttention` —— 3/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `LTXVConcatAVLatent` —— 2/4 个有
- `LTXVSeparateAVLatent` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `MiniMaxH3SigmaShift` —— 2/4 个有
- `MinimaxH3LatentUpscaler3D` —— 2/4 个有
- `ModelAttentionBackend` —— 2/4 个有
- `SolAttnPatch` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `ManualSigmas` —— 1/4 个有
- `PT_H3ConcatAVLatent` —— 1/4 个有
- `VAEEncode` —— 1/4 个有
- `VAEEncodeAudio` —— 1/4 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
