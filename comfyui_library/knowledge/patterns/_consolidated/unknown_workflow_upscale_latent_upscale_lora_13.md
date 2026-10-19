---
name: unknown_workflow_upscale_latent_upscale_lora_13
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.848231
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveStringMultiline, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2031685383376867330.json, 视频生成/图生视频/2031928343846723586.json, 视频生成/图生视频/2030540846281527298.json, 视频生成/图生视频/2075950096994361345.json, 视频生成/图生视频/2037117341531643906.json, 视频生成/图生视频/2042604454435889153.json, 视频生成/图生视频/2030584551327670273.json, 视频生成/图生视频/2037112524918755329.json, 视频生成/图生视频/2031341831253925890.json, 视频生成/图生视频/2032121353918226434.json, 视频生成/图生视频/2034102193380401154.json, 视频生成/图生视频/2040291923272933378.json, 视频生成/图生视频/2081658308183814145.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_13

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2031685383376867330.json、视频生成/图生视频/2031928343846723586.json、视频生成/图生视频/2030540846281527298.json、视频生成/图生视频/2075950096994361345.json、视频生成/图生视频/2037117341531643906.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 13 个 workflow 都包含：
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
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 12/13 个有
- `ImageResizeKJv2` —— 10/13 个有
- `LTX2_NAG` —— 8/13 个有
- `ResizeImageMaskNode` —— 8/13 个有
- `Int` —— 6/13 个有
- `LTXVImgToVideoInplaceKJ` —— 6/13 个有
- `llama_cpp_instruct_adv` —— 6/13 个有
- `llama_cpp_model_loader` —— 6/13 个有
- `llama_cpp_parameters` —— 6/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/13 个有
- `LayerUtility: PurgeVRAM V2` —— 5/13 个有
- `PrimitiveBoolean` —— 5/13 个有
- `Fast Groups Bypasser (rgthree)` —— 4/13 个有
- `MathExpression|pysssss` —— 4/13 个有
- `Float` —— 3/13 个有
- `ImageStitch` —— 2/13 个有
- `LTXTiledSampler` —— 2/13 个有
- `LTXVFirstLastFrameControl_TTP` —— 2/13 个有
- `LTXVLatentUpsamplerTiled` —— 2/13 个有
- `LTXVMiddleFrame_TTP` —— 2/13 个有
- `easy mathInt` —— 2/13 个有
- `easy showAnything` —— 2/13 个有
- `CustomAddLabel` —— 1/13 个有
- `JWFloat` —— 1/13 个有
- `RH_Utils` —— 1/13 个有
- `TTResolutionSelector` —— 1/13 个有
- `ttN concat` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 13 | 100% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，13 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
