---
name: unknown_workflow_upscale_latent_upscale_lora_14
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.847846
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2061384649385009154.json, 视频生成/图生视频/2038518064030945282.json, 视频生成/图生视频/2031273311556079618.json, 视频生成/图生视频/2032374429937836033.json, 视频生成/图生视频/2032414154048413698.json, 视频生成/图生视频/2033429258751709185.json, 视频生成/图生视频/2033403811573800961.json, 视频生成/图生视频/2031361873404239873.json, 视频生成/图生视频/2036273219824521217.json, 视频生成/图生视频/2073405314405322753.json, 视频生成/图生视频/2033190788460453889.json, 视频生成/文生视频/LTX2.3-文生视频，智能提示词优化_2031263174128836610.json, 视频生成/文生视频/LTX2.3短剧_2042644046811766785.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_14

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2061384649385009154.json、视频生成/图生视频/2038518064030945282.json、视频生成/图生视频/2031273311556079618.json、视频生成/图生视频/2032374429937836033.json、视频生成/图生视频/2032414154048413698.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 13 个 workflow 都包含：
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
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 12/13 个有
- `PrimitiveStringMultiline` —— 12/13 个有
- `RH_LLMAPI_Pro_Node` —— 12/13 个有
- `PrimitiveInt` —— 10/13 个有
- `ResizeImageMaskNode` —— 10/13 个有
- `ResizeImagesByLongerEdge` —— 10/13 个有
- `PrimitiveBoolean` —— 7/13 个有
- `LTXVImgToVideoInplaceKJ` —— 6/13 个有
- `SimpleMath+` —— 6/13 个有
- `Int` —— 3/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/13 个有
- `FloatConstant` —— 2/13 个有
- `Resize` —— 2/13 个有
- `easy ifElse` —— 2/13 个有
- `BDXTestInt` —— 1/13 个有
- `EmptyImage` —— 1/13 个有
- `ImageSizeInfo` —— 1/13 个有
- `JoinStrings` —— 1/13 个有
- `MultiplicationNode` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `Qwen3_VQA` —— 1/13 个有
- `SaveImage` —— 1/13 个有
- `Text Multiline` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `easy mathInt` —— 1/13 个有

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
