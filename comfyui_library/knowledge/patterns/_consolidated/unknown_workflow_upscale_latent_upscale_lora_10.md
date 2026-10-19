---
name: unknown_workflow_upscale_latent_upscale_lora_10
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.872167
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, FloatConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2052949271544123393.json, 视频生成/图生视频/2047731840944967682.json, 视频生成/图生视频/2044586983204327425.json, 视频生成/图生视频/2052216878214467585.json, 视频生成/图生视频/2051164751694184449.json, 视频生成/图生视频/2035325465820405761.json, 视频生成/图生视频/2038794251055669250.json, 视频生成/图生视频/2042205939977162753.json, 视频生成/图生视频/2042240826851463170.json, 视频生成/图生视频/2063794873710501890.json, 视频生成/图生视频/2051490555791720450.json, 视频生成/图生视频/2051660543777361922.json, 视频生成/图生视频/2042812427200372738.json, 视频生成/图生视频/2051217425542201345.json, 视频生成/图生视频/2051911216334942209.json, 视频生成/图生视频/2054734557966020610.json, 视频生成/图生视频/2050610398684041217.json, 视频生成/图生视频/2051654152509501441.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_10

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/2052949271544123393.json、视频生成/图生视频/2047731840944967682.json、视频生成/图生视频/2044586983204327425.json、视频生成/图生视频/2052216878214467585.json、视频生成/图生视频/2051164751694184449.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `FloatConstant`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVChunkFeedForward` —— 17/18 个有
- `LoadImage` —— 17/18 个有
- `ModelPatchTorchSettings` —— 17/18 个有
- `PathchSageAttentionKJ` —— 17/18 个有
- `RH_LLMAPI_Pro_Node` —— 17/18 个有
- `SimpleMath+` —— 17/18 个有
- `LTXVPreprocess` —— 16/18 个有
- `CreateVideo` —— 14/18 个有
- `ResizeImagesByLongerEdge` —— 14/18 个有
- `SaveVideo` —— 14/18 个有
- `PrimitiveStringMultiline` —— 12/18 个有
- `CR Prompt Text` —— 6/18 个有
- `DualCLIPLoader` —— 6/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/18 个有
- `PreviewAny` —— 6/18 个有
- `TextGenerateLTX2Prompt` —— 6/18 个有
- `ImageResizeKJv2` —— 5/18 个有
- `ResizeImageMaskNode` —— 5/18 个有
- `TextCombinerTwo` —— 4/18 个有
- `VHS_VideoCombine` —— 4/18 个有
- `easy int` —— 3/18 个有
- `ColorMatchV2` —— 2/18 个有
- `Fast Groups Bypasser (rgthree)` —— 2/18 个有
- `PreviewImage` —— 2/18 个有
- `Resize` —— 2/18 个有
- `CR Text Concatenate` —— 1/18 个有
- `Image Resize` —— 1/18 个有
- `ImageResize+` —— 1/18 个有
- `RHHiddenNodes` —— 1/18 个有
- `RH_RhartImageG2TextToImage` —— 1/18 个有
- `ResizeAndPadImage` —— 1/18 个有
- `kkResize` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 18 | 100% |
| 高度 | 25 | 25 - 25 | 18 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，18 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，18 个样本，取值集中（一致性 100%）
