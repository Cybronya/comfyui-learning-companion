---
name: unknown_workflow_upscale_latent_upscale_lora_64
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7598
common_nodes: [CFGGuider, CLIPTextEncode, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.0 音画同步 文生视频_2013869097615888385.json, 视频生成/文生视频/LTX-2 GGUF 12GB 文生有声视频工作流-B站UP主@好奇漫步_2018342048012701697.json, 视频生成/文生视频/LTX-2 文生视频-音画同步-支持中英文_2008850630965731329.json, 视频生成/文生视频/LTX-2 文生视频_2009299206938304514.json, 视频生成/文生视频/LTX-2.3-T2V_2043499040456839169.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_64

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/LTX 2.0 音画同步 文生视频_2013869097615888385.json、视频生成/文生视频/LTX-2 GGUF 12GB 文生有声视频工作流-B站UP主@好奇漫步_2018342048012701697.json、视频生成/文生视频/LTX-2 文生视频-音画同步-支持中英文_2008850630965731329.json、视频生成/文生视频/LTX-2 文生视频_2009299206938304514.json、视频生成/文生视频/LTX-2.3-T2V_2043499040456839169.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 4/5 个有
- `LTXAVTextEncoderLoader` —— 4/5 个有
- `LTXVAudioVAELoader` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `LTXVCropGuides` —— 3/5 个有
- `VAEDecodeTiled` —— 3/5 个有
- `VHS_VideoCombine` —— 3/5 个有
- `CreateVideo` —— 2/5 个有
- `DualCLIPLoader` —— 2/5 个有
- `LTXVGemmaEnhancePrompt` —— 2/5 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `SaveVideo` —— 2/5 个有
- `UnetLoaderGGUF` —— 2/5 个有
- `VAELoaderKJ` —— 2/5 个有
- `CM_IntToFloat` —— 1/5 个有
- `CR Float To Integer` —— 1/5 个有
- `DF_Int_to_Float` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `ImpactExecutionOrderController` —— 1/5 个有
- `LTXVGemmaCLIPModelLoader` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `VAELoader` —— 1/5 个有
- `easy float` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 5 | 89% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，5 个样本，取值集中（一致性 89%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
