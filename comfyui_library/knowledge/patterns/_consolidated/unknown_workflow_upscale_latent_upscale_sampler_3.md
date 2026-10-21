---
name: unknown_workflow_upscale_latent_upscale_sampler_3
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.872667
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2037403697717714946.json, 视频生成/图生视频/2037865194449281026.json, 视频生成/图生视频/2054921122281467905.json, 视频生成/图生视频/2054919936321040385.json, 视频生成/图生视频/2058534614507024386.json, 视频生成/图生视频/2031027294181003266.json, 视频生成/图生视频/2031010048406720514.json, 视频生成/图生视频/2058784933593837570.json, 视频生成/图生视频/2036368754602414082.json, 视频生成/图生视频/2036749082479304706.json, 视频生成/图生视频/2031034395125096450.json, 视频生成/图生视频/2048705684543381506.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_3

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/2037403697717714946.json、视频生成/图生视频/2037865194449281026.json、视频生成/图生视频/2054921122281467905.json、视频生成/图生视频/2054919936321040385.json、视频生成/图生视频/2058534614507024386.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
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
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 10/12 个有
- `PrimitiveStringMultiline` —— 10/12 个有
- `ResizeImageMaskNode` —— 9/12 个有
- `VHS_VideoCombine` —— 8/12 个有
- `CreateVideo` —— 7/12 个有
- `LoraLoaderModelOnly` —— 7/12 个有
- `LTXVChunkFeedForward` —— 6/12 个有
- `ModelPatchTorchSettings` —— 6/12 个有
- `PathchSageAttentionKJ` —— 6/12 个有
- `PrimitiveBoolean` —— 6/12 个有
- `LTXVImgToVideoInplaceKJ` —— 5/12 个有
- `SaveVideo` —— 4/12 个有
- `LTX2_NAG` —— 3/12 个有
- `LTXVAddGuideMulti` —— 3/12 个有
- `INTConstant` —— 2/12 个有
- `LayerUtility: PurgeVRAM` —— 2/12 个有
- `PromptRelaySmartEncode` —— 2/12 个有
- `easy ifElse` —— 2/12 个有
- `FloatConstant` —— 1/12 个有
- `ImageAddMulti` —— 1/12 个有
- `LTXAddVideoICLoRAGuideAdvanced` —— 1/12 个有
- `LTXICLoRALoaderModelOnly` —— 1/12 个有
- `PromptRelayEncodeTimeline` —— 1/12 个有
- `RH_LLMAPI_Pro_Node` —— 1/12 个有
- `SimpleMath+` —— 1/12 个有
- `VAELoader` —— 1/12 个有
- `easy imageRemBg` —— 1/12 个有
- `easy showAnything` —— 1/12 个有
- `孤海图像缩放按像素` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 44 | 12 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 44，12 个样本
