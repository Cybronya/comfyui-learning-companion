---
name: unknown_workflow_video_sampler_clip_46
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.492
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PathchSageAttentionKJ, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [平台全量/LTX2.3 动作迁移_2035556740632154113.json, 数字人/数字人/「Supermate」LTX2.3-数字人说话&唱歌-加强版_2042665378840584193.json, 视频生成/图生视频/LTX-2.3-动作迁移_2055551224920985601.json, 视频生成/图生视频/LTX2.3 动作迁移（LTX-2.3 22B IC-LoRA 联合控制）_2042591989492879362.json, 视频生成/图生视频/LTX2.3 数字人说话&唱歌_2035556711162978305.json, 视频生成/图生视频/LTX2.3-数字人说话唱歌长视频版 图生视频加强版_2060612930189746177.json, 视频生成/图生视频/LTX2.3-数字人说话唱歌长视频版 图生视频加强版_2073725528359661570.json, 视频生成/图生视频/LTX2.3-数字人说话唱歌长视频版 图生视频加强版_2078784827976937473.json, 视频生成/图生视频/LTX2.3-生长视频版数字人说话唱歌图生视频加强版_2060324398200090625.json, 视频生成/图生视频/LTX2.3-生长视频版数字人说话唱歌图生视频加强版_2075890796582236161.json, 视频生成/文生视频/LTX2.3-生长视频版-27秒6分钟生成-数字人说话&唱歌-加强版_2036248412106002433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_46

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/LTX2.3 动作迁移_2035556740632154113.json、数字人/数字人/「Supermate」LTX2.3-数字人说话&唱歌-加强版_2042665378840584193.json、视频生成/图生视频/LTX-2.3-动作迁移_2055551224920985601.json、视频生成/图生视频/LTX2.3 动作迁移（LTX-2.3 22B IC-LoRA 联合控制）_2042591989492879362.json、视频生成/图生视频/LTX2.3 数字人说话&唱歌_2035556711162978305.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 10/11 个有
- `ComfyMathExpression` —— 10/11 个有
- `LTX2_NAG` —— 10/11 个有
- `LTXVImgToVideoInplace` —— 10/11 个有
- `LTXVLatentUpsampler` —— 10/11 个有
- `LatentUpscaleModelLoader` —— 10/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/11 个有
- `ModelPatchTorchSettings` —— 10/11 个有
- `PrimitiveInt` —— 10/11 个有
- `easy cleanGpuUsed` —— 10/11 个有
- `CR Float To Integer` —— 9/11 个有
- `LTXVAudioVAEEncode` —— 9/11 个有
- `MathExpression|pysssss` —— 9/11 个有
- `SetLatentNoiseMask` —— 9/11 个有
- `SolidMask` —— 9/11 个有
- `MelBandRoFormerModelLoader` —— 8/11 个有
- `MelBandRoFormerSampler` —— 8/11 个有
- `PrimitiveStringMultiline` —— 8/11 个有
- `VHS_LoadAudioUpload` —— 8/11 个有
- `WujiCleaner` —— 7/11 个有
- `CannyEdgePreprocessor` —— 3/11 个有
- `DWPreprocessor` —— 3/11 个有
- `GetImageSize` —— 3/11 个有
- `LTXAddVideoICLoRAGuide` —— 3/11 个有
- `LTXICLoRALoaderModelOnly` —— 3/11 个有
- `LTXVAudioVAEDecode` —— 3/11 个有
- `LTXVEmptyLatentAudio` —— 3/11 个有
- `LTXVImgToVideoConditionOnly` —— 3/11 个有
- `ResizeImageMaskNode` —— 3/11 个有
- `VHS_LoadVideo` —— 3/11 个有
- `DepthAnythingPreprocessor` —— 2/11 个有
- `ComfySwitchNode` —— 1/11 个有
- `DepthAnythingV2Preprocessor` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `SigmasPreview` —— 1/11 个有
- `VAELoader` —— 1/11 个有
- `VHS_VideoInfoLoaded` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
