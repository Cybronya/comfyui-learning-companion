---
name: unknown_workflow_video_lora_sampler_604
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.429
common_nodes: [CLIPTextEncode, DiffusionModelLoaderKJ, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PromptRelayEncode, SamplerCustom, SetNode, SimpleCalculatorKJ, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2054364894450987010.json, 视频生成/图生视频/2054538928006410241.json, 视频生成/图生视频/2054535064364568577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_604

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2054364894450987010.json、视频生成/图生视频/2054538928006410241.json、视频生成/图生视频/2054535064364568577.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：43%

## 共有节点

全部 3 个 workflow 都包含：
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
- `PromptRelayEncode`
- `SamplerCustom`
- `SetNode`
- `SimpleCalculatorKJ`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `TTResolutionSelector` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageFlip` —— 1/3 个有
- `LTX2SamplingPreviewOverride` —— 1/3 个有
- `LTXVLatentUpsampler` —— 1/3 个有
- `LTXVPreprocess` —— 1/3 个有
- `LTXVScheduler` —— 1/3 个有
- `LatentUpscaleModelLoader` —— 1/3 个有
- `ResizeImageMaskNode` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 3 | 100% |
| 高度 | 30 | 24 - 30 | 3 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，3 个样本，取值集中（一致性 100%）
- 高度 中位数 30，观测区间 24 - 30，3 个样本，取值集中（一致性 90%）
