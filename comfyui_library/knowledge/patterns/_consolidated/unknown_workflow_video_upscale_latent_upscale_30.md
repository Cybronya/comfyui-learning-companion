---
name: unknown_workflow_video_upscale_latent_upscale_30
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.516364
common_nodes: [AudioInfo, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, SamplerCustom, Seed (rgthree), SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/LTX 2.3  单图数字人_2086755632165769217.json, 数字人/数字人/LTX 2.3  单图数字人高清工作流_2074911807369732098.json, 数字人/数字人/LTX-2.3+数字人对口型+高清画质工作流_2036703046939447298.json, 数字人/数字人/LTX2.3+（图+音频）数字人口播+高清优化版工作流_2083406138854428674.json, 视频生成/图生视频/LTX 2.3  单图数字人高清工作流_2072957704288694274.json, 视频生成/图生视频/LTX 2.3  图片语音生成数字人工作流_2072578791876161538.json, 视频生成/图生视频/LTX 2.3  首尾帧数字人唱歌+视频高清放大1080P_2047852790181011458.json, 视频生成/图生视频/LTX 2.3  首尾帧数字人高清+30秒视频41分钟pius模式_2046223171501694978.json, 视频生成/图生视频/LTX-2.3 数字人对口型 高清画质专业博主工作流 LAO-郑 5-12_2053738368332251137.json, 视频生成/图生视频/【数字人唱歌】LTX2.3_2057291924830248961.json, 视频生成/文生视频/LTX-2.3+数字人对口型多人对话唱歌+高清画质工作流_2069356013098196994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_30

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/LTX 2.3  单图数字人_2086755632165769217.json、数字人/数字人/LTX 2.3  单图数字人高清工作流_2074911807369732098.json、数字人/数字人/LTX-2.3+数字人对口型+高清画质工作流_2036703046939447298.json、数字人/数字人/LTX2.3+（图+音频）数字人口播+高清优化版工作流_2083406138854428674.json、视频生成/图生视频/LTX 2.3  单图数字人高清工作流_2072957704288694274.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 11 个 workflow 都包含：
- `AudioInfo`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `SamplerCustom`
- `Seed (rgthree)`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Display Any (rgthree)` —— 10/11 个有
- `ImageResizeKJv2` —— 10/11 个有
- `MelBandRoFormerModelLoader` —— 10/11 个有
- `MelBandRoFormerSampler` —— 10/11 个有
- `PreviewAudio` —— 10/11 个有
- `AudioCrop` —— 9/11 个有
- `LTXVEmptyLatentAudio` —— 8/11 个有
- `DiffusionModelLoaderKJ` —— 7/11 个有
- `Fast Groups Bypasser (rgthree)` —— 7/11 个有
- `LTXVImgToVideoInplaceKJ` —— 7/11 个有
- `ResizeImageMaskNode` —— 7/11 个有
- `ShowText|pysssss` —— 7/11 个有
- `TextInput_` —— 7/11 个有
- `ImageFlip` —— 5/11 个有
- `ResizeImagesByLongerEdge` —— 5/11 个有
- `JDC_ResizeFactor` —— 4/11 个有
- `LTX2SamplingPreviewOverride` —— 4/11 个有
- `LTX2_NAG` —— 4/11 个有
- `LTXVChunkFeedForward` —— 4/11 个有
- `LTXVImgToVideoInplace` —— 4/11 个有
- `LTXVScheduler` —— 4/11 个有
- `PathchSageAttentionKJ` —— 4/11 个有
- `PrimitiveBoolean` —— 4/11 个有
- `RH_LLMAPI_Pro_Node` —— 4/11 个有
- `UNETLoader` —— 4/11 个有
- `VAELoader` —— 4/11 个有
- `JoinStrings` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `RH_LLMAPI_NODE` —— 3/11 个有
- `ImageConcanate` —— 2/11 个有
- `LTXVAudioVAEDecode` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `LayerUtility: PurgeVRAM` —— 1/11 个有
- `PainterVRAM` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有
- `TTResolutionSelector` —— 1/11 个有
- `WanVideoBlockSwap` —— 1/11 个有
- `WujiCleaner` —— 1/11 个有
- `wanBlock_Swap` —— 1/11 个有

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
