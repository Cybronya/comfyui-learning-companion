---
name: unknown_workflow_video_sampler_vae_32
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.9125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/海螺H3图生视频官方工作流_2084309077278150657.json, 视频生成/图生视频/漫剧图生视频_2085003263367278593.json, 视频生成/图生视频/空中起舞_2097526794093158402.json, 视频生成/图生视频/空白工作流MinimaxH3首尾帧创意视频T1_2086623709909053442.json, 视频生成/图生视频/美好的夏天_2097286565499330561.json, 视频生成/图生视频/跳肚皮舞的女孩_2098689343039819778.json, 视频生成/图生视频/首尾帧创意电商广告_2087187752570933249.json, 视频生成/图生视频/首尾帧欢乐小狗_2087363013287432194.json, 视频生成/图生视频/首尾帧生成广告视频_2087173880573157377.json, 视频生成/图生视频/首尾帧视频生成_2086728278747996161.json, 视频生成/图生视频/香水广告_2098035698040397826.json, 视频生成/文生视频/minimax_h3_i2v w4a8-超低显存-0810_2086689468593041410.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_32

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/海螺H3图生视频官方工作流_2084309077278150657.json、视频生成/图生视频/漫剧图生视频_2085003263367278593.json、视频生成/图生视频/空中起舞_2097526794093158402.json、视频生成/图生视频/空白工作流MinimaxH3首尾帧创意视频T1_2086623709909053442.json、视频生成/图生视频/美好的夏天_2097286565499330561.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 12 个 workflow 都包含：
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
- `Text` —— 10/12 个有
- `UNETLoader` —— 10/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/12 个有
- `ImageResizeKJv2` —— 7/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/12 个有
- `RHHiddenNodes` —— 5/12 个有
- `RH_Captioner` —— 5/12 个有
- `TextConcatenate_UTK` —— 5/12 个有
- `easy showAnything` —— 5/12 个有
- `LoraLoaderBypassModelOnly` —— 3/12 个有
- `MiniMaxH3BlockCacheT8` —— 3/12 个有
- `ResolutionSelector` —— 3/12 个有
- `Display Any (rgthree)` —— 2/12 个有
- `EnhancedLoadDiffusionModel` —— 2/12 个有
- `PreviewImage` —— 2/12 个有
- `ImageScaleToTotalPixels` —— 1/12 个有
- `PathchSageAttentionKJ` —— 1/12 个有
- `PlaySound|pysssss` —— 1/12 个有
- `SolAttnPatch` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
