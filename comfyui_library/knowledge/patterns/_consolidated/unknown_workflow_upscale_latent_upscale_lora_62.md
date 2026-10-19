---
name: unknown_workflow_upscale_latent_upscale_lora_62
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.958
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTX2_NAG, LTXAVTextEncoderLoader, LTXFaceDetector, LTXICLoRALoaderModelOnly, LTXLatentAnchorAware, LTXLikenessAnchor, LTXLikenessGuide, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, PromptRelaySmartEncode, RandomNoise, STGGuiderAdvanced, SamplerCustomAdvanced, SaveVideo, Seed Everywhere, Sigmas Easing, Text, VAEDecodeTiled, VRAMReserver, image_scale_pixel_v2]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3 图文视频工作流｜图片参考 + 文本控制 + 10S相似度保持全流程_2061456734065094658.json, 视频生成/文生视频/LTX2.3 多图参考重大更新｜多图导入 + 10S相似度锁定，角色稳定不乱_2061671863138476034.json, 视频生成/文生视频/LTX2.3 文生视频 3.1｜三阶高清精修_2061480014171955202.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_62

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/LTX2.3 图文视频工作流｜图片参考 + 文本控制 + 10S相似度保持全流程_2061456734065094658.json、视频生成/文生视频/LTX2.3 多图参考重大更新｜多图导入 + 10S相似度锁定，角色稳定不乱_2061671863138476034.json、视频生成/文生视频/LTX2.3 文生视频 3.1｜三阶高清精修_2061480014171955202.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXFaceDetector`
- `LTXICLoRALoaderModelOnly`
- `LTXLatentAnchorAware`
- `LTXLikenessAnchor`
- `LTXLikenessGuide`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PromptRelaySmartEncode`
- `RandomNoise`
- `STGGuiderAdvanced`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `Seed Everywhere`
- `Sigmas Easing`
- `Text`
- `VAEDecodeTiled`
- `VRAMReserver`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `Image_Resize_longsize` —— 2/3 个有
- `LTXVImgToVideoConditionOnly` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `GetImageSize+` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `Int` —— 1/3 个有
- `JWImageSequenceExtractFromBatch` —— 1/3 个有
- `LTXVAddGuideMulti` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
