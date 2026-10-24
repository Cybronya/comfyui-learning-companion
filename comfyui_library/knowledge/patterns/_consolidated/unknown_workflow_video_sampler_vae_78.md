---
name: unknown_workflow_video_sampler_vae_78
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.884286
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/海螺H3图生视频官方工作流_2084309077278150657.json, 视频生成/图生视频/漫剧图生视频_2085003263367278593.json, 视频生成/图生视频/空中起舞_2097526794093158402.json, 视频生成/图生视频/美好的夏天_2097286565499330561.json, 视频生成/图生视频/跳肚皮舞的女孩_2098689343039819778.json, 视频生成/图生视频/香水广告_2098035698040397826.json, 视频生成/文生视频/minimax_h3_i2v w4a8-超低显存-0810_2086689468593041410.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_78

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/海螺H3图生视频官方工作流_2084309077278150657.json、视频生成/图生视频/漫剧图生视频_2085003263367278593.json、视频生成/图生视频/空中起舞_2097526794093158402.json、视频生成/图生视频/美好的夏天_2097286565499330561.json、视频生成/图生视频/跳肚皮舞的女孩_2098689343039819778.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `RH_Captioner` —— 5/7 个有
- `Text` —— 5/7 个有
- `TextConcatenate_UTK` —— 5/7 个有
- `UNETLoader` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `LoraLoaderBypassModelOnly` —— 3/7 个有
- `MiniMaxH3BlockCacheT8` —— 3/7 个有
- `ResolutionSelector` —— 3/7 个有
- `Display Any (rgthree)` —— 2/7 个有
- `EnhancedLoadDiffusionModel` —— 2/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `SolAttnPatch` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
