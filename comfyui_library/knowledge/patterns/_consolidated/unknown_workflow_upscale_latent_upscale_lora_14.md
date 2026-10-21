---
name: unknown_workflow_upscale_latent_upscale_lora_14
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.872643
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced]
problems: []
missing: []
members: [视频生成/图生视频/2017463595512111106.json, 视频生成/图生视频/2009155672465743874.json, 视频生成/图生视频/2009919579048382465.json, 视频生成/图生视频/2009073353373519874.json, 视频生成/图生视频/2048596027241930753.json, 视频生成/图生视频/2010692328301793282.json, 视频生成/图生视频/2008482127481933826.json, 视频生成/图生视频/2008532910646763522.json, 视频生成/图生视频/2008794813583331330.json, 视频生成/图生视频/2021544395123724290.json, 视频生成/图生视频/2019249142207352834.json, 视频生成/图生视频/2010611172453654529.json, 视频生成/图生视频/2009275287908913153.json, 视频生成/图生视频/2012538447445106690.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_14

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/2017463595512111106.json、视频生成/图生视频/2009155672465743874.json、视频生成/图生视频/2009919579048382465.json、视频生成/图生视频/2009073353373519874.json、视频生成/图生视频/2048596027241930753.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 14 个 workflow 都包含：
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
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 13/14 个有
- `VAEDecode` —— 12/14 个有
- `ResizeImagesByLongerEdge` —— 11/14 个有
- `PrimitiveInt` —— 10/14 个有
- `VHS_VideoCombine` —— 10/14 个有
- `ImageResizeKJv2` —— 9/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/14 个有
- `CR Text` —— 6/14 个有
- `MathExpression|pysssss` —— 6/14 个有
- `CreateVideo` —— 4/14 个有
- `Int` —— 4/14 个有
- `SaveVideo` —— 4/14 个有
- `DF_Int_to_Float` —— 3/14 个有
- `GetNode` —— 3/14 个有
- `JWInteger` —— 3/14 个有
- `PreviewImage` —— 3/14 个有
- `SetNode` —— 3/14 个有
- `VAEDecodeTiled` —— 3/14 个有
- `ImpactSwitch` —— 2/14 个有
- `PrimitiveFloat` —— 2/14 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `RH_LLMAPI_NODE` —— 1/14 个有
- `SaveImage` —— 1/14 个有
- `ShowText|pysssss` —— 1/14 个有
- `SimpleMath+` —— 1/14 个有
- `ToFloat` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 14 | 100% |
| 高度 | 25 | 25 - 25 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，14 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）
