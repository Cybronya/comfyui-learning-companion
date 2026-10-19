---
name: unknown_workflow_upscale_latent_upscale_sampler_9
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8781
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2054757610527707137.json, 视频生成/图生视频/2031027294181003266.json, 视频生成/图生视频/2031010048406720514.json, 视频生成/图生视频/2058784933593837570.json, 视频生成/图生视频/2036368754602414082.json, 视频生成/图生视频/2036749082479304706.json, 视频生成/图生视频/2031034395125096450.json, 视频生成/图生视频/2040976928861069314.json, 视频生成/图生视频/2057838055628828673.json, 视频生成/图生视频/本地开源免费，真人短镜头3_2058240849422675970.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_9

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2054757610527707137.json、视频生成/图生视频/2031027294181003266.json、视频生成/图生视频/2031010048406720514.json、视频生成/图生视频/2058784933593837570.json、视频生成/图生视频/2036368754602414082.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
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
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `ResizeImagesByLongerEdge` —— 9/10 个有
- `ImageResizeKJv2` —— 8/10 个有
- `ResizeImageMaskNode` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `UNETLoader` —— 8/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `LTXVImgToVideoInplaceKJ` —— 4/10 个有
- `LTXVAddGuideMulti` —— 3/10 个有
- `EnhancedLoadDiffusionModel` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `VAELoader` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有
- `easy indexAnything` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `AspectRatio` —— 1/10 个有
- `BasicScheduler` —— 1/10 个有
- `CR Prompt Text` —— 1/10 个有
- `Int` —— 1/10 个有
- `LTX2_NAG` —— 1/10 个有
- `LoadAudio` —— 1/10 个有
- `ModelSamplingSD3` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `Switch` —— 1/10 个有
- `Vignette` —— 1/10 个有
- `VisualizeSigmasKJ` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
