---
name: unknown_workflow_upscale_latent_upscale_lora_33
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.954375
common_nodes: [Audio Duration (mtb), CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, Float, GetLatentSizeAndCount, JWImageResizeByLongerSide, KSamplerSelect, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SimpleMath+, SolidMask, Text, TrimAudioDuration, VAEDecodeTiled, easy showAnything, image_scale_pixel_v2]
problems: []
missing: []
members: [视频生成/图生视频/2057776210763149313.json, 视频生成/图生视频/2057371445994549250.json, 视频生成/图生视频/2051995691907596290.json, 视频生成/文生视频/2.5套件｜LTX2.3 单人数字人｜IC Edit 100%无字幕口播_2054453027771297794.json, 视频生成/文生视频/2.5套件｜LTX2.3 双人数字人｜IC Edit 100%无字幕对话_2054479470995755009.json, 视频生成/文生视频/For循环Ltx2.3长MV自动生成工作流_2055888057307549697.json, 视频生成/文生视频/LTX2.3 音频反应式动画工作流_2058938733910650882.json, 视频生成/文生视频/单人数字人3.0｜OmniNFT+Relay+蒸馏1.1｜音频驱动_2058190932108992514.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_33

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2057776210763149313.json、视频生成/图生视频/2057371445994549250.json、视频生成/图生视频/2051995691907596290.json、视频生成/文生视频/2.5套件｜LTX2.3 单人数字人｜IC Edit 100%无字幕口播_2054453027771297794.json、视频生成/文生视频/2.5套件｜LTX2.3 双人数字人｜IC Edit 100%无字幕对话_2054479470995755009.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `Audio Duration (mtb)`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `Float`
- `GetLatentSizeAndCount`
- `JWImageResizeByLongerSide`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SolidMask`
- `Text`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `easy showAnything`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 7/8 个有
- `Image To Mask` —— 7/8 个有
- `LTX2SamplingPreviewOverride` —— 7/8 个有
- `LTXAddVideoICLoRAGuide` —— 7/8 个有
- `LTXICLoRALoaderModelOnly` —— 7/8 个有
- `LTXVCropGuides` —— 7/8 个有
- `LayerUtility: ColorImage` —— 7/8 个有
- `PathchSageAttentionKJ` —— 7/8 个有
- `PromptRelayEncode` —— 7/8 个有
- `RepeatImageBatch` —— 7/8 个有
- `Seed (rgthree)` —— 7/8 个有
- `VAEEncodeForInpaint` —— 7/8 个有
- `easy imageCount` —— 7/8 个有
- `easy imageSize` —— 7/8 个有
- `SaveVideo` —— 6/8 个有
- `VHS_VideoCombine` —— 5/8 个有
- `JjkText` —— 4/8 个有
- `Seed Everywhere` —— 4/8 个有
- `VRAMReserver` —— 4/8 个有
- `ACE_AudioCrop` —— 2/8 个有
- `FloatToText` —— 2/8 个有
- `ImpactMakeImageBatch` —— 2/8 个有
- `Int` —— 2/8 个有
- `RH_RhartImageG2ImageToImage` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `String Literal` —— 2/8 个有
- `Text Load Line From File` —— 2/8 个有
- `easy batchAnything` —— 2/8 个有
- `easy forLoopEnd` —— 2/8 个有
- `easy forLoopStart` —— 2/8 个有
- `easy indexAnything` —— 2/8 个有
- `easy lengthAnything` —— 2/8 个有
- `RHHiddenNodes` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 8 | 100% |
| 高度 | 25 | 25 - 25 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，8 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
