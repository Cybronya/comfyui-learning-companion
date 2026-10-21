---
name: unknown_workflow_upscale_latent_upscale_sampler_24
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.946
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, SimpleMath+, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3-多宫格生视频-画质感人-v2_2038941376720674817.json, 视频生成/文生视频/LTX2.3-多宫格生视频-画质感人_2038650134229159937.json, 视频生成/文生视频/LTX2.3-首尾帧_2031929637428793346.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_24

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/LTX2.3-多宫格生视频-画质感人-v2_2038941376720674817.json、视频生成/文生视频/LTX2.3-多宫格生视频-画质感人_2038650134229159937.json、视频生成/文生视频/LTX2.3-首尾帧_2031929637428793346.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 2/3 个有
- `GuHaiAutoImageSplit` —— 2/3 个有
- `ImageFromBatch` —— 2/3 个有
- `Int` —— 2/3 个有
- `LTXVAddGuideMulti` —— 2/3 个有
- `QZ_ResolutionPreset` —— 2/3 个有
- `RH_LLMAPI_Pro_Node` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `1hew_SaveVideo` —— 1/3 个有
- `ConcatTextOfUtils` —— 1/3 个有
- `LTXVImgToVideoInplaceKJ` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `Primitive float [Crystools]` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 3 | 89% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，3 个样本，取值集中（一致性 89%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
