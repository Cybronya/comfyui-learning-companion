---
name: unknown_workflow_upscale_latent_upscale_lora_12
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.961375
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled, image_scale_pixel_v2]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜Dev-Dare 三阶渲染增强版_2051714493138382849.json, 视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜三阶渲染·极致打磨『最优实现』无音频版_2050915982742433793.json, 视频生成/文生视频/LTX 2.3 图片+音频数字人 2.0｜Dev-Dare 音画驱动增强版_2051714450033524738.json, 视频生成/文生视频/LTX 2.3 图生视频 2.0｜Dev-Dare 三阶渲染增强版_2051714465686667266.json, 视频生成/文生视频/LTX 2.3 的 100% 实力释放图生视频三阶段采样工作流_2034922243968471041.json, 视频生成/文生视频/LTX-2.3三阶渲染1+3数字人100%性能释放_2034922238251634690.json, 视频生成/文生视频/LTX-2三阶渲染1+3数字人100%性能释放_2034922123667447810.json, 视频生成/文生视频/LTX2.3 单人数字人工作流｜新增10S相似度保持，口播、唱歌、角色一致性一套跑通_2061362758670708737.json, 视频生成/文生视频/LTX2.3 图文视频工作流｜图片参考 + 文本控制 + 10S相似度保持全流程_2061456734065094658.json, 视频生成/文生视频/LTX2.3 文生视频 3.1｜三阶高清精修_2061480014171955202.json, 视频生成/文生视频/VBVR数字人_2043983796604768258.json, 视频生成/文生视频/『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：高概率数字人最优_2047657281310953473.json, 视频生成/文生视频/『最优实现』LTX 2.3 音频驱动双人对话生产力方案_2048727975096487938.json, 视频生成/文生视频/图片+音频数字人 2.0｜Dev-Dare + VBVR 最终版_2051722678544941058.json, 视频生成/文生视频/图片+音频驱动数字人 对比｜Distilled + Dev-Dare + VAVR 三模实测_2051704448384282626.json, 视频生成/文生视频/音频数字人 2.0｜三阶渲染打磨版，人物说话更自然_2050906015968837633.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_12

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜Dev-Dare 三阶渲染增强版_2051714493138382849.json、视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜三阶渲染·极致打磨『最优实现』无音频版_2050915982742433793.json、视频生成/文生视频/LTX 2.3 图片+音频数字人 2.0｜Dev-Dare 音画驱动增强版_2051714450033524738.json、视频生成/文生视频/LTX 2.3 图生视频 2.0｜Dev-Dare 三阶渲染增强版_2051714465686667266.json、视频生成/文生视频/LTX 2.3 的 100% 实力释放图生视频三阶段采样工作流_2034922243968471041.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 16 个 workflow 都包含：
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
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 15/16 个有
- `LTXVEmptyLatentAudio` —— 15/16 个有
- `LTX2_NAG` —— 13/16 个有
- `Audio Duration (mtb)` —— 11/16 个有
- `GetLatentSizeAndCount` —— 11/16 个有
- `JWImageResizeByLongerSide` —— 11/16 个有
- `LTXVAudioVAEEncode` —— 11/16 个有
- `LoadAudio` —— 11/16 个有
- `MelBandRoFormerModelLoader` —— 11/16 个有
- `MelBandRoFormerSampler` —— 11/16 个有
- `SetLatentNoiseMask` —— 11/16 个有
- `SolidMask` —— 11/16 个有
- `TrimAudioDuration` —— 11/16 个有
- `VRAMReserver` —— 11/16 个有
- `LayerUtility: PurgeVRAM V2` —— 10/16 个有
- `SimpleMath+` —— 10/16 个有
- `PromptRelayEncode` —— 9/16 个有
- `Seed Everywhere` —— 9/16 个有
- `Float` —— 8/16 个有
- `Text` —— 8/16 个有
- `easy showAnything` —— 7/16 个有
- `Image_Resize_longsize` —— 5/16 个有
- `DisTorchPurgeVRAMV2` —— 3/16 个有
- `LTXFaceDetector` —— 3/16 个有
- `LTXICLoRALoaderModelOnly` —— 3/16 个有
- `LTXLatentAnchorAware` —— 3/16 个有
- `LTXLikenessAnchor` —— 3/16 个有
- `LTXLikenessGuide` —— 3/16 个有
- `STGGuiderAdvanced` —— 3/16 个有
- `Sigmas Easing` —— 3/16 个有
- `SimpleCalculatorKJ` —— 3/16 个有
- `KepStringLiteral` —— 2/16 个有
- `PathchSageAttentionKJ` —— 2/16 个有
- `PromptRelaySmartEncode` —— 2/16 个有
- `INTConstant` —— 1/16 个有
- `JjkText` —— 1/16 个有
- `SetNode` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 15 | 100% |
| 高度 | 25 | 25 - 25 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，15 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，15 个样本，取值集中（一致性 100%）
