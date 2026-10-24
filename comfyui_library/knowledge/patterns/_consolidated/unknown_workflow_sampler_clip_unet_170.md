---
name: unknown_workflow_sampler_clip_unet_170
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.78125
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, TextGenerateLTX2Prompt, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/A-10 LTX-2.5 首尾帧生视频 （FLF2V）_2087395088770097154.json, 视频生成/图生视频/A-9 LTX-2.5 图生视频（I2V）· 首帧图直接出片 · 音画同步_2087380641817124866.json, 视频生成/图生视频/LTX 2.5 图生视频_2093915637625212929.json, 视频生成/图生视频/LTX 2.5 首尾帧生视频版_2094313555356119041.json, 视频生成/图生视频/LTX-2.5 T2V_I2V单采样_2087377086850883585.json, 视频生成/图生视频/LTX-2.5 T2V_I2V双采样_2087409169308676098.json, 视频生成/文生视频/ltx2.5双采文生+图生_2087504450205339650.json, 视频生成/文生视频/图生视频 文生视频 首尾帧 极速 LTX2.5全家桶 音画同出_2087552830658924545.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_170

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/A-10 LTX-2.5 首尾帧生视频 （FLF2V）_2087395088770097154.json、视频生成/图生视频/A-9 LTX-2.5 图生视频（I2V）· 首帧图直接出片 · 音画同步_2087380641817124866.json、视频生成/图生视频/LTX 2.5 图生视频_2093915637625212929.json、视频生成/图生视频/LTX 2.5 首尾帧生视频版_2094313555356119041.json、视频生成/图生视频/LTX-2.5 T2V_I2V单采样_2087377086850883585.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 7/8 个有
- `LTXVDualCFGGuider` —— 7/8 个有
- `PreviewAny` —— 7/8 个有
- `SaveVideo` —— 7/8 个有
- `KSamplerSelect` —— 6/8 个有
- `LTXVImgToVideoInplace` —— 6/8 个有
- `ResizeImageMaskNode` —— 6/8 个有
- `LTXVLatentUpsampler` —— 5/8 个有
- `LatentUpscaleModelLoader` —— 5/8 个有
- `ResolutionSelector` —— 5/8 个有
- `CFGGuider` —— 3/8 个有
- `ComfyNotNode` —— 3/8 个有
- `GetImageSize` —— 3/8 个有
- `LTXFloatToInt` —— 3/8 个有
- `LTXVAddGuide` —— 3/8 个有
- `LTXVCropGuides` —— 3/8 个有
- `PrimitiveFloat` —— 3/8 个有
- `SamplerEulerAncestral` —— 3/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `DualCLIPLoader` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `ImageFromBatch` —— 2/8 个有
- `SaveAudio` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `GemmaAPITextEncode` —— 1/8 个有
- `ImageScale` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `SeedGenerator` —— 1/8 个有
- `StringContains` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 8 | 89% |
| 高度 | 25 | 25 - 25 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，8 个样本，取值集中（一致性 89%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
