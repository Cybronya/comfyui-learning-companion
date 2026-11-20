---
name: unknown_workflow_video_sampler_clip_232
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.747
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoaderGGUF, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetNode, UnetLoaderGGUF, VAEDecodeTiled, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2 GGUF量化版图生视频_2021585038990647298.json, 视频生成/图生视频/LTX-2 GGUF（rubby）_2012344262502912001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_232

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX-2 GGUF量化版图生视频_2021585038990647298.json、视频生成/图生视频/LTX-2 GGUF（rubby）_2012344262502912001.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoaderGGUF`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/2 个有
- `Int` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `SomethingToString` —— 1/2 个有
- `Split String` —— 1/2 个有
- `TextPreview` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
