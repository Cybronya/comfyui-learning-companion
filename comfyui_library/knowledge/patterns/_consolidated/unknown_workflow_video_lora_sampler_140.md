---
name: unknown_workflow_video_lora_sampler_140
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.648167
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2064300604129898497.json, 视频生成/图生视频/2048943736339570690.json, 视频生成/图生视频/2064316689243791362.json, 视频生成/图生视频/2068963265690034177.json, 视频生成/图生视频/2064318009904287745.json, 视频生成/图生视频/2047700964789981186.json, 视频生成/图生视频/2074096652201320450.json, 视频生成/图生视频/2074111504655405057.json, 视频生成/图生视频/2072497688859471874.json, 视频生成/图生视频/2075049953608687617.json, 视频生成/图生视频/2048694979278671873.json, 视频生成/图生视频/2042591989492879362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_140

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/2064300604129898497.json、视频生成/图生视频/2048943736339570690.json、视频生成/图生视频/2064316689243791362.json、视频生成/图生视频/2068963265690034177.json、视频生成/图生视频/2064318009904287745.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 11/12 个有
- `LatentUpscaleModelLoader` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `SimpleMath+` —— 11/12 个有
- `VHS_VideoInfo` —— 11/12 个有
- `INTConstant` —— 10/12 个有
- `ImageResizeKJv2` —— 10/12 个有
- `PrimitiveBoolean` —— 8/12 个有
- `VAEDecodeTiled` —— 8/12 个有
- `CannyEdgePreprocessor` —— 7/12 个有
- `DWPreprocessor` —— 7/12 个有
- `DepthAnythingPreprocessor` —— 7/12 个有
- `LTXVPreprocess` —— 7/12 个有
- `LTXVImgToVideoInplace` —— 6/12 个有
- `LTXVLatentUpsampler` —— 6/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/12 个有
- `Text` —— 4/12 个有
- `VAEDecode` —— 4/12 个有
- `ComfyMathExpression` —— 3/12 个有
- `MathExpression|pysssss` —— 3/12 个有
- `LoraLoaderModelOnly` —— 2/12 个有
- `RTXVideoSuperResolution` —— 2/12 个有
- `ResizeImageMaskNode` —— 2/12 个有
- `Anything Everywhere` —— 1/12 个有
- `LTX2_NAG` —— 1/12 个有
- `LTXVChunkFeedForward` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `LowVRAMCheckpointLoader` —— 1/12 个有
- `ModelPatchTorchSettings` —— 1/12 个有
- `MultiTextConcatenate` —— 1/12 个有
- `PathchSageAttentionKJ` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `TextGenerateLTX2Prompt` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
