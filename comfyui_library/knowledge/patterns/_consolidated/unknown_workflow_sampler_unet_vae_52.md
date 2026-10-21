---
name: unknown_workflow_sampler_unet_vae_52
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.826
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax_h3图生视频_2084523818936262657.json, 视频生成/图生视频/minimax_h3图生视频（稳定）_2085014325353340930.json, 视频生成/图生视频/minimax_图生视频8步加速_2087371300875620353.json, 视频生成/图生视频/minimaxh3首尾帧视频_2109562727692849153.json, 视频生成/图生视频/minimax图出视频_2084274641455112193.json, 视频生成/图生视频/minmaxh3图生视频_2109544409682497537.json, 视频生成/图生视频/minnimax h3 首尾帧生视频（4步加速）_2085544529314271234.json, 视频生成/图生视频/minnimax h3 首帧生视频（8步加速）_2085549343964221442.json, 视频生成/图生视频/video_minimax_h3_i2v 开源comfyui 官方版本_2084149773224992770.json, 视频生成/文生视频/MiniMax H3 文生视频 8步加速_2085538844547575810.json, 视频生成/文生视频/MiniMaxH3地表最强阿里3步加速Lora 效果炸裂_2099440464775696386.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_52

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/minimax_h3图生视频_2084523818936262657.json、视频生成/图生视频/minimax_h3图生视频（稳定）_2085014325353340930.json、视频生成/图生视频/minimax_图生视频8步加速_2087371300875620353.json、视频生成/图生视频/minimaxh3首尾帧视频_2109562727692849153.json、视频生成/图生视频/minimax图出视频_2084274641455112193.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 9/11 个有
- `PrimitiveFloat` —— 9/11 个有
- `ResolutionSelector` —— 9/11 个有
- `SaveVideo` —— 8/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/11 个有
- `PathchSageAttentionKJ` —— 4/11 个有
- `PreviewImage` —— 4/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有
- `GetImageSize` —— 3/11 个有
- `ImageScaleToTotalPixels` —— 3/11 个有
- `JjkText` —— 3/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `VHS_VideoCombine` —— 3/11 个有
- `ResizeImageMaskNode` —— 2/11 个有
- `easy int` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `DiffusionModelLoaderKJ` —— 1/11 个有
- `EasyCache` —— 1/11 个有
- `Fast Groups Muter (rgthree)` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `ImageScale` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `RTXVideoSuperResolution` —— 1/11 个有
- `SpectrumApplyMiniMaxH3` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
