---
name: unknown_workflow_sampler_clip_unet_244
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.7755
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, CreateVideo, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PreviewAny, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, TextGenerateLTX2Prompt, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/A-10 LTX-2.5 首尾帧生视频 （FLF2V）_2087395088770097154.json, 视频生成/图生视频/A-9 LTX-2.5 图生视频（I2V）· 首帧图直接出片 · 音画同步_2087380641817124866.json, 视频生成/图生视频/LTX 2.5 图生视频_2093915637625212929.json, 视频生成/图生视频/LTX 2.5 首尾帧生视频版_2094313555356119041.json, 视频生成/图生视频/LTX-2.5 T2V_I2V单采样_2087377086850883585.json, 视频生成/图生视频/LTX-2.5 T2V_I2V双采样_2087409169308676098.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_244

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/A-10 LTX-2.5 首尾帧生视频 （FLF2V）_2087395088770097154.json、视频生成/图生视频/A-9 LTX-2.5 图生视频（I2V）· 首帧图直接出片 · 音画同步_2087380641817124866.json、视频生成/图生视频/LTX 2.5 图生视频_2093915637625212929.json、视频生成/图生视频/LTX 2.5 首尾帧生视频版_2094313555356119041.json、视频生成/图生视频/LTX-2.5 T2V_I2V单采样_2087377086850883585.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 4/6 个有
- `LTXVImgToVideoInplace` —— 4/6 个有
- `ResizeImageMaskNode` —— 4/6 个有
- `ResolutionSelector` —— 4/6 个有
- `LTXVLatentUpsampler` —— 3/6 个有
- `LatentUpscaleModelLoader` —— 3/6 个有
- `CFGGuider` —— 2/6 个有
- `ComfyNotNode` —— 2/6 个有
- `DualCLIPLoader` —— 2/6 个有
- `GetImageSize` —— 2/6 个有
- `ImageFromBatch` —— 2/6 个有
- `LTXFloatToInt` —— 2/6 个有
- `LTXVAddGuide` —— 2/6 个有
- `LTXVCropGuides` —— 2/6 个有
- `PrimitiveFloat` —— 2/6 个有
- `SamplerEulerAncestral` —— 2/6 个有
- `SaveAudio` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `GemmaAPITextEncode` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `SeedGenerator` —— 1/6 个有
- `StringContains` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 6 | 89% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，6 个样本，取值集中（一致性 89%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
