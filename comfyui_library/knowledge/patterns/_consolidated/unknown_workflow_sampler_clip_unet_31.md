---
name: unknown_workflow_sampler_clip_unet_31
type: Unknown Workflow
frequency: 21
level: strong
coverage: 0.859286
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/ltx-2.5-22b-ic-lora-ingredients-0.9 参考图 Lora 视频工作流_2110025875143086082.json, 视频生成/图生视频/LTX-2.5 Cinemagraph 局部动态 图像到视频 ComfyUI 工作流_2110222043215130625.json, 视频生成/图生视频/LTX-2.5 Slow Motion Control 慢动作视频生成工作流_2110054667488153602.json, 视频生成/图生视频/LTX-2.5 单图多参_2087502470892310529.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2087976019419557889.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088139583937662977.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088145977638215681.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088158559048650753.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088327502329638913.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088508046191452161.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088508469056991233.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088516027708694530.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2089038486316871681.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2089204054537891841.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2089770769709621250.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2091566207215431682.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2093745280222064641.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2102437970862231554.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成_2091803227397378050.json, 视频生成/图生视频/LTX2.5-图生视频_2087412034005725185.json, 视频生成/图生视频/LTX2.5_i2v_2092791658453753857.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_31

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/ltx-2.5-22b-ic-lora-ingredients-0.9 参考图 Lora 视频工作流_2110025875143086082.json、视频生成/图生视频/LTX-2.5 Cinemagraph 局部动态 图像到视频 ComfyUI 工作流_2110222043215130625.json、视频生成/图生视频/LTX-2.5 Slow Motion Control 慢动作视频生成工作流_2110054667488153602.json、视频生成/图生视频/LTX-2.5 单图多参_2087502470892310529.json、视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2087976019419557889.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 21 个 workflow 都包含：
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
- `LTXVImgToVideoInplace` —— 20/21 个有
- `LTXVPreprocess` —— 20/21 个有
- `ResizeImageMaskNode` —— 20/21 个有
- `LTXVDualCFGGuider` —— 18/21 个有
- `LTXVLatentUpsampler` —— 18/21 个有
- `LatentUpscaleModelLoader` —— 18/21 个有
- `PrimitiveBoolean` —— 18/21 个有
- `ComfySwitchNode` —— 17/21 个有
- `ResolutionSelector` —— 17/21 个有
- `TextGenerateLTX2Prompt` —— 17/21 个有
- `PurgeVRAM_UTK` —— 15/21 个有
- `GetImageSize` —— 4/21 个有
- `PrimitiveFloat` —— 4/21 个有
- `CFGGuider` —— 3/21 个有
- `LTXAddVideoICLoRAGuide` —— 2/21 个有
- `LTXICLoRALoaderModelOnly` —— 2/21 个有
- `LTXVCropGuides` —— 2/21 个有
- `LoraLoaderModelOnly` —— 2/21 个有
- `RepeatImageBatch` —— 2/21 个有
- `XB_CanvasLabel` —— 2/21 个有
- `GetVideoComponents` —— 1/21 个有
- `ImageScale` —— 1/21 个有
- `Label (rgthree)` —— 1/21 个有
- `PreviewAny` —— 1/21 个有
- `easy showAnything` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 21 | 95% |
| 高度 | 25 | 24 - 25 | 21 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，21 个样本，取值集中（一致性 95%）
- 高度 中位数 25，观测区间 24 - 25，21 个样本，取值集中（一致性 99%）
