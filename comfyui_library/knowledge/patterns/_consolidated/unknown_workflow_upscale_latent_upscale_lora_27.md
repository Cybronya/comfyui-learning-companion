---
name: unknown_workflow_upscale_latent_upscale_lora_27
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.901364
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/2009253788510593026.json, 视频生成/图生视频/2009559520669863938.json, 视频生成/图生视频/2019655709050281986.json, 视频生成/图生视频/2019956098375094274.json, 视频生成/图生视频/2010957418854879234.json, 视频生成/图生视频/2020659052396683265.json, 视频生成/图生视频/2008723483076861954.json, 视频生成/图生视频/2009326383134150658.json, 视频生成/图生视频/2057293549762334721.json, 视频生成/图生视频/2012047557043687425.json, 视频生成/图生视频/2009604954146742273.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_27

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2009253788510593026.json、视频生成/图生视频/2009559520669863938.json、视频生成/图生视频/2019655709050281986.json、视频生成/图生视频/2019956098375094274.json、视频生成/图生视频/2010957418854879234.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 10/11 个有
- `PrimitiveInt` —— 10/11 个有
- `ResizeImagesByLongerEdge` —— 10/11 个有
- `VHS_VideoCombine` —— 10/11 个有
- `BetaSamplingScheduler` —— 9/11 个有
- `LTXVFirstLastFrameControl_TTP` —— 9/11 个有
- `MemoryCleaner` —— 8/11 个有
- `ImageResizeKJv2` —— 4/11 个有
- `CR Prompt Text` —— 2/11 个有
- `CreateVideo` —— 2/11 个有
- `INTConstant` —— 2/11 个有
- `LTXVImgToVideoInplace` —— 2/11 个有
- `Qwen3_VQA` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `> Text Replace` —— 1/11 个有
- `Any To Any` —— 1/11 个有
- `Any To String (mtb)` —— 1/11 个有
- `ImageConcatMulti` —— 1/11 个有
- `JWInteger` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `MathExpression|pysssss` —— 1/11 个有
- `MultiplePathsInput` —— 1/11 个有
- `Resize` —— 1/11 个有
- `SaveVideo` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有
- `SmartImageConcat` —— 1/11 个有
- `Textbox` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有
- `VHS_SelectFilename` —— 1/11 个有
- `easy promptConcat` —— 1/11 个有
- `easy showAnything` —— 1/11 个有
- `easy textSwitch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 11 | 100% |
| 高度 | 25 | 24 - 25 | 11 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，11 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，11 个样本，取值集中（一致性 99%）
