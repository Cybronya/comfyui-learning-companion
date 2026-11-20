---
name: unknown_workflow_upscale_latent_upscale_lora_26
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.899727
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [图片生成/文生图/LTX2.3 3.5系列套件｜三阶高清文生视频_2067477095336464386.json, 视频生成/图生视频/3图参考_2057833759952687106.json, 视频生成/图生视频/LTX 2.3 三阶段采样四图首尾帧工作流_2036624444684247042.json, 视频生成/图生视频/LTX 2.3 的 100% 实力释放三阶段采样多图首尾帧工作流_2034914796595847170.json, 视频生成/图生视频/LTX2.3 多图参考生视频_2061938954978553858.json, 视频生成/图生视频/LTX2.3+文生视频+3.1｜三阶高清精修_2062353588676030465.json, 视频生成/文生视频/3图参考_2052698977556021250.json, 视频生成/文生视频/4图参考_2052698989765644290.json, 视频生成/文生视频/4图参考音频驱动_2052700211776110593.json, 视频生成/文生视频/LTX2.3 3.5系列套件｜首帧高相似视频_2067652016737968129.json, 视频生成/文生视频/LTX2.3 多图参考重大更新｜多图导入 + 10S相似度锁定，角色稳定不乱_2061671863138476034.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_26

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/LTX2.3 3.5系列套件｜三阶高清文生视频_2067477095336464386.json、视频生成/图生视频/3图参考_2057833759952687106.json、视频生成/图生视频/LTX 2.3 三阶段采样四图首尾帧工作流_2036624444684247042.json、视频生成/图生视频/LTX 2.3 的 100% 实力释放三阶段采样多图首尾帧工作流_2034914796595847170.json、视频生成/图生视频/LTX2.3 多图参考生视频_2061938954978553858.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：90%

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
- `LTXVPreprocess` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `image_scale_pixel_v2` —— 10/11 个有
- `LTX2_NAG` —— 9/11 个有
- `LTXVImgToVideoConditionOnly` —— 9/11 个有
- `PrimitiveBoolean` —— 9/11 个有
- `Seed Everywhere` —— 9/11 个有
- `Text` —— 9/11 个有
- `VRAMReserver` —— 9/11 个有
- `GetImageSize+` —— 8/11 个有
- `ImageResizeKJv2` —— 8/11 个有
- `JWImageSequenceExtractFromBatch` —— 8/11 个有
- `LTXVAddGuideMulti` —— 8/11 个有
- `PromptRelaySmartEncode` —— 7/11 个有
- `VHS_VideoCombine` —— 7/11 个有
- `Int` —— 6/11 个有
- `PreviewImage` —— 6/11 个有
- `easy showAnything` —— 6/11 个有
- `STGGuiderAdvanced` —— 5/11 个有
- `SaveVideo` —— 5/11 个有
- `Sigmas Easing` —— 5/11 个有
- `LTXFaceDetector` —— 4/11 个有
- `LTXLatentAnchorAware` —— 4/11 个有
- `LTXLikenessAnchor` —— 4/11 个有
- `LTXLikenessGuide` —— 4/11 个有
- `LayerUtility: PurgeVRAM V2` —— 4/11 个有
- `PromptRelayAdvancedOptions` —— 4/11 个有
- `PromptRelayEncodeTimeline` —— 4/11 个有
- `SimpleMath+` —— 4/11 个有
- `LTXICLoRALoaderModelOnly` —— 3/11 个有
- `Image_Resize_longsize` —— 2/11 个有
- `LTXVAudioVAEEncode` —— 2/11 个有
- `LoadAudio` —— 2/11 个有
- `ResizeImageMaskNode` —— 2/11 个有
- `ResizeLongestToNode` —— 2/11 个有
- `Audio Duration (mtb)` —— 1/11 个有
- `DF_Integer` —— 1/11 个有
- `Float` —— 1/11 个有
- `GetLatentSizeAndCount` —— 1/11 个有
- `JWInteger` —— 1/11 个有
- `MelBandRoFormerModelLoader` —— 1/11 个有
- `MelBandRoFormerSampler` —— 1/11 个有
- `SetLatentNoiseMask` —— 1/11 个有
- `SolidMask` —— 1/11 个有
- `TextBox` —— 1/11 个有
- `TrimAudioDuration` —— 1/11 个有
- `easy mathInt` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 11 | 93% |
| 高度 | 25 | 25 - 25 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，11 个样本，取值集中（一致性 93%）
- 高度 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
