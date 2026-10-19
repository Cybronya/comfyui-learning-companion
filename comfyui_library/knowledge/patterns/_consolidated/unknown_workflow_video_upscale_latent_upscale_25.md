---
name: unknown_workflow_video_upscale_latent_upscale_25
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.505462
common_nodes: [CLIPTextEncode, DiffusionModelLoaderKJ, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ResizeImageMaskNode, SamplerCustom, Seed (rgthree), SetNode, SimpleMath+, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/LTX 2.3  单图数字人_2086755632165769217.json, 数字人/数字人/LTX2.3+（图+音频）数字人口播+高清优化版工作流_2083406138854428674.json, 视频生成/图生视频/2072957704288694274.json, 视频生成/图生视频/2050424425325056002.json, 视频生成/图生视频/2072578791876161538.json, 视频生成/图生视频/2058113991079190529.json, 视频生成/图生视频/2047852790181011458.json, 视频生成/图生视频/2046223171501694978.json, 视频生成/图生视频/2064957941442244609.json, 视频生成/图生视频/2048020600035221506.json, 视频生成/图生视频/2049132268295299073.json, 视频生成/图生视频/2046973175417802754.json, 视频生成/图生视频/2057514932127752193.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_25

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（数字人/数字人/LTX 2.3  单图数字人_2086755632165769217.json、数字人/数字人/LTX2.3+（图+音频）数字人口播+高清优化版工作流_2083406138854428674.json、视频生成/图生视频/2072957704288694274.json、视频生成/图生视频/2050424425325056002.json、视频生成/图生视频/2072578791876161538.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：51%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
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
- `ImageResizeKJv2` —— 12/13 个有
- `AudioInfo` —— 11/13 个有
- `ImageFlip` —— 11/13 个有
- `LTXVAudioVAEEncode` —— 11/13 个有
- `LoadAudio` —— 11/13 个有
- `MelBandRoFormerModelLoader` —— 11/13 个有
- `MelBandRoFormerSampler` —— 11/13 个有
- `SetLatentNoiseMask` —— 11/13 个有
- `SolidMask` —— 11/13 个有
- `Display Any (rgthree)` —— 10/13 个有
- `PreviewAudio` —— 10/13 个有
- `Fast Groups Bypasser (rgthree)` —— 9/13 个有
- `RH_LLMAPI_Pro_Node` —— 9/13 个有
- `ShowText|pysssss` —— 9/13 个有
- `TextInput_` —— 9/13 个有
- `AudioCrop` —— 8/13 个有
- `LTX2SamplingPreviewOverride` —— 6/13 个有
- `PreviewImage` —— 6/13 个有
- `ImageConcanate` —— 5/13 个有
- `LTXVAudioVAEDecode` —— 2/13 个有
- `Label (rgthree)` —— 2/13 个有
- `PrimitiveStringMultiline` —— 2/13 个有
- `SimpleCalculatorKJ` —— 2/13 个有
- `LayerUtility: PurgeVRAM` —— 1/13 个有
- `MemoryCleaner` —— 1/13 个有
- `PainterVRAM` —— 1/13 个有
- `PromptRelayEncode` —— 1/13 个有
- `ResizeImagesByLongerEdge` —— 1/13 个有
- `TTResolutionSelector` —— 1/13 个有
- `WanVideoBlockSwap` —— 1/13 个有
- `WujiCleaner` —— 1/13 个有
- `wanBlock_Swap` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 13 | 100% |
| 高度 | 24 | 24 - 24 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，13 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，13 个样本，取值集中（一致性 100%）
