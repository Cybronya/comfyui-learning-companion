---
name: unknown_workflow_video_upscale_latent_upscale_54
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.49
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3双人分镜视频生成_2059165088854138882.json, 视频生成/图生视频/LTX-2.3-图生视频_2055514596210946049.json, 视频生成/图生视频/LTX-2.3-首尾帧_2055556105299873793.json, 视频生成/图生视频/LTX-2.3_-_I2V_Short-Story_PromptRelay四图视频制作_2050871854566518786.json, 视频生成/图生视频/LTX2.3+9宫格+AI+漫剧生成+工作流_2061608359572369410.json, 视频生成/图生视频/LTX2首尾帧工作流_2016770696625524737.json, 视频生成/文生视频/LTX2.3 9宫格 AI 漫剧生成 工作流（仅供娱乐测试）_2054171445080666114.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_54

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3双人分镜视频生成_2059165088854138882.json、视频生成/图生视频/LTX-2.3-图生视频_2055514596210946049.json、视频生成/图生视频/LTX-2.3-首尾帧_2055556105299873793.json、视频生成/图生视频/LTX-2.3_-_I2V_Short-Story_PromptRelay四图视频制作_2050871854566518786.json、视频生成/图生视频/LTX2.3+9宫格+AI+漫剧生成+工作流_2061608359572369410.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
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
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 6/7 个有
- `LTX2_NAG` —— 6/7 个有
- `LTX2SamplingPreviewOverride` —— 5/7 个有
- `LTXVPreprocess` —— 5/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `ResizeImagesByLongerEdge` —— 5/7 个有
- `GetImageSize` —— 4/7 个有
- `LTXVAddGuideMulti` —— 4/7 个有
- `LTXVCropGuides` —— 4/7 个有
- `LTXVImgToVideoInplace` —— 4/7 个有
- `PromptRelayEncodeTimeline` —— 4/7 个有
- `ComfyMathExpression` —— 3/7 个有
- `LTX2AttentionTunerPatch` —— 3/7 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 3/7 个有
- `ResizeImageMaskNode` —— 3/7 个有
- `SimpleCalculatorKJ` —— 3/7 个有
- `1hewOffice_Qwen35397BA17B` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `GuHaiAutoImageSplit` —— 2/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `ImageFromBatch+` —— 2/7 个有
- `ImageScaleBy` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `TTResolutionSelector` —— 2/7 个有
- `Textbox` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `Context (rgthree)` —— 1/7 个有
- `Context Switch (rgthree)` —— 1/7 个有
- `JWFloatToInteger` —— 1/7 个有
- `LTX2AudioLatentNormalizingSampling` —— 1/7 个有
- `LTXVImgToVideoInplaceKJ` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `ModelPatchTorchSettings` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 265 | 97 - 721 | 7 | 25% |
| 高度 | 25 | 24 - 25 | 7 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 265，观测区间 97 - 721，7 个样本，取值分散，一致性仅 25%
- 高度 中位数 25，观测区间 24 - 25，7 个样本，取值集中（一致性 99%）
