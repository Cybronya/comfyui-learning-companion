---
name: unknown_workflow_video_sampler_clip_163
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.77675
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, TrimAudioDuration, UNETLoader, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/ltx2_s2v_2011018464567234562.json, 视频生成/图生视频/二次元数字人(LTX2.3新模型)_2044961246537060354.json, 视频生成/图生视频/数字人对口型LTX2.3稳定版数字_2044051743004172289.json, 视频生成/图生视频/（新版模型）LTX2.3稳定版数字人工作流_2044317825631784961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_163

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/ltx2_s2v_2011018464567234562.json、视频生成/图生视频/二次元数字人(LTX2.3新模型)_2044961246537060354.json、视频生成/图生视频/数字人对口型LTX2.3稳定版数字_2044051743004172289.json、视频生成/图生视频/（新版模型）LTX2.3稳定版数字人工作流_2044317825631784961.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `ComfySwitchNode` —— 3/4 个有
- `LTX2SamplingPreviewOverride` —— 3/4 个有
- `LTX2_NAG` —— 3/4 个有
- `LTXVEmptyLatentAudio` —— 3/4 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ManualSigmas` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `SaveAudio` —— 3/4 个有
- `SimpleCalculatorKJ` —— 3/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `Int` —— 1/4 个有
- `LTXVScheduler` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `VAEDecode` —— 1/4 个有

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
