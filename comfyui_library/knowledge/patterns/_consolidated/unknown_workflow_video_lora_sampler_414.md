---
name: unknown_workflow_video_lora_sampler_414
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7014
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LTXVSpatioTemporalTiledVAEDecode, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SolidMask, UNETLoader, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2044784831422275586.json, 视频生成/图生视频/2050231422836846593.json, 视频生成/图生视频/2043896242345877506.json, 视频生成/图生视频/2046132388467580929.json, 视频生成/图生视频/2044579812215361538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_414

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2044784831422275586.json、视频生成/图生视频/2050231422836846593.json、视频生成/图生视频/2043896242345877506.json、视频生成/图生视频/2046132388467580929.json、视频生成/图生视频/2044579812215361538.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SolidMask`
- `UNETLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/5 个有
- `TrimAudioDuration` —— 4/5 个有
- `GetImageSize` —— 3/5 个有
- `LTXVEmptyLatentAudio` —— 3/5 个有
- `SaveAudio` —— 3/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `PreviewAudio` —— 2/5 个有
- `SigmasPreview` —— 2/5 个有
- `llama_cpp_instruct_adv` —— 2/5 个有
- `llama_cpp_model_loader` —— 2/5 个有
- `llama_cpp_parameters` —— 2/5 个有
- `AudioCrop` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `Display Any (rgthree)` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Float` —— 1/5 个有
- `LTXVImgToVideoConditionOnly` —— 1/5 个有
- `LTXVLatentUpsampler` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LatentUpscaleModelLoader` —— 1/5 个有
- `Mute / Bypass Relay (rgthree)` —— 1/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/5 个有
- `PreviewTextNode` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 3 | 100% |
| 高度 | 24 | 24 - 24 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，3 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，3 个样本，取值集中（一致性 100%）
