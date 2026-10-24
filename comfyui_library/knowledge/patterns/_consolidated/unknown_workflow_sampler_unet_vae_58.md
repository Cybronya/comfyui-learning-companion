---
name: unknown_workflow_sampler_unet_vae_58
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.863929
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/FS-video_minimax_h3_r2v_2105628001928044546.json, 视频生成/文生视频/FastH3 文生视频_2100134500020867073.json, 视频生成/文生视频/FastVideo FastH3：文生视频_2100285646945472514.json, 视频生成/文生视频/FastVideo-FastH3-8-Step-V2 文生视频_2100836004453249025.json, 视频生成/文生视频/Fasth3图生视频_2100129417984036866.json, 视频生成/文生视频/GF01-MiniMax H3：文生视频_2084716666163908609.json, 视频生成/文生视频/H3 关键帧视频动画_2106371268684636162.json, 视频生成/文生视频/MiniMax FastH3 v2首尾帧视频_2100074906296872962.json, 视频生成/文生视频/MiniMax H3 加速版 图生视频 首尾帧生视频_2086653248143978497.json, 视频生成/文生视频/MiniMax H3 加速版 文生视频_2086639037351284737.json, 视频生成/文生视频/MiniMax H3 图生视频 首尾帧生视频_2085441158259494913.json, 视频生成/文生视频/MiniMax H3｜5图多参考快速出片｜5-15秒｜稳定版_2091107780571783170.json, 视频生成/文生视频/Minimax H3 多参生视频_2087727061006901250.json, 视频生成/文生视频/minmaxH3单采加速_2105257162896404482.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_58

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/FS-video_minimax_h3_r2v_2105628001928044546.json、视频生成/文生视频/FastH3 文生视频_2100134500020867073.json、视频生成/文生视频/FastVideo FastH3：文生视频_2100285646945472514.json、视频生成/文生视频/FastVideo-FastH3-8-Step-V2 文生视频_2100836004453249025.json、视频生成/文生视频/Fasth3图生视频_2100129417984036866.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
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
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 13/14 个有
- `VAEDecodeAudio` —— 13/14 个有
- `LoadImage` —— 9/14 个有
- `MiniMaxH3ImageToVideo` —— 9/14 个有
- `MiniMaxH3SigmaShift` —— 8/14 个有
- `ModelAttentionBackend` —— 8/14 个有
- `BlockSparseAttention` —— 6/14 个有
- `PrimitiveStringMultiline` —— 6/14 个有
- `MiniMaxH3ReferenceToVideo` —— 5/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/14 个有
- `GetImageSize` —— 3/14 个有
- `ImageScaleToTotalPixels` —— 3/14 个有
- `Label (rgthree)` —— 3/14 个有
- `MiniMaxH3BlockCacheT8` —— 3/14 个有
- `LoraLoaderModelOnly` —— 2/14 个有
- `ExtendIntermediateSigmas` —— 1/14 个有
- `LoadAudio` —— 1/14 个有
- `SaveImage` —— 1/14 个有
- `Text` —— 1/14 个有
- `VAEDecodeTiled` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
