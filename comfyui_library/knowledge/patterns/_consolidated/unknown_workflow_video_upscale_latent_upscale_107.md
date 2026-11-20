---
name: unknown_workflow_video_upscale_latent_upscale_107
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.76225
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/YZ金鱼-LTX-2 文生视频_2009514987760394241.json, 视频生成/文生视频/很强的文生视频-LTXV2.0你就是导演_2008866865359097857.json, 视频生成/文生视频/音画同步 LTX2.0 文生视频【蒸馏  48G】_2008562261769592834.json, 视频生成/文生视频/颠覆想象力：LTX2.0多模态文生视频自动优化提示词工作流自动加音效_2015594786417287170.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_107

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/YZ金鱼-LTX-2 文生视频_2009514987760394241.json、视频生成/文生视频/很强的文生视频-LTXV2.0你就是导演_2008866865359097857.json、视频生成/文生视频/音画同步 LTX2.0 文生视频【蒸馏  48G】_2008562261769592834.json、视频生成/文生视频/颠覆想象力：LTX2.0多模态文生视频自动优化提示词工作流自动加音效_2015594786417287170.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVCropGuides` —— 3/4 个有
- `LTXVScheduler` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `Int` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `MemoryCleaner` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `JoinStrings` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `Primitive integer [Crystools]` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `Qwen3VL_Advanced` —— 1/4 个有
- `Qwen3_VQA_Plus` —— 1/4 个有
- `VAEDecode` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 4 | 90% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，4 个样本，取值集中（一致性 90%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
