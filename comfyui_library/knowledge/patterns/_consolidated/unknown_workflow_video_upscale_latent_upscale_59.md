---
name: unknown_workflow_video_upscale_latent_upscale_59
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.704
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2041388395624140802.json, 视频生成/图生视频/2040449259794866177.json, 视频生成/图生视频/2041694294079184898.json, 视频生成/图生视频/2037153504921391105.json, 视频生成/图生视频/2041110942255161346.json, 视频生成/图生视频/2051128498395336706.json, 视频生成/图生视频/2063264536383287297.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_59

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2041388395624140802.json、视频生成/图生视频/2040449259794866177.json、视频生成/图生视频/2041694294079184898.json、视频生成/图生视频/2037153504921391105.json、视频生成/图生视频/2041110942255161346.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
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
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `SimpleMath+` —— 5/7 个有
- `CustomAddLabel` —— 4/7 个有
- `GetNode` —— 4/7 个有
- `LoraLoader` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `CreateVideo` —— 3/7 个有
- `LTXVAddGuideMulti` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `RH_LLMAPI_Pro_Node` —— 3/7 个有
- `TTResolutionSelector` —— 3/7 个有
- `JWFloat` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `PrimitiveBoolean` —— 2/7 个有
- `ResizeImageMaskNode` —— 2/7 个有
- `llama_cpp_instruct_adv` —— 2/7 个有
- `llama_cpp_model_loader` —— 2/7 个有
- `llama_cpp_parameters` —— 2/7 个有
- `Dapao_LlamaCaption` —— 1/7 个有
- `Dapao_LlamaCaptionOptions` —— 1/7 个有
- `GetVideoComponents` —— 1/7 个有
- `MultiTextConcatenate` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `RH_Utils` —— 1/7 个有
- `RegexReplace` —— 1/7 个有
- `ShowText` —— 1/7 个有
- `Text` —— 1/7 个有
- `ttN concat` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
