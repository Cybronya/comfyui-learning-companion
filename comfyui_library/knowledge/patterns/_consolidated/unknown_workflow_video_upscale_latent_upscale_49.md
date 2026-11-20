---
name: unknown_workflow_video_upscale_latent_upscale_49
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.91275
common_nodes: [BetaSamplingScheduler, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVFirstLastFrameControl_TTP, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2魔改版自动首尾帧V1_2009253788510593026.json, 视频生成/图生视频/LTX_2_First_Last_I2V_ttp_v2_2009559520669863938.json, 视频生成/图生视频/LTX_2_首尾帧工作流_2019655709050281986.json, 视频生成/图生视频/LTX_2_首尾帧工作流_2019956098375094274.json, 视频生成/图生视频/LTX_2_首尾帧生视频_2010957418854879234.json, 视频生成/图生视频/LTX_2首尾帧工作流_2020659052396683265.json, 视频生成/图生视频/「Supermate」LTX_2_首尾帧工作流_2009326383134150658.json, 视频生成/图生视频/「Supermate」LTX_2_首尾帧工作流_2057293549762334721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_49

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/LTX2魔改版自动首尾帧V1_2009253788510593026.json、视频生成/图生视频/LTX_2_First_Last_I2V_ttp_v2_2009559520669863938.json、视频生成/图生视频/LTX_2_首尾帧工作流_2019655709050281986.json、视频生成/图生视频/LTX_2_首尾帧工作流_2019956098375094274.json、视频生成/图生视频/LTX_2_首尾帧生视频_2010957418854879234.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `BetaSamplingScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `ResizeImagesByLongerEdge` —— 7/8 个有
- `MemoryCleaner` —— 6/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `> Text Replace` —— 1/8 个有
- `Any To Any` —— 1/8 个有
- `CR Prompt Text` —— 1/8 个有
- `CreateVideo` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `MultiplePathsInput` —— 1/8 个有
- `Qwen3_VQA` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `VHS_SelectFilename` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 8 | 100% |
| 高度 | 25 | 24 - 25 | 8 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，8 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，8 个样本，取值集中（一致性 99%）
