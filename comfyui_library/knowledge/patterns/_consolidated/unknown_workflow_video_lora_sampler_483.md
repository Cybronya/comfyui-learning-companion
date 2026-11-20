---
name: unknown_workflow_video_lora_sampler_483
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6054
common_nodes: [CFGGuider, CLIPTextEncode, CannyEdgePreprocessor, DWPreprocessor, DepthAnythingV2Preprocessor, EmptyLTXVLatentVideo, GetImageSize, GetNode, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, MathExpression|pysssss, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3-动作迁移_2055551224920985601.json, 视频生成/图生视频/LTX2.3-视频参考生成原生720P版工作流_2031747450532274178.json, 视频生成/图生视频/LTX2.3-视频参考生成超分720P加速版_2031927472920469506.json, 视频生成/文生视频/LTX 2.3 音视频生成 All-In-One 拆分子图-6和1版工作流_2046932902830678017.json, 视频生成/文生视频/LTX 2.5 All-In-One (八合一全功能) 解开子图版工作流_2091797657235845121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_483

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3-动作迁移_2055551224920985601.json、视频生成/图生视频/LTX2.3-视频参考生成原生720P版工作流_2031747450532274178.json、视频生成/图生视频/LTX2.3-视频参考生成超分720P加速版_2031927472920469506.json、视频生成/文生视频/LTX 2.3 音视频生成 All-In-One 拆分子图-6和1版工作流_2046932902830678017.json、视频生成/文生视频/LTX 2.5 All-In-One (八合一全功能) 解开子图版工作流_2091797657235845121.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `DWPreprocessor`
- `DepthAnythingV2Preprocessor`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `MathExpression|pysssss`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `LTXVLatentUpsampler` —— 3/5 个有
- `LatentUpscaleModelLoader` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `PrimitiveBoolean` —— 3/5 个有
- `ResizeImagesByLongerEdge` —— 3/5 个有
- `Any Switch (rgthree)` —— 2/5 个有
- `CM_FloatToInt` —— 2/5 个有
- `CM_IntToFloat` —— 2/5 个有
- `ComfyMathExpression` —— 2/5 个有
- `ComfySwitchNode` —— 2/5 个有
- `EmptyImage` —— 2/5 个有
- `FinalFrameSelector` —— 2/5 个有
- `ImageResizeAdvanced` —— 2/5 个有
- `ImageScaleBy` —— 2/5 个有
- `LTXVChunkFeedForward` —— 2/5 个有
- `LTXVImgToVideoInplace` —— 2/5 个有
- `Power Lora Loader (rgthree)` —— 2/5 个有
- `PreviewAudio` —— 2/5 个有
- `Switch any [Crystools]` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `UnetLoaderGGUF` —— 2/5 个有
- `VAELoader` —— 2/5 个有
- `mxSlider` —— 2/5 个有
- `Any To Any` —— 1/5 个有
- `CLIPLoader` —— 1/5 个有
- `CR Float To Integer` —— 1/5 个有
- `LTX2SamplingPreviewOverride` —— 1/5 个有
- `LTXVAddGuideMulti` —— 1/5 个有
- `LTXVDualCFGGuider` —— 1/5 个有
- `LTXVImgToVideoInplaceKJ` —— 1/5 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `ModelPreviewOverrideKJ` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有
- `SigmasPreview` —— 1/5 个有
- `SimpleCalculatorKJ` —— 1/5 个有
- `TrimAudioDuration` —— 1/5 个有
- `VHS_LoadAudioUpload` —— 1/5 个有
- `VHS_VideoInfoLoaded` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 24 - 25 | 5 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，5 个样本，取值集中（一致性 98%）
