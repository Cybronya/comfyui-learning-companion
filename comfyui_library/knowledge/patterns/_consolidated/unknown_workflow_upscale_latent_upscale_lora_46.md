---
name: unknown_workflow_upscale_latent_upscale_lora_46
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.859571
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/2063969520473165826.json, 视频生成/图生视频/2073707066895724546.json, 视频生成/图生视频/2037115894140248065.json, 视频生成/图生视频/2030985719384121346.json, 视频生成/图生视频/2048728329137688578.json, 视频生成/图生视频/2037154084020559874.json, 视频生成/图生视频/2037180362916368386.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_46

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2063969520473165826.json、视频生成/图生视频/2073707066895724546.json、视频生成/图生视频/2037115894140248065.json、视频生成/图生视频/2030985719384121346.json、视频生成/图生视频/2048728329137688578.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LTXVFirstLastFrameControl_TTP` —— 6/7 个有
- `ImageResizeKJv2` —— 5/7 个有
- `ImageStitch` —— 5/7 个有
- `ResizeImageMaskNode` —— 5/7 个有
- `ResizeImagesByLongerEdge` —— 5/7 个有
- `SimpleMath+` —— 5/7 个有
- `CheckpointLoaderSimple` —— 4/7 个有
- `CreateVideo` —— 4/7 个有
- `LTXAVTextEncoderLoader` —— 4/7 个有
- `LTXVAudioVAELoader` —— 4/7 个有
- `SaveVideo` —— 4/7 个有
- `DualCLIPLoader` —— 3/7 个有
- `LTXVImgToVideoConditionOnly` —— 3/7 个有
- `UNETLoader` —— 3/7 个有
- `VAELoaderKJ` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `Int` —— 2/7 个有
- `LTXTiledSampler` —— 2/7 个有
- `LTXVImgToVideoInplace` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `LayerUtility: PurgeVRAM` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `TextConcat` —— 2/7 个有
- `ToString` —— 2/7 个有
- `easy imageConcat` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
