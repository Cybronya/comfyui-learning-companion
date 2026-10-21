---
name: unknown_workflow_upscale_latent_upscale_lora_24
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.902182
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [图片生成/文生图/LTX2.3 3.5系列套件｜三阶高清文生视频_2067477095336464386.json, 视频生成/图生视频/2057833759952687106.json, 视频生成/图生视频/2036624444684247042.json, 视频生成/图生视频/2034914796595847170.json, 视频生成/图生视频/2061938954978553858.json, 视频生成/图生视频/2062353588676030465.json, 视频生成/文生视频/3图参考_2052698977556021250.json, 视频生成/文生视频/4图参考_2052698989765644290.json, 视频生成/文生视频/4图参考音频驱动_2052700211776110593.json, 视频生成/文生视频/LTX2.3 3.5系列套件｜首帧高相似视频_2067652016737968129.json, 视频生成/文生视频/LTX2.3 单人数字人工作流｜新增10S相似度保持，口播、唱歌、角色一致性一套跑通_2061362758670708737.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_24

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/LTX2.3 3.5系列套件｜三阶高清文生视频_2067477095336464386.json、视频生成/图生视频/2057833759952687106.json、视频生成/图生视频/2036624444684247042.json、视频生成/图生视频/2034914796595847170.json、视频生成/图生视频/2061938954978553858.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 10/11 个有
- `LTXVEmptyLatentAudio` —— 10/11 个有
- `LTXVImgToVideoConditionOnly` —— 10/11 个有
- `LTXVPreprocess` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `PrimitiveBoolean` —— 10/11 个有
- `image_scale_pixel_v2` —— 10/11 个有
- `LTX2_NAG` —— 9/11 个有
- `Text` —— 9/11 个有
- `Seed Everywhere` —— 8/11 个有
- `VRAMReserver` —— 8/11 个有
- `GetImageSize+` —— 7/11 个有
- `ImageResizeKJv2` —— 7/11 个有
- `JWImageSequenceExtractFromBatch` —— 7/11 个有
- `LTXVAddGuideMulti` —— 7/11 个有
- `VHS_VideoCombine` —— 7/11 个有
- `PreviewImage` —— 6/11 个有
- `PromptRelaySmartEncode` —— 6/11 个有
- `easy showAnything` —— 6/11 个有
- `Int` —— 5/11 个有
- `STGGuiderAdvanced` —— 5/11 个有
- `SaveVideo` —— 5/11 个有
- `Sigmas Easing` —— 5/11 个有
- `SimpleMath+` —— 5/11 个有
- `LTXFaceDetector` —— 4/11 个有
- `LTXLatentAnchorAware` —— 4/11 个有
- `LTXLikenessAnchor` —— 4/11 个有
- `LTXLikenessGuide` —— 4/11 个有
- `LayerUtility: PurgeVRAM V2` —— 4/11 个有
- `PromptRelayAdvancedOptions` —— 4/11 个有
- `PromptRelayEncodeTimeline` —— 4/11 个有
- `LTXICLoRALoaderModelOnly` —— 3/11 个有
- `LTXVAudioVAEEncode` —— 3/11 个有
- `LoadAudio` —— 3/11 个有
- `Audio Duration (mtb)` —— 2/11 个有
- `Float` —— 2/11 个有
- `GetLatentSizeAndCount` —— 2/11 个有
- `Image_Resize_longsize` —— 2/11 个有
- `MelBandRoFormerModelLoader` —— 2/11 个有
- `MelBandRoFormerSampler` —— 2/11 个有
- `ResizeImageMaskNode` —— 2/11 个有
- `ResizeLongestToNode` —— 2/11 个有
- `SetLatentNoiseMask` —— 2/11 个有
- `SolidMask` —— 2/11 个有
- `TrimAudioDuration` —— 2/11 个有
- `DF_Integer` —— 1/11 个有
- `JWImageResizeByLongerSide` —— 1/11 个有
- `JWInteger` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `PromptRelayEncode` —— 1/11 个有
- `TextBox` —— 1/11 个有
- `easy mathInt` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 10 | 93% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，10 个样本，取值集中（一致性 93%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
