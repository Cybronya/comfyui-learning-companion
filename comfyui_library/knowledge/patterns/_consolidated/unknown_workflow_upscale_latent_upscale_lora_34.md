---
name: unknown_workflow_upscale_latent_upscale_lora_34
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7842
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3 三采样采样策略 _ 图生视频画质拉满实战_2034501283566063617.json, 视频生成/图生视频/LTX 2.3 双人对话_2059861850040389633.json, 视频生成/图生视频/LTX 2.3 的 100% 实力释放三阶段采样图生视频工作流_2034800880725266433.json, 视频生成/图生视频/三采样提高质量LTX 2.3-图生视频-建议plus模式_2034238637155557377.json, 视频生成/图生视频/三采样提高质量LTX 2.3-图生视频-建议plus模式_2034906343454281730.json, 视频生成/图生视频/电商海报配音广告，电商产品海报叫卖，图加配音 数字人带货_2051995691907596290.json, 视频生成/图生视频/视频-图片对音频口型单人-LTX2.3-VBVR_2055146860268015617.json, 视频生成/图生视频/视频-图片对音频口型双人-LTX2.3-VBVR_2055152472892690433.json, 视频生成/图生视频/视频-图生视频扩写-LTX2.3-VBVR_2054821497482555394.json, 视频生成/文生视频/视频-文生视频扩写-LTX2.3-VBVR_2054821471918272513.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_34

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3 三采样采样策略 _ 图生视频画质拉满实战_2034501283566063617.json、视频生成/图生视频/LTX 2.3 双人对话_2059861850040389633.json、视频生成/图生视频/LTX 2.3 的 100% 实力释放三阶段采样图生视频工作流_2034800880725266433.json、视频生成/图生视频/三采样提高质量LTX 2.3-图生视频-建议plus模式_2034238637155557377.json、视频生成/图生视频/三采样提高质量LTX 2.3-图生视频-建议plus模式_2034906343454281730.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 10 个 workflow 都包含：
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
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `Text` —— 9/10 个有
- `Image_Resize_longsize` —— 7/10 个有
- `SetNode` —— 7/10 个有
- `SimpleMath+` —— 7/10 个有
- `LTX2_NAG` —— 6/10 个有
- `LayerUtility: PurgeVRAM V2` —— 6/10 个有
- `Seed Everywhere` —— 6/10 个有
- `easy showAnything` —— 6/10 个有
- `image_scale_pixel_v2` —— 6/10 个有
- `GetNode` —— 5/10 个有
- `VRAMReserver` —— 5/10 个有
- `easy int` —— 5/10 个有
- `GetImageSizeAndCount` —— 4/10 个有
- `ImageScaleBy` —— 4/10 个有
- `Int` —— 4/10 个有
- `JWFloatToString` —— 4/10 个有
- `MemoryCleaner` —— 4/10 个有
- `PromptRelaySmartEncode` —— 4/10 个有
- `RH_LLMAPI_NODE` —— 4/10 个有
- `StringFunction|pysssss` —— 4/10 个有
- `easy anythingIndexSwitch` —— 4/10 个有
- `easy positive` —— 4/10 个有
- `easy seed` —— 4/10 个有
- `Audio Duration (mtb)` —— 3/10 个有
- `DisTorchPurgeVRAMV2` —— 3/10 个有
- `Float` —— 3/10 个有
- `GetLatentSizeAndCount` —— 3/10 个有
- `JWImageResizeByLongerSide` —— 3/10 个有
- `LTXVAudioVAEEncode` —— 3/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `LoadAudio` —— 3/10 个有
- `MelBandRoFormerModelLoader` —— 3/10 个有
- `MelBandRoFormerSampler` —— 3/10 个有
- `Qwen3_VQA_Plus` —— 3/10 个有
- `SetLatentNoiseMask` —— 3/10 个有
- `SolidMask` —— 3/10 个有
- `TrimAudioDuration` —— 3/10 个有
- `WujiCleaner` —— 3/10 个有
- `easy cleanGpuUsed` —— 3/10 个有
- `easy saveText` —— 3/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `PathchSageAttentionKJ` —— 2/10 个有
- `Qwen3ASRLoader_DFT` —— 2/10 个有
- `Qwen3ASRTranscribe_DFT` —— 2/10 个有
- `ImageResizeKJv2` —— 1/10 个有
- `PromptRelayEncode` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `ZML_SplitText` —— 1/10 个有

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
