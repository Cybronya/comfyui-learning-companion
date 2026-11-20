---
name: unknown_workflow_video_lora_sampler_853
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.396
common_nodes: [CLIPTextEncode, DiffusionModelLoaderKJ, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PreviewImage, PrimitiveFloat, PromptRelayEncode, SamplerCustom, SetNode, SimpleCalculatorKJ, TTResolutionSelector, Text Multiline, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3单图生视频_2054538928006410241.json, 视频生成/图生视频/LTX2.3首尾帧生视频_2054535064364568577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_853

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX2.3单图生视频_2054538928006410241.json、视频生成/图生视频/LTX2.3首尾帧生视频_2054535064364568577.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：40%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveFloat`
- `PromptRelayEncode`
- `SamplerCustom`
- `SetNode`
- `SimpleCalculatorKJ`
- `TTResolutionSelector`
- `Text Multiline`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | - | 2 | 100% |
| 高度 | 30 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
