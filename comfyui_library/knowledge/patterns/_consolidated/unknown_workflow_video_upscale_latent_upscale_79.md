---
name: unknown_workflow_video_upscale_latent_upscale_79
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5898
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/ltx2.3_无导演台-参考音频_纯参数_2085178800698118146.json, 视频生成/图生视频/2076920722613686273.json, 视频生成/图生视频/2062249205984485378.json, 视频生成/图生视频/2062236079884947457.json, 视频生成/图生视频/2065767656409616386.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_79

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/ltx2.3_无导演台-参考音频_纯参数_2085178800698118146.json、视频生成/图生视频/2076920722613686273.json、视频生成/图生视频/2062249205984485378.json、视频生成/图生视频/2062236079884947457.json、视频生成/图生视频/2065767656409616386.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Float To Integer` —— 4/5 个有
- `LTXVEmptyLatentAudio` —— 4/5 个有
- `Float` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `easy positive` —— 3/5 个有
- `BasicScheduler` —— 2/5 个有
- `Int` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `LTXVAudioVAEEncode` —— 2/5 个有
- `LoadAudio` —— 2/5 个有
- `PromptRelayEncode` —— 2/5 个有
- `SetLatentNoiseMask` —— 2/5 个有
- `SolidMask` —— 2/5 个有
- `TTResolutionSelector` —— 2/5 个有
- `1hew_AudioDuration` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
