---
name: unknown_workflow_upscale_latent_upscale_lora_36
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9241
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VRAMReserver, image_scale_pixel_v2]
problems: []
missing: []
members: [视频生成/文生视频/2.5套件｜LTX2.3 图生视频｜IC Edit 100%无字幕生成_2054434432525840386.json, 视频生成/文生视频/2.5套件｜LTX2.3 多图参考｜IC Edit 100%无字幕生成_2054535482951913473.json, 视频生成/文生视频/2.5套件｜LTX2.3 文生视频｜IC Edit 100%无字幕生成_2054455981848965122.json, 视频生成/文生视频/LTX 2.3 + VBVR 多图首尾帧_2043983802795560961.json, 视频生成/文生视频/LTX 2.3 一分四多图首尾帧 2.0｜Dev-Dare 四段接力增强版_2051714472196222977.json, 视频生成/文生视频/LTX 2.3 多图首尾帧 2.0｜Dev-Dare 三阶渲染增强版_2051714484946915330.json, 视频生成/文生视频/LTX 2.3 多图首尾帧 2.0｜三阶渲染·极致打磨『最优实现』_2050912405437333506.json, 视频生成/文生视频/图生视频3.0｜OmniNFT+Relay+蒸馏1.1｜一图成片_2058326590685274113.json, 视频生成/文生视频/多图参考3.0｜OmniNFT+Relay+蒸馏1.1｜多图融合_2058327091539701762.json, 视频生成/文生视频/文生视频3.0｜OmniNFT+Relay+蒸馏1.1｜三阶无字幕_2057671098963161090.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_36

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/2.5套件｜LTX2.3 图生视频｜IC Edit 100%无字幕生成_2054434432525840386.json、视频生成/文生视频/2.5套件｜LTX2.3 多图参考｜IC Edit 100%无字幕生成_2054535482951913473.json、视频生成/文生视频/2.5套件｜LTX2.3 文生视频｜IC Edit 100%无字幕生成_2054455981848965122.json、视频生成/文生视频/LTX 2.3 + VBVR 多图首尾帧_2043983802795560961.json、视频生成/文生视频/LTX 2.3 一分四多图首尾帧 2.0｜Dev-Dare 四段接力增强版_2051714472196222977.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2_NAG`
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
- `VRAMReserver`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 9/10 个有
- `PrimitiveBoolean` —— 9/10 个有
- `Seed Everywhere` —— 9/10 个有
- `Text` —— 9/10 个有
- `PromptRelayEncode` —— 7/10 个有
- `VHS_VideoCombine` —— 7/10 个有
- `GetImageRangeFromBatch` —— 6/10 个有
- `GetImageSize+` —— 6/10 个有
- `Image To Mask` —— 6/10 个有
- `ImageResizeKJv2` —— 6/10 个有
- `Int` —— 6/10 个有
- `JWImageSequenceExtractFromBatch` —— 6/10 个有
- `LTX2SamplingPreviewOverride` —— 6/10 个有
- `LTXAddVideoICLoRAGuide` —— 6/10 个有
- `LTXICLoRALoaderModelOnly` —— 6/10 个有
- `LTXVAddGuideMulti` —— 6/10 个有
- `LTXVCropGuides` —— 6/10 个有
- `LayerUtility: ColorImage` —— 6/10 个有
- `PathchSageAttentionKJ` —— 6/10 个有
- `PreviewImage` —— 6/10 个有
- `RepeatImageBatch` —— 6/10 个有
- `Seed (rgthree)` —— 6/10 个有
- `SimpleMath+` —— 6/10 个有
- `VAEEncodeForInpaint` —— 6/10 个有
- `easy imageCount` —— 6/10 个有
- `easy imageSize` —— 6/10 个有
- `easy showAnything` —— 6/10 个有
- `SaveVideo` —— 5/10 个有
- `DisTorchPurgeVRAMV2` —— 4/10 个有
- `Image_Resize_longsize` —— 4/10 个有
- `ResizeLongestToNode` —— 4/10 个有
- `PromptRelaySmartEncode` —— 2/10 个有
- `ImageCrop+` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `PromptRelayAdvancedOptions` —— 1/10 个有
- `SaveImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
