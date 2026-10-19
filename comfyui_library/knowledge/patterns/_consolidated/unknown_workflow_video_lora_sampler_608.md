---
name: unknown_workflow_video_lora_sampler_608
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.996333
common_nodes: [CFGGuider, CLIPTextEncode, CR Float To Integer, DiffusionModelLoaderKJ, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy float, easy getNode, easy int, easy setNode]
problems: []
missing: []
members: [视频生成/图生视频/2046138080263938050.json, 视频生成/图生视频/2048930807976300546.json, 视频生成/图生视频/2044379140505214978.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_608

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2046138080263938050.json、视频生成/图生视频/2048930807976300546.json、视频生成/图生视频/2044379140505214978.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Float To Integer`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy float`
- `easy getNode`
- `easy int`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `JWFloat` —— 2/3 个有
- `LTXVLatentUpsampler` —— 2/3 个有
- `LTXVScheduler` —— 2/3 个有
- `LatentUpscaleModelLoader` —— 2/3 个有

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
