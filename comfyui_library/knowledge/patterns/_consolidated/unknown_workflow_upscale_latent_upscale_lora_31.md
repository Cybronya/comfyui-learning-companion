---
name: unknown_workflow_upscale_latent_upscale_lora_31
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9564
common_nodes: [Audio Duration (mtb), CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, Float, GetLatentSizeAndCount, JWImageResizeByLongerSide, KSamplerSelect, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SimpleMath+, SolidMask, TrimAudioDuration, VAEDecodeTiled, image_scale_pixel_v2]
problems: []
missing: []
members: [图片生成/文生图/Anima Edit 图像编辑工作流_2060760904450535425.json, 图片生成/文生图/LTX 2.3-1.1 + VBVR 数字人_2045068946071621633.json, 数字人/数字人/LTX2.3 3.5套件｜头像开口·单人数字人口播唱歌音频驱动_2068714653911445505.json, 视频生成/图生视频/2.5套件｜LTX2.3 双人数字人｜IC Edit 100%无字幕对话_2057776210763149313.json, 视频生成/图生视频/For循环Ltx2.3长MV自动生成工作流_2057371445994549250.json, 视频生成/文生视频/2.5套件｜LTX2.3 单人数字人｜IC Edit 100%无字幕口播_2054453027771297794.json, 视频生成/文生视频/2.5套件｜LTX2.3 双人数字人｜IC Edit 100%无字幕对话_2054479470995755009.json, 视频生成/文生视频/For循环Ltx2.3长MV自动生成工作流_2055888057307549697.json, 视频生成/文生视频/LTX2.3 音频反应式动画工作流_2058938733910650882.json, 视频生成/文生视频/单人数字人3.0｜OmniNFT+Relay+蒸馏1.1｜音频驱动_2058190932108992514.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_31

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Anima Edit 图像编辑工作流_2060760904450535425.json、图片生成/文生图/LTX 2.3-1.1 + VBVR 数字人_2045068946071621633.json、数字人/数字人/LTX2.3 3.5套件｜头像开口·单人数字人口播唱歌音频驱动_2068714653911445505.json、视频生成/图生视频/2.5套件｜LTX2.3 双人数字人｜IC Edit 100%无字幕对话_2057776210763149313.json、视频生成/图生视频/For循环Ltx2.3长MV自动生成工作流_2057371445994549250.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 10 个 workflow 都包含：
- `Audio Duration (mtb)`
- `CFGGuider`
- `CLIPTextEncode`
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
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
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
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 9/10 个有
- `LTXICLoRALoaderModelOnly` —— 9/10 个有
- `LTXVEmptyLatentAudio` —— 9/10 个有
- `LayerUtility: PurgeVRAM V2` —— 9/10 个有
- `PathchSageAttentionKJ` —— 9/10 个有
- `PromptRelayEncode` —— 9/10 个有
- `Text` —— 9/10 个有
- `easy showAnything` —— 9/10 个有
- `GetImageRangeFromBatch` —— 8/10 个有
- `Image To Mask` —— 8/10 个有
- `LTX2SamplingPreviewOverride` —— 8/10 个有
- `LTXAddVideoICLoRAGuide` —— 8/10 个有
- `LTXVCropGuides` —— 8/10 个有
- `LayerUtility: ColorImage` —— 8/10 个有
- `RepeatImageBatch` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `Seed (rgthree)` —— 8/10 个有
- `VAEEncodeForInpaint` —— 8/10 个有
- `easy imageCount` —— 8/10 个有
- `easy imageSize` —— 8/10 个有
- `JjkText` —— 6/10 个有
- `VHS_VideoCombine` —— 6/10 个有
- `VRAMReserver` —— 4/10 个有
- `Seed Everywhere` —— 3/10 个有
- `ACE_AudioCrop` —— 2/10 个有
- `FloatToText` —— 2/10 个有
- `ImpactMakeImageBatch` —— 2/10 个有
- `Int` —— 2/10 个有
- `RH_RhartImageG2ImageToImage` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `String Literal` —— 2/10 个有
- `Text Load Line From File` —— 2/10 个有
- `easy batchAnything` —— 2/10 个有
- `easy forLoopEnd` —— 2/10 个有
- `easy forLoopStart` —— 2/10 个有
- `easy indexAnything` —— 2/10 个有
- `easy lengthAnything` —— 2/10 个有
- `ImageFromBatch` —— 1/10 个有
- `LTXFaceDetector` —— 1/10 个有
- `LTXLatentAnchorAware` —— 1/10 个有
- `LTXLikenessAnchor` —— 1/10 个有
- `LTXLikenessGuide` —— 1/10 个有
- `STGGuiderAdvanced` —— 1/10 个有
- `Sigmas Easing` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 9 | 100% |
| 高度 | 25 | 25 - 25 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，9 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，9 个样本，取值集中（一致性 100%）
