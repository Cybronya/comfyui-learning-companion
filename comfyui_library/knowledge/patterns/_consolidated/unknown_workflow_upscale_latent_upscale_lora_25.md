---
name: unknown_workflow_upscale_latent_upscale_lora_25
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.817727
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, image_scale_pixel_v2]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3 三采样采样策略 _ 图生视频画质拉满实战_2034501283566063617.json, 视频生成/图生视频/LTX 2.3 双人对话_2059861850040389633.json, 视频生成/图生视频/LTX 2.3 的 100% 实力释放三阶段采样图生视频工作流_2034800880725266433.json, 视频生成/图生视频/三采样提高质量LTX 2.3-图生视频-建议plus模式_2034238637155557377.json, 视频生成/图生视频/三采样提高质量LTX 2.3-图生视频-建议plus模式_2034906343454281730.json, 视频生成/文生视频/2.5套件｜LTX2.3 图生视频｜IC Edit 100%无字幕生成_2054434432525840386.json, 视频生成/文生视频/2.5套件｜LTX2.3 多图参考｜IC Edit 100%无字幕生成_2054535482951913473.json, 视频生成/文生视频/2.5套件｜LTX2.3 文生视频｜IC Edit 100%无字幕生成_2054455981848965122.json, 视频生成/文生视频/图生视频3.0｜OmniNFT+Relay+蒸馏1.1｜一图成片_2058326590685274113.json, 视频生成/文生视频/多图参考3.0｜OmniNFT+Relay+蒸馏1.1｜多图融合_2058327091539701762.json, 视频生成/文生视频/文生视频3.0｜OmniNFT+Relay+蒸馏1.1｜三阶无字幕_2057671098963161090.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_25

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3 三采样采样策略 _ 图生视频画质拉满实战_2034501283566063617.json、视频生成/图生视频/LTX 2.3 双人对话_2059861850040389633.json、视频生成/图生视频/LTX 2.3 的 100% 实力释放三阶段采样图生视频工作流_2034800880725266433.json、视频生成/图生视频/三采样提高质量LTX 2.3-图生视频-建议plus模式_2034238637155557377.json、视频生成/图生视频/三采样提高质量LTX 2.3-图生视频-建议plus模式_2034906343454281730.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 10/11 个有
- `SaveVideo` —— 10/11 个有
- `SimpleMath+` —— 10/11 个有
- `Text` —— 10/11 个有
- `Image_Resize_longsize` —— 9/11 个有
- `LTX2_NAG` —— 7/11 个有
- `PathchSageAttentionKJ` —— 7/11 个有
- `Seed Everywhere` —— 7/11 个有
- `VRAMReserver` —— 7/11 个有
- `GetImageRangeFromBatch` —— 6/11 个有
- `Image To Mask` —— 6/11 个有
- `LTX2SamplingPreviewOverride` —— 6/11 个有
- `LTXAddVideoICLoRAGuide` —— 6/11 个有
- `LTXICLoRALoaderModelOnly` —— 6/11 个有
- `LTXVCropGuides` —— 6/11 个有
- `LayerUtility: ColorImage` —— 6/11 个有
- `LayerUtility: PurgeVRAM V2` —— 6/11 个有
- `RepeatImageBatch` —— 6/11 个有
- `Seed (rgthree)` —— 6/11 个有
- `VAEEncodeForInpaint` —— 6/11 个有
- `easy imageCount` —— 6/11 个有
- `easy imageSize` —— 6/11 个有
- `DisTorchPurgeVRAMV2` —— 5/11 个有
- `PromptRelayEncode` —— 5/11 个有
- `GetNode` —— 3/11 个有
- `SetNode` —— 3/11 个有
- `VHS_VideoCombine` —— 3/11 个有
- `WujiCleaner` —— 3/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `GetImageSize+` —— 2/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `Int` —— 2/11 个有
- `JWImageSequenceExtractFromBatch` —— 2/11 个有
- `LTXVAddGuideMulti` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `PromptRelaySmartEncode` —— 2/11 个有
- `PromptRelayAdvancedOptions` —— 1/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `ZML_SplitText` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 11 | 100% |
| 高度 | 25 | 25 - 25 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，11 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
