---
name: unknown_workflow_video_lora_sampler_122
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.679923
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SimpleMath+, UNETLoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [视频生成/图生视频/2064300604129898497.json, 视频生成/图生视频/2048943736339570690.json, 视频生成/图生视频/2064316689243791362.json, 视频生成/图生视频/2068963265690034177.json, 视频生成/图生视频/2064318009904287745.json, 视频生成/图生视频/2047700964789981186.json, 视频生成/图生视频/2074096652201320450.json, 视频生成/图生视频/2074111504655405057.json, 视频生成/图生视频/2072497688859471874.json, 视频生成/图生视频/2075049953608687617.json, 视频生成/图生视频/2048694979278671873.json, 视频生成/文生视频/LTX-2.3_ICLoRA_Union_Control_Distilled_2033749447833821185.json, 视频生成/文生视频/LTX-2.5_ICLoRA_Union_Control（3采）V1_2087874712008478722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_122

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2064300604129898497.json、视频生成/图生视频/2048943736339570690.json、视频生成/图生视频/2064316689243791362.json、视频生成/图生视频/2068963265690034177.json、视频生成/图生视频/2064318009904287745.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
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
- `SimpleMath+`
- `UNETLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 12/13 个有
- `VAELoaderKJ` —— 12/13 个有
- `GetNode` —— 11/13 个有
- `INTConstant` —— 11/13 个有
- `ImageResizeKJv2` —— 11/13 个有
- `LatentUpscaleModelLoader` —— 11/13 个有
- `SetNode` —— 11/13 个有
- `CannyEdgePreprocessor` —— 8/13 个有
- `DWPreprocessor` —— 8/13 个有
- `DepthAnythingPreprocessor` —— 8/13 个有
- `PrimitiveBoolean` —— 8/13 个有
- `VAEDecodeTiled` —— 8/13 个有
- `LTXVPreprocess` —— 7/13 个有
- `LTXVImgToVideoInplace` —— 6/13 个有
- `LTXVLatentUpsampler` —— 6/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/13 个有
- `Text` —— 5/13 个有
- `VAEDecode` —— 5/13 个有
- `MathExpression|pysssss` —— 4/13 个有
- `ComfyMathExpression` —— 2/13 个有
- `LoraLoaderModelOnly` —— 2/13 个有
- `PreviewAny` —— 2/13 个有
- `RTXVideoSuperResolution` —— 2/13 个有
- `ResizeImageMaskNode` —— 2/13 个有
- `TextGenerateLTX2Prompt` —— 2/13 个有
- `CLIPLoader` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `LowVRAMCheckpointLoader` —— 1/13 个有
- `MultiTextConcatenate` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `VAELoader` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 13 | 100% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，13 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
