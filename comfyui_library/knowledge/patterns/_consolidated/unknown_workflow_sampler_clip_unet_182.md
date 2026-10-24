---
name: unknown_workflow_sampler_clip_unet_182
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.827714
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/ltx-2.5-22b-ic-lora-ingredients-0.9 参考图 Lora 视频工作流_2110025875143086082.json, 视频生成/图生视频/LTX-2.5 Cinemagraph 局部动态 图像到视频 ComfyUI 工作流_2110222043215130625.json, 视频生成/图生视频/LTX-2.5 Slow Motion Control 慢动作视频生成工作流_2110054667488153602.json, 视频生成/图生视频/LTX-2.5 单图多参_2087502470892310529.json, 视频生成/图生视频/LTX2.5图生视频 -高质量直出1K_2087559276465319937.json, 视频生成/文生视频/LTX2.5_I2V_T2V_2087347078044405762.json, 视频生成/文生视频/ltx2.5 - 文_图生视频 (2)_2087437692429750274.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_182

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/ltx-2.5-22b-ic-lora-ingredients-0.9 参考图 Lora 视频工作流_2110025875143086082.json、视频生成/图生视频/LTX-2.5 Cinemagraph 局部动态 图像到视频 ComfyUI 工作流_2110222043215130625.json、视频生成/图生视频/LTX-2.5 Slow Motion Control 慢动作视频生成工作流_2110054667488153602.json、视频生成/图生视频/LTX-2.5 单图多参_2087502470892310529.json、视频生成/图生视频/LTX2.5图生视频 -高质量直出1K_2087559276465319937.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LoadImage`
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
- `LTXVImgToVideoInplace` —— 6/7 个有
- `LTXVPreprocess` —— 6/7 个有
- `ResizeImageMaskNode` —— 6/7 个有
- `PrimitiveFloat` —— 5/7 个有
- `CFGGuider` —— 4/7 个有
- `GetImageSize` —— 4/7 个有
- `LTXVLatentUpsampler` —— 4/7 个有
- `LatentUpscaleModelLoader` —— 4/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `LTXVDualCFGGuider` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `ResolutionSelector` —— 3/7 个有
- `LTXAddVideoICLoRAGuide` —— 2/7 个有
- `LTXICLoRALoaderModelOnly` —— 2/7 个有
- `LTXVCropGuides` —— 2/7 个有
- `RepeatImageBatch` —— 2/7 个有
- `XB_CanvasLabel` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ComfyNotNode` —— 1/7 个有
- `GetVideoComponents` —— 1/7 个有
- `ImageScale` —— 1/7 个有
- `LTXFloatToInt` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 7 | 90% |
| 高度 | 25 | 24 - 25 | 7 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，7 个样本，取值集中（一致性 90%）
- 高度 中位数 25，观测区间 24 - 25，7 个样本，取值集中（一致性 99%）
