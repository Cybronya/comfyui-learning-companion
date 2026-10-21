---
name: unknown_workflow_upscale_latent_upscale_lora_8
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.850412
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2039704492752510977.json, 视频生成/图生视频/2039914050452201474.json, 视频生成/图生视频/2035320209401192449.json, 视频生成/图生视频/2030927886542180353.json, 视频生成/图生视频/2058356490804752385.json, 视频生成/图生视频/2037117341531643906.json, 视频生成/图生视频/2042604454435889153.json, 视频生成/图生视频/2030584551327670273.json, 视频生成/图生视频/2037112524918755329.json, 视频生成/图生视频/2034102193380401154.json, 视频生成/图生视频/2040291923272933378.json, 视频生成/图生视频/2049507628333670402.json, 视频生成/图生视频/2037239092089458690.json, 视频生成/文生视频/LTX-2.3+Qwen3.5生成宠物播客视频_2030535698637398018.json, 视频生成/文生视频/LTX-2.3+Qwen3.5生成武打电影视频_2030549062293921794.json, 视频生成/文生视频/LTX-2.3文_图生视频二合一_2030147617967050753.json, 视频生成/文生视频/LTX-2.3龙虾术：把”白狐酱板鸭_视频生成器装进OpenClaw！_2034812167572164610.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_8

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/2039704492752510977.json、视频生成/图生视频/2039914050452201474.json、视频生成/图生视频/2035320209401192449.json、视频生成/图生视频/2030927886542180353.json、视频生成/图生视频/2058356490804752385.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 17 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
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
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 16/17 个有
- `LTXVImgToVideoInplace` —— 16/17 个有
- `PrimitiveInt` —— 16/17 个有
- `PrimitiveStringMultiline` —— 14/17 个有
- `llama_cpp_instruct_adv` —— 12/17 个有
- `llama_cpp_model_loader` —— 12/17 个有
- `llama_cpp_parameters` —— 12/17 个有
- `ImageResizeKJv2` —— 10/17 个有
- `PrimitiveBoolean` —— 10/17 个有
- `ResizeImageMaskNode` —— 10/17 个有
- `PreviewAny` —— 9/17 个有
- `LTX2_NAG` —— 7/17 个有
- `Label (rgthree)` —— 5/17 个有
- `Fast Groups Bypasser (rgthree)` —— 4/17 个有
- `StringReplace` —— 4/17 个有
- `string_util_StrConcat` —— 4/17 个有
- `CR Text` —— 3/17 个有
- `CustomAddLabel` —— 3/17 个有
- `Int` —— 3/17 个有
- `RH_Utils` —— 3/17 个有
- `TTResolutionSelector` —— 3/17 个有
- `ttN concat` —— 3/17 个有
- `ImageStitch` —— 2/17 个有
- `LTXVImgToVideoInplaceKJ` —— 2/17 个有
- `MathExpression|pysssss` —— 2/17 个有
- `MultiTextConcatenate` —— 2/17 个有
- `RH_LLMAPI_Pro_Node` —— 2/17 个有
- `SimpleMath+` —— 2/17 个有
- `easy showAnything` —— 2/17 个有
- `JWFloat` —— 1/17 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 17 | 100% |
| 高度 | 25 | 25 - 25 | 17 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，17 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，17 个样本，取值集中（一致性 100%）
