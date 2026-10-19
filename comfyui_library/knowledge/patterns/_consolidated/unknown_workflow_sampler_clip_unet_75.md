---
name: unknown_workflow_sampler_clip_unet_75
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.77725
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ManualSigmas, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.5 单图多参_2087502470892310529.json, 视频生成/图生视频/LTX-2.5图生视频（提示词指南）_2087560099316453378.json, 视频生成/图生视频/LTX-2.5首尾帧生视频（提示词指南）_2087552277501530114.json, 视频生成/文生视频/LTX-2.5文生视频（提示词指南）_2087564051504263169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_75

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX-2.5 单图多参_2087502470892310529.json、视频生成/图生视频/LTX-2.5图生视频（提示词指南）_2087560099316453378.json、视频生成/图生视频/LTX-2.5首尾帧生视频（提示词指南）_2087552277501530114.json、视频生成/文生视频/LTX-2.5文生视频（提示词指南）_2087564051504263169.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
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
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 3/4 个有
- `Int` —— 3/4 个有
- `LTXFloatToInt` —— 3/4 个有
- `LTXVPreprocess` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `ResizeImageMaskNode` —— 3/4 个有
- `DF_Get_image_size` —— 2/4 个有
- `LTXVCropGuides` —— 2/4 个有
- `LTXVImgToVideoInplace` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `GetImageSize` —— 1/4 个有
- `GetVideoComponents` —— 1/4 个有
- `LTXAddVideoICLoRAGuide` —— 1/4 个有
- `LTXICLoRALoaderModelOnly` —— 1/4 个有
- `LTXVAddGuide` —— 1/4 个有
- `LTXVDualCFGGuider` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `RepeatImageBatch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 4 | 100% |
| 高度 | 25 | 24 - 25 | 4 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，4 个样本，取值集中（一致性 98%）
