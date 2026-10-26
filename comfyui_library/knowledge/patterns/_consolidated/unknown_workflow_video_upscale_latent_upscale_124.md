---
name: unknown_workflow_video_upscale_latent_upscale_124
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.630333
common_nodes: [CFGGuider, CLIPTextEncode, CR Float To Integer, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed, easy positive]
problems: []
missing: []
members: [视频生成/图生视频/解说漫-LTX对话_2062249205984485378.json, 视频生成/图生视频/解说漫-LTX旁白_2062236079884947457.json, 视频生成/图生视频/解说漫-单图LTX旁白_2065767656409616386.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_124

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/解说漫-LTX对话_2062249205984485378.json、视频生成/图生视频/解说漫-LTX旁白_2062236079884947457.json、视频生成/图生视频/解说漫-单图LTX旁白_2065767656409616386.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Float To Integer`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `1hew_AudioDuration` —— 1/3 个有
- `Float` —— 1/3 个有
- `LTXVAudioVAEEncode` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `SetLatentNoiseMask` —— 1/3 个有
- `SolidMask` —— 1/3 个有

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
