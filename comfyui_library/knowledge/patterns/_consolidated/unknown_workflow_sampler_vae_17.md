---
name: unknown_workflow_sampler_vae_17
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.853437
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/FastH3 文生视频_2100134500020867073.json, 视频生成/文生视频/FastVideo FastH3：文生视频_2100285646945472514.json, 视频生成/文生视频/FastVideo-FastH3-8-Step-V2 文生视频_2100836004453249025.json, 视频生成/文生视频/Fasth3图生视频_2100129417984036866.json, 视频生成/文生视频/GF01-MiniMax H3：文生视频_2084716666163908609.json, 视频生成/文生视频/H3-文生视频_2088176717721591810.json, 视频生成/文生视频/MINIMAX-H3文生视频工作流_2099829311577616385.json, 视频生成/文生视频/MINIMAXH3-文生视频8月8日版本_2086533093908893698.json, 视频生成/文生视频/MiniMax FastH3 v2首尾帧视频_2100074906296872962.json, 视频生成/文生视频/MiniMax H3 T2V 文生视频 加速版_2086019169908248577.json, 视频生成/文生视频/MiniMax H3 T2V 文生视频_2089602856834912257.json, 视频生成/文生视频/MiniMax H3 T2V 文生视频_2097227552527052802.json, 视频生成/文生视频/Minimax h3 4 步 lora2 加速版_2092076952441151490.json, 视频生成/文生视频/fastvideo_fasth3_文生视频-9：16口播5秒_2101846484743450626.json, 视频生成/文生视频/fastvideo_fasth3_文生视频_2101835354880962561.json, 视频生成/文生视频/minimaxH3UltraFastestTrue4_v80LightningSpeed_2098097827569295361.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_17

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/文生视频/FastH3 文生视频_2100134500020867073.json、视频生成/文生视频/FastVideo FastH3：文生视频_2100285646945472514.json、视频生成/文生视频/FastVideo-FastH3-8-Step-V2 文生视频_2100836004453249025.json、视频生成/文生视频/Fasth3图生视频_2100129417984036866.json、视频生成/文生视频/GF01-MiniMax H3：文生视频_2084716666163908609.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 15/16 个有
- `UNETLoader` —— 13/16 个有
- `ModelAttentionBackend` —— 9/16 个有
- `MiniMaxH3SigmaShift` —— 8/16 个有
- `BlockSparseAttention` —— 7/16 个有
- `Label (rgthree)` —— 5/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/16 个有
- `PrimitiveStringMultiline` —— 5/16 个有
- `LoadImage` —— 4/16 个有
- `LoraLoaderModelOnly` —— 4/16 个有
- `DiffusionModelLoaderKJ` —— 3/16 个有
- `SpectrumApplyMiniMaxH3` —— 2/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `GetImageSize` —— 1/16 个有
- `ImageScaleToTotalPixels` —— 1/16 个有
- `LTX_lora_loader` —— 1/16 个有
- `LoadAudio` —— 1/16 个有
- `MiniMaxH3ReferenceToVideo` —— 1/16 个有
- `ModelPreviewOverrideKJ` —— 1/16 个有
- `RTXVideoSuperResolution` —— 1/16 个有
- `SolAttnPatch` —— 1/16 个有
- `VHS_LoadVideo` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
