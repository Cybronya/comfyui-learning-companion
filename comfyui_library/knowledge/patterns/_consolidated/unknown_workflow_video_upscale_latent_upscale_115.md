---
name: unknown_workflow_video_upscale_latent_upscale_115
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.721333
common_nodes: [CFGGuider, CLIPTextEncode, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, JoinStrings, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, Qwen3_VQA, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, TextInput_, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.0文生视频gguf版本_2012499867683262466.json, 视频生成/文生视频/LTX2文生视频低显存版2.0（智能提示词扩写）_2011000003422068738.json, 视频生成/文生视频/LTX2文生视频低显存版（智能提示词扩写）_2009277455604916226.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_115

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/LTX2.0文生视频gguf版本_2012499867683262466.json、视频生成/文生视频/LTX2文生视频低显存版2.0（智能提示词扩写）_2011000003422068738.json、视频生成/文生视频/LTX2文生视频低显存版（智能提示词扩写）_2009277455604916226.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `JoinStrings`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `Qwen3_VQA`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `TextInput_`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `CheckpointLoaderSimple` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `LTXAVTextEncoderLoader` —— 2/3 个有
- `LTXVAudioVAELoader` —— 2/3 个有
- `RH_LLMAPI_Pro_Node` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `DualCLIPLoaderGGUF` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `PurgeVRAM_UTK` —— 1/3 个有
- `SomethingToString` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `VAELoader` —— 1/3 个有
- `VAELoaderKJ` —— 1/3 个有

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
