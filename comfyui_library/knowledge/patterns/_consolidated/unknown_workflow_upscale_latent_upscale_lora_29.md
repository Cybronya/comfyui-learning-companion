---
name: unknown_workflow_upscale_latent_upscale_lora_29
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.899778
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2052231209417232385.json, 视频生成/图生视频/2066087069847482370.json, 视频生成/图生视频/2044864850374955009.json, 视频生成/图生视频/2030820457208877058.json, 视频生成/图生视频/2039704492752510977.json, 视频生成/图生视频/2039914050452201474.json, 视频生成/图生视频/2035325472770367490.json, 视频生成/图生视频/2057749829224329218.json, 视频生成/图生视频/2049303254957297665.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_29

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2052231209417232385.json、视频生成/图生视频/2066087069847482370.json、视频生成/图生视频/2044864850374955009.json、视频生成/图生视频/2030820457208877058.json、视频生成/图生视频/2039704492752510977.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 8/9 个有
- `ResizeImagesByLongerEdge` —— 8/9 个有
- `SimpleMath+` —— 7/9 个有
- `FloatConstant` —— 5/9 个有
- `LTXVChunkFeedForward` —— 5/9 个有
- `LTXVImgToVideoInplaceKJ` —— 5/9 个有
- `ModelPatchTorchSettings` —— 5/9 个有
- `PathchSageAttentionKJ` —— 5/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `RH_LLMAPI_Pro_Node` —— 5/9 个有
- `easy showAnything` —— 5/9 个有
- `PreviewAny` —— 4/9 个有
- `PrimitiveBoolean` —— 4/9 个有
- `llama_cpp_instruct_adv` —— 4/9 个有
- `llama_cpp_model_loader` —— 4/9 个有
- `llama_cpp_parameters` —— 4/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `CR Prompt Text` —— 2/9 个有
- `CR Text` —— 2/9 个有
- `CustomAddLabel` —— 2/9 个有
- `Int` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `MultiTextConcatenate` —— 2/9 个有
- `RH_Utils` —— 2/9 个有
- `ResizeImageMaskNode` —— 2/9 个有
- `TTResolutionSelector` —— 2/9 个有
- `easy int` —— 2/9 个有
- `ttN concat` —— 2/9 个有
- `AILab_QwenVL` —— 1/9 个有
- `CombineImagesForQwen3VL` —— 1/9 个有
- `DualCLIPLoader` —— 1/9 个有
- `Evaluate Integers` —— 1/9 个有
- `Image Resize` —— 1/9 个有
- `QZ_ResolutionPreset` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `SDVN Any Show` —— 1/9 个有
- `TextGenerateLTX2Prompt` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 9 | 100% |
| 高度 | 25 | 25 - 25 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，9 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，9 个样本，取值集中（一致性 100%）
