---
name: unknown_workflow_sampler_unet_vae_28
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.906533
common_nodes: [CFGGuider, ComfyMathExpression, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LoadImage, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2052341800647569410.json, 视频生成/图生视频/2039999501695459329.json, 视频生成/图生视频/2039365637025304577.json, 视频生成/图生视频/2038953510800199682.json, 视频生成/图生视频/2039330537847922689.json, 视频生成/图生视频/2039363002973032450.json, 视频生成/图生视频/2040690570988883969.json, 视频生成/图生视频/2031244973215064065.json, 视频生成/图生视频/2031018191203340289.json, 视频生成/图生视频/2040716663120732161.json, 视频生成/图生视频/2037880867695108098.json, 视频生成/图生视频/2037157386359672834.json, 视频生成/图生视频/2037707002851364865.json, 视频生成/图生视频/2038548270510776322.json, 视频生成/图生视频/2037742707522670593.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_28

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/2052341800647569410.json、视频生成/图生视频/2039999501695459329.json、视频生成/图生视频/2039365637025304577.json、视频生成/图生视频/2038953510800199682.json、视频生成/图生视频/2039330537847922689.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGGuider`
- `ComfyMathExpression`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 14/15 个有
- `LTXVLatentUpsampler` —— 14/15 个有
- `LTXVPreprocess` —— 14/15 个有
- `LatentUpscaleModelLoader` —— 14/15 个有
- `ManualSigmas` —— 14/15 个有
- `SimpleMath+` —— 14/15 个有
- `LoraLoaderModelOnly` —— 13/15 个有
- `ShowText|pysssss` —— 12/15 个有
- `LTXVAddGuideMulti` —— 11/15 个有
- `Text` —— 10/15 个有
- `easy cleanGpuUsed` —— 9/15 个有
- `llama_cpp_instruct_adv` —— 9/15 个有
- `llama_cpp_model_loader` —— 9/15 个有
- `AspectRatio` —— 5/15 个有
- `ImageConcanate` —— 5/15 个有
- `RH_LLMAPI_Pro_Node` —— 3/15 个有
- `ImageSizeInfo` —— 2/15 个有
- `PrimitiveStringMultiline` —— 2/15 个有
- `llama_cpp_unload_model` —— 2/15 个有
- `BasicScheduler` —— 1/15 个有
- `ConditioningZeroOut` —— 1/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `ImageConcatMulti` —— 1/15 个有
- `Int` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `PrimitiveFloat` —— 1/15 个有
- `PromptRelayEncodeTimeline` —— 1/15 个有
- `easy showAnything` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 193 | 15 | 77% |
| 高度 | 25 | 25 - 25 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 193，15 个样本
- 高度 中位数 25，观测区间 25 - 25，15 个样本，取值集中（一致性 100%）
