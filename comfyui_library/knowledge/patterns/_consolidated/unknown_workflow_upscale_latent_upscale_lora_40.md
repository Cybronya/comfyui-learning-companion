---
name: unknown_workflow_upscale_latent_upscale_lora_40
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.84
common_nodes: [Any Switch (rgthree), Audio Duration (mtb), AudioCrop, CFGGuider, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, GetImageSize, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PreviewAny, PrimitiveBoolean, PrimitiveInt, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, Sigmas Rescale, SimpleMathDual+, SolidMask, VAEDecodeTiled, easy convertAnything, easy ifElse, easy positive]
problems: []
missing: []
members: [图片生成/文生图/QIANSUI+LTX2.3+图文生视频_2032449219776221185.json, 视频生成/图生视频/LTX 2.3 多帧生视频 电影级效果（支持音频传入）_2030925818993582082.json, 视频生成/图生视频/LTX2.3 图生视频 分镜成片高清无字幕  超强音频驱动数字人MV_2031738492585254914.json, 视频生成/图生视频/LTX2.3 超强音频数字人MV  支持文生_单_多帧Full版_2031034066862084097.json, 视频生成/图生视频/LTX2.3（蒸馏版）+Distilled1.1+图文音频生视频_2045119325643743233.json, 视频生成/图生视频/LTX2.3（蒸馏版）+Distilled1.1+图文音频生视频工作流 V2.0_2045304246991593473.json, 视频生成/文生视频/LTX2.3 文_图_音_生视频 1080P 多合一_2030698400957603841.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_40

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/QIANSUI+LTX2.3+图文生视频_2032449219776221185.json、视频生成/图生视频/LTX 2.3 多帧生视频 电影级效果（支持音频传入）_2030925818993582082.json、视频生成/图生视频/LTX2.3 图生视频 分镜成片高清无字幕  超强音频驱动数字人MV_2031738492585254914.json、视频生成/图生视频/LTX2.3 超强音频数字人MV  支持文生_单_多帧Full版_2031034066862084097.json、视频生成/图生视频/LTX2.3（蒸馏版）+Distilled1.1+图文音频生视频_2045119325643743233.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Audio Duration (mtb)`
- `AudioCrop`
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `Sigmas Rescale`
- `SimpleMathDual+`
- `SolidMask`
- `VAEDecodeTiled`
- `easy convertAnything`
- `easy ifElse`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 6/7 个有
- `LTXVAudioVAELoader` —— 6/7 个有
- `LTXVEnhanceAVideoKJ` —— 6/7 个有
- `easy float` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 4/7 个有
- `ResizeImagesByShorterEdge` —— 4/7 个有
- `easy int` —— 4/7 个有
- `CM_IntToFloat` —— 3/7 个有
- `GetNode` —— 3/7 个有
- `ImageBatchMulti` —— 3/7 个有
- `LTXVAddGuideMulti` —— 3/7 个有
- `PrimitiveString` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `SimpleMath+` —— 3/7 个有
- `TextSplitByDelimiter` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `easy batchAnything` —— 3/7 个有
- `easy forLoopEnd` —— 3/7 个有
- `easy forLoopStart` —— 3/7 个有
- `easy imagesSplitImage` —— 3/7 个有
- `easy indexAnything` —— 3/7 个有
- `easy lengthAnything` —— 3/7 个有
- `图像缩放V2_孤海` —— 3/7 个有
- `LTX2SamplingPreviewOverride` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `DeepTranslatorTextNode` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `UNETLoader` —— 1/7 个有
- `VAELoader` —— 1/7 个有
- `easy anythingIndexSwitch` —— 1/7 个有
- `easy blocker` —— 1/7 个有
- `easy compare` —— 1/7 个有
- `easy mathInt` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
