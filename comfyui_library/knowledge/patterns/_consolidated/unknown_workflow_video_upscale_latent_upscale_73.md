---
name: unknown_workflow_video_upscale_latent_upscale_73
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.4678
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTX2AttentionTunerPatch, LTX2MemoryEfficientSageAttentionPatch, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, PrimitiveFloat, PromptRelayEncodeTimeline, RandomNoise, SamplerCustomAdvanced, SetNode, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3+9宫格+AI+漫剧生成+工作流_2061608359572369410.json, 视频生成/图生视频/Sulphur-2 timelinePrompt时序视频_2053346294621589505.json, 视频生成/图生视频/ltx2.3-PromptRelay-4宫格工作流-1.66-24G_2063565423085445122.json, 视频生成/图生视频/ltx2.3-PromptRelay-4宫格工作流-1.80_2073745164908191745.json, 视频生成/文生视频/LTX2.3 9宫格 AI 漫剧生成 工作流（仅供娱乐测试）_2054171445080666114.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_73

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/LTX2.3+9宫格+AI+漫剧生成+工作流_2061608359572369410.json、视频生成/图生视频/Sulphur-2 timelinePrompt时序视频_2053346294621589505.json、视频生成/图生视频/ltx2.3-PromptRelay-4宫格工作流-1.66-24G_2063565423085445122.json、视频生成/图生视频/ltx2.3-PromptRelay-4宫格工作流-1.80_2073745164908191745.json、视频生成/文生视频/LTX2.3 9宫格 AI 漫剧生成 工作流（仅供娱乐测试）_2054171445080666114.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTX2AttentionTunerPatch`
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PromptRelayEncodeTimeline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GuHaiAutoImageSplit` —— 4/5 个有
- `ImageFromBatch+` —— 4/5 个有
- `LTXVAddGuideMulti` —— 4/5 个有
- `LTXVCropGuides` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `LTXVPreprocess` —— 3/5 个有
- `ResizeImagesByLongerEdge` —— 3/5 个有
- `1hewOffice_Qwen35397BA17B` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `ResizeImageMaskNode` —— 2/5 个有
- `TTResolutionSelector` —— 2/5 个有
- `Textbox` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `LTXAVTextEncoderLoader` —— 1/5 个有
- `LTXVAudioVAELoader` —— 1/5 个有
- `LTXVImgToVideoInplace` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `SeedGenerator` —— 1/5 个有
- `SimpleCalculatorKJ` —— 1/5 个有
- `easy ckptNames` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 289 | 241 - 361 | 5 | 85% |
| 高度 | 25 | 24 - 25 | 5 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 289，观测区间 241 - 361，5 个样本，取值集中（一致性 85%）
- 高度 中位数 25，观测区间 24 - 25，5 个样本，取值集中（一致性 98%）
