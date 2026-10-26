---
name: unknown_workflow_video_upscale_latent_upscale_70
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9132
common_nodes: [AudioConcat, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), GetImageSize, H3SigmaRefiner, ImageBatch, ImageBatchMulti, ImageExpandBatch+, ImageFromBatch, ImageScaleToTotalPixels, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxChunkFeedForward, MiniMaxH3AddGuide, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, MinimaxH3LatentUpscaler3D, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, RepeatImageBatch, ResizeImagesByShorterEdge, ResolutionSelector, SamplerCustomAdvanced, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideoFFmpeg, VHS_VideoCombine, VHS_VideoInfo, easy forLoopEnd, easy forLoopStart]
problems: []
missing: []
members: [图片生成/图生图/海螺H3_人物替换专用流v1.5_2113448330415140866.json, 图片生成/图生图/海螺H3_人物替换专用流v1.5_2114638887707561986.json, 视频生成/图生视频/H3 人物替换专用流（村头东 二狗子流）_2109969385438932994.json, 视频生成/图生视频/海螺H3_人物替换专用流v1.5_2113771024394309634.json, 视频生成/图生视频/海螺H3_人物替换专用流v1.5_2113784739583848450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_70

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/海螺H3_人物替换专用流v1.5_2113448330415140866.json、图片生成/图生图/海螺H3_人物替换专用流v1.5_2114638887707561986.json、视频生成/图生视频/H3 人物替换专用流（村头东 二狗子流）_2109969385438932994.json、视频生成/图生视频/海螺H3_人物替换专用流v1.5_2113771024394309634.json、视频生成/图生视频/海螺H3_人物替换专用流v1.5_2113784739583848450.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioConcat`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `H3SigmaRefiner`
- `ImageBatch`
- `ImageBatchMulti`
- `ImageExpandBatch+`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3AddGuide`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `MinimaxH3LatentUpscaler3D`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `RepeatImageBatch`
- `ResizeImagesByShorterEdge`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 4/5 个有
- `PreviewImage` —— 3/5 个有
- `EmptyImage` —— 2/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
