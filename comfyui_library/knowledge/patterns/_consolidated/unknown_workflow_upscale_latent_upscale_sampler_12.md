---
name: unknown_workflow_upscale_latent_upscale_sampler_12
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.889222
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [图片生成/文生图/2030338706959245314.json, 数字人/数字人/LTX2.3首尾帧_2037413437122289666.json, 视频生成/图生视频/ITX2.3--首尾帧_2032004087528562690.json, 视频生成/图生视频/LTX-2 GGUF 12GB图生有声视频工作流-B站UP主@好奇漫步_2018342004555522049.json, 视频生成/图生视频/LTX-2.3  5图高清参考工作流V1.0_2038717836129996802.json, 视频生成/图生视频/LTX2.3-I2V-GGUF_2031025711103873026.json, 视频生成/图生视频/LTX2.3强化对口型 KJ版_2040052966710845441.json, 视频生成/图生视频/本地开源免费，漫剧短镜头3_2057838055628828673.json, 视频生成/图生视频/本地开源免费，真人短镜头3_2058240849422675970.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_12

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/2030338706959245314.json、数字人/数字人/LTX2.3首尾帧_2037413437122289666.json、视频生成/图生视频/ITX2.3--首尾帧_2032004087528562690.json、视频生成/图生视频/LTX-2 GGUF 12GB图生有声视频工作流-B站UP主@好奇漫步_2018342004555522049.json、视频生成/图生视频/LTX-2.3  5图高清参考工作流V1.0_2038717836129996802.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `ResizeImagesByLongerEdge` —— 8/9 个有
- `CreateVideo` —— 7/9 个有
- `LTXVCropGuides` —— 7/9 个有
- `PrimitiveBoolean` —— 7/9 个有
- `ResizeImageMaskNode` —— 7/9 个有
- `ComfyMathExpression` —— 6/9 个有
- `SaveVideo` —— 6/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `UNETLoader` —— 5/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `LTXVImgToVideoInplaceKJ` —— 3/9 个有
- `PrimitiveFloat` —— 3/9 个有
- `UnetLoaderGGUF` —— 3/9 个有
- `VAELoader` —— 3/9 个有
- `VHS_VideoCombine` —— 3/9 个有
- `EmptyImage` —— 2/9 个有
- `EnhancedLoadDiffusionModel` —— 2/9 个有
- `GetImageSize` —— 2/9 个有
- `ImageScaleBy` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `easy indexAnything` —— 2/9 个有
- `CM_FloatToInt` —— 1/9 个有
- `LTXVImgToVideoConditionOnly` —— 1/9 个有
- `LTXVScheduler` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `MatAnyone` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有
- `Switch` —— 1/9 个有
- `Text` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 9 | 100% |
| 高度 | 25 | 25 - 25 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，9 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，9 个样本，取值集中（一致性 100%）
