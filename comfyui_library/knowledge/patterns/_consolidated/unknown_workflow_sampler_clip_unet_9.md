---
name: unknown_workflow_sampler_clip_unet_9
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.794125
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.5 Cinemagraph 局部动态 图像到视频 ComfyUI 工作流_2110222043215130625.json, 视频生成/图生视频/LTX-2.5 Slow Motion Control 慢动作视频生成工作流_2110054667488153602.json, 视频生成/图生视频/LTX-2.5 T2V_I2V单采样_2087377086850883585.json, 视频生成/图生视频/LTX-2.5 T2V_I2V双采样_2087409169308676098.json, 视频生成/图生视频/LTX2.5-图生视频_2087412034005725185.json, 视频生成/图生视频/LTX2.5图生视频_2087332188219068417.json, 视频生成/图生视频/LTX2.5图生视频_2087422859705667585.json, 视频生成/图生视频/LTX2.5图生视频_2087443699126071298.json, 视频生成/图生视频/LTX2.5图生视频_2088701698968743938.json, 视频生成/图生视频/LTX2.5图生视频_2089721005475459074.json, 视频生成/图生视频/LTX2.5图生视频_2090891877334736897.json, 视频生成/图生视频/LTX2.5图生视频（速度快、像素高）_2087522388522127361.json, 视频生成/图生视频/LTX2.5超精简图生视频480P只要2分钟【推荐新手试用】_2087528931011424257.json, 视频生成/文生视频/LTX2.5-文生视频_2087399947888062465.json, 视频生成/文生视频/ltx2.5 - 文_图生视频 (2)_2087437692429750274.json, 视频生成/文生视频/ltx2.5双采文生+图生_2087504450205339650.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/LTX-2.5 Cinemagraph 局部动态 图像到视频 ComfyUI 工作流_2110222043215130625.json、视频生成/图生视频/LTX-2.5 Slow Motion Control 慢动作视频生成工作流_2110054667488153602.json、视频生成/图生视频/LTX-2.5 T2V_I2V单采样_2087377086850883585.json、视频生成/图生视频/LTX-2.5 T2V_I2V双采样_2087409169308676098.json、视频生成/图生视频/LTX2.5-图生视频_2087412034005725185.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 15/16 个有
- `LTXVPreprocess` —— 15/16 个有
- `LoadImage` —— 15/16 个有
- `ResizeImageMaskNode` —— 15/16 个有
- `LTXVLatentUpsampler` —— 14/16 个有
- `LatentUpscaleModelLoader` —— 14/16 个有
- `ComfySwitchNode` —— 13/16 个有
- `LTXVDualCFGGuider` —— 13/16 个有
- `PrimitiveBoolean` —— 13/16 个有
- `ResolutionSelector` —— 13/16 个有
- `TextGenerateLTX2Prompt` —— 13/16 个有
- `PreviewAny` —— 10/16 个有
- `PrimitiveFloat` —— 6/16 个有
- `CFGGuider` —— 5/16 个有
- `ComfyNotNode` —— 4/16 个有
- `LTXFloatToInt` —— 4/16 个有
- `LoraLoaderModelOnly` —— 3/16 个有
- `easy showAnything` —— 3/16 个有
- `DualCLIPLoader` —— 2/16 个有
- `GetImageSize` —— 2/16 个有
- `XB_CanvasLabel` —— 2/16 个有
- `CR Text` —— 1/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `GemmaAPITextEncode` —— 1/16 个有
- `PreviewImage` —— 1/16 个有
- `RH_LLMAPI_Pro_Node` —— 1/16 个有
- `SeedGenerator` —— 1/16 个有
- `StringContains` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 16 | 90% |
| 高度 | 25 | 25 - 25 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，16 个样本，取值集中（一致性 90%）
- 高度 中位数 25，观测区间 25 - 25，16 个样本，取值集中（一致性 100%）
