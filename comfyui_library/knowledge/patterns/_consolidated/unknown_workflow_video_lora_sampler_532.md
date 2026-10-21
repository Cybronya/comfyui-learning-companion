---
name: unknown_workflow_video_lora_sampler_532
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7645
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, ComfySwitchNode, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LTXVSpatioTemporalTiledVAEDecode, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveAudio, SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SolidMask, TrimAudioDuration, UNETLoader, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2044304245054246914.json, 视频生成/图生视频/2044961246537060354.json, 视频生成/图生视频/2044051743004172289.json, 视频生成/图生视频/2044317825631784961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_532

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2044304245054246914.json、视频生成/图生视频/2044961246537060354.json、视频生成/图生视频/2044051743004172289.json、视频生成/图生视频/2044317825631784961.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `ComfySwitchNode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
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
- `SaveAudio`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `LTXVEmptyLatentAudio` —— 3/4 个有
- `Int` —— 2/4 个有
- `AudioInfoNode` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

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
