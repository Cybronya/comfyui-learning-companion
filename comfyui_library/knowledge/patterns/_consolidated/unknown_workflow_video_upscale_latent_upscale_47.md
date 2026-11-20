---
name: unknown_workflow_video_upscale_latent_upscale_47
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.5285
common_nodes: [CLIPTextEncode, DiffusionModelLoaderKJ, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageFlip, ImageResizeKJv2, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ResizeImageMaskNode, SamplerCustom, Seed (rgthree), SetNode, SimpleMath+, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3  单图生视频高清工作流_2050424425325056002.json, 视频生成/图生视频/LTX 2.3  图生视频高清工作流_2058113991079190529.json, 视频生成/图生视频/LTX 2.3  首尾帧数字人高清工作流_2064957941442244609.json, 视频生成/图生视频/LTX 2.3  首尾帧高清工作流_2054364894450987010.json, 视频生成/图生视频/LTX 2.3 单图数字人高清工作流_2048020600035221506.json, 视频生成/图生视频/LTX2.3 数字人首尾帧 加入转场lora和Prompt Relay_2049132268295299073.json, 视频生成/图生视频/LTX2.3 高清 首尾帧 MV、数字人、唱歌、带货_2046973175417802754.json, 视频生成/图生视频/【Supermate】LTX 2.3  首尾帧数字人一次采样高清工作流_2057514932127752193.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_47

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3  单图生视频高清工作流_2050424425325056002.json、视频生成/图生视频/LTX 2.3  图生视频高清工作流_2058113991079190529.json、视频生成/图生视频/LTX 2.3  首尾帧数字人高清工作流_2064957941442244609.json、视频生成/图生视频/LTX 2.3  首尾帧高清工作流_2054364894450987010.json、视频生成/图生视频/LTX 2.3 单图数字人高清工作流_2048020600035221506.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageFlip`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ResizeImageMaskNode`
- `SamplerCustom`
- `Seed (rgthree)`
- `SetNode`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 6/8 个有
- `RH_LLMAPI_Pro_Node` —— 6/8 个有
- `ShowText|pysssss` —— 6/8 个有
- `TextInput_` —— 6/8 个有
- `AudioInfo` —— 5/8 个有
- `Display Any (rgthree)` —— 5/8 个有
- `LTXVAudioVAEEncode` —— 5/8 个有
- `LoadAudio` —— 5/8 个有
- `MelBandRoFormerModelLoader` —— 5/8 个有
- `MelBandRoFormerSampler` —— 5/8 个有
- `PreviewAudio` —— 5/8 个有
- `SetLatentNoiseMask` —— 5/8 个有
- `SolidMask` —— 5/8 个有
- `AudioCrop` —— 4/8 个有
- `LTX2SamplingPreviewOverride` —— 4/8 个有
- `ImageConcanate` —— 3/8 个有
- `LTXVAudioVAEDecode` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `SimpleCalculatorKJ` —— 3/8 个有
- `PromptRelayEncode` —— 2/8 个有
- `LTXVScheduler` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `MemoryCleaner` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 8 | 100% |
| 高度 | 24 | 24 - 24 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，8 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，8 个样本，取值集中（一致性 100%）
