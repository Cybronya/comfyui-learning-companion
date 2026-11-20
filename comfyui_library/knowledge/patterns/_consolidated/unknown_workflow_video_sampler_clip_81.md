---
name: unknown_workflow_video_sampler_clip_81
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.779375
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVSpatioTemporalTiledVAEDecode, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/LTX2.3-数字人-Distilled-1.1-蒸馏稳定版-避免字幕-数字人-对口型_2045492864917970946.json, 数字人/数字人/LTX2.3数字人_2046490310024372225.json, 数字人/数字人/LTX2.3数字人【 超稳版 + 无字幕 】_2046462637571051521.json, 视频生成/图生视频/LTX2.3-数字人-自定义音频图像(抖音复现)_2044784831422275586.json, 视频生成/图生视频/LTX2.3-音频数字人(双采样高清版)_2050231422836846593.json, 视频生成/图生视频/LTX2.3稳定版数字人（新版模型）_2043896242345877506.json, 视频生成/图生视频/LTX2.3稳定版数字人（新版模型）_2046132388467580929.json, 视频生成/图生视频/LTX2.3稳定版数字人（最新版模型）_2044579812215361538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_81

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/LTX2.3-数字人-Distilled-1.1-蒸馏稳定版-避免字幕-数字人-对口型_2045492864917970946.json、数字人/数字人/LTX2.3数字人_2046490310024372225.json、数字人/数字人/LTX2.3数字人【 超稳版 + 无字幕 】_2046462637571051521.json、视频生成/图生视频/LTX2.3-数字人-自定义音频图像(抖音复现)_2044784831422275586.json、视频生成/图生视频/LTX2.3-音频数字人(双采样高清版)_2050231422836846593.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 7/8 个有
- `GetNode` —— 7/8 个有
- `INTConstant` —— 7/8 个有
- `LTXVAudioVAEDecode` —— 7/8 个有
- `LTXVPreprocess` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `SimpleCalculatorKJ` —— 7/8 个有
- `TrimAudioDuration` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `LTXVEmptyLatentAudio` —— 5/8 个有
- `SaveAudio` —— 5/8 个有
- `GetImageSize` —— 4/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `PreviewAudio` —— 2/8 个有
- `SigmasPreview` —— 2/8 个有
- `llama_cpp_instruct_adv` —— 2/8 个有
- `llama_cpp_model_loader` —— 2/8 个有
- `llama_cpp_parameters` —— 2/8 个有
- `AudioCrop` —— 1/8 个有
- `CR Prompt Text` —— 1/8 个有
- `CustomAddLabel` —— 1/8 个有
- `Display Any (rgthree)` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Float` —— 1/8 个有
- `Int` —— 1/8 个有
- `LTXVImgToVideoConditionOnly` —— 1/8 个有
- `LTXVLatentUpsampler` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LatentUpscaleModelLoader` —— 1/8 个有
- `Mute / Bypass Relay (rgthree)` —— 1/8 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/8 个有
- `PreviewTextNode` —— 1/8 个有
- `Primitive integer [Crystools]` —— 1/8 个有
- `PrimitiveBoolean` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 5 | 100% |
| 高度 | 24 | 24 - 24 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，5 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，5 个样本，取值集中（一致性 100%）
