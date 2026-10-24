---
name: unknown_workflow_video_lora_sampler_392
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8986
common_nodes: [CLIPTextEncode, CM_BoolToInt, DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVSeparateAVLatent, LoadImage, Lora Loader Stack (rgthree), PathchSageAttentionKJ, PreviewImage, SamplerCustom, SimpleMath+, Switch image [Crystools], UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy isNone, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/ltx23-lock 多人对话_2105153996301365249.json, 视频生成/图生视频/LTX2.3多人对话_2055168345057570818.json, 视频生成/图生视频/LTX2.3多人对话_2056562094497161218.json, 视频生成/文生视频/LTX2.3 Single Sample V1.0（文生视频_图生视频_首尾帧视频）_2052259370225942529.json, 视频生成/文生视频/LTX2.3 Single Sample V2.0（文生视频_图生视频_首尾帧视频_数字人对口型）_2052670475729424385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_392

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/ltx23-lock 多人对话_2105153996301365249.json、视频生成/图生视频/LTX2.3多人对话_2055168345057570818.json、视频生成/图生视频/LTX2.3多人对话_2056562094497161218.json、视频生成/文生视频/LTX2.3 Single Sample V1.0（文生视频_图生视频_首尾帧视频）_2052259370225942529.json、视频生成/文生视频/LTX2.3 Single Sample V2.0（文生视频_图生视频_首尾帧视频_数字人对口型）_2052670475729424385.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CM_BoolToInt`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SamplerCustom`
- `SimpleMath+`
- `Switch image [Crystools]`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy isNone`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 3/5 个有
- `ManualSigmas` —— 3/5 个有
- `VisualizeSigmasKJ` —— 3/5 个有
- `CreateVideo` —— 2/5 个有
- `DualCLIPLoaderGGUF` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `LTXVAudioVAEEncode` —— 2/5 个有
- `LoadAudio` —— 2/5 个有
- `NormalizeAudioLoudness` —— 2/5 个有
- `PlaySound|pysssss` —— 2/5 个有
- `SaveVideo` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `UnetLoaderGGUF` —— 2/5 个有
- `VHS_SelectImages` —— 2/5 个有
- `AudioConcat` —— 1/5 个有
- `ComfySwitchNode` —— 1/5 个有
- `MelBandRoFormerModelLoader` —— 1/5 个有
- `MelBandRoFormerSampler` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `SetLatentNoiseMask` —— 1/5 个有
- `SolidMask` —— 1/5 个有
- `TrimAudioDuration` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 361 | 361 - 361 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 361，观测区间 361 - 361，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
