---
name: unknown_workflow_upscale_latent_upscale_lora_77
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.579667
common_nodes: [Any To String (mtb), CFGGuider, CLIPTextEncode, CR String To Combo, CR Text, CR Text Concatenate, CreateVideo, Display Any (rgthree), EmptyImage, EmptyLTXVLatentVideo, GetImageSize, GetNode, ImageScaleBy, ImpactSwitch, Int, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, SetNode, ShowText|pysssss, VAEDecodeTiled, VRAMReserver, easy cleanGpuUsed, easy convertAnything, easy int, ttN concat]
problems: []
missing: []
members: [视频生成/图生视频/图生视频LTX2.0_2008764920220880897.json, 视频生成/文生视频/LTX2.3图生视频+音视同步【双版本优化】_2059047320699891713.json, 视频生成/文生视频/ltx2.3 图生视频【蒸馏版】+反推提示词_2037473491712221185.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_77

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/图生视频LTX2.0_2008764920220880897.json、视频生成/文生视频/LTX2.3图生视频+音视同步【双版本优化】_2059047320699891713.json、视频生成/文生视频/ltx2.3 图生视频【蒸馏版】+反推提示词_2037473491712221185.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `Any To String (mtb)`
- `CFGGuider`
- `CLIPTextEncode`
- `CR String To Combo`
- `CR Text`
- `CR Text Concatenate`
- `CreateVideo`
- `Display Any (rgthree)`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `ImageScaleBy`
- `ImpactSwitch`
- `Int`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `ShowText|pysssss`
- `VAEDecodeTiled`
- `VRAMReserver`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `easy int`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `CR Value` —— 2/3 个有
- `CheckpointLoaderSimple` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `LTXAVTextEncoderLoader` —— 2/3 个有
- `LTXVAudioVAELoader` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VAELoaderKJ` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `AnySwitch` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GGUFLoaderKJ` —— 1/3 个有
- `LTX2_NAG` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `MemoryCleaner` —— 1/3 个有
- `ModelScopeVisionPromptInversion_Sevr` —— 1/3 个有
- `PIP_IntegerCalculator` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `ProcessString` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `RTXVideoSuperResolution` —— 1/3 个有
- `SomethingToString` —— 1/3 个有
- `Switch any [Crystools]` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `easy boolean` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 24 | 24 - 24 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，3 个样本，取值集中（一致性 100%）
