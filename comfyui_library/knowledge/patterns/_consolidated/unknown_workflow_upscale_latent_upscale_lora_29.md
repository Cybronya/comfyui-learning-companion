---
name: unknown_workflow_upscale_latent_upscale_lora_29
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.843
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, FloatConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RH_LLMAPI_Pro_Node, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecodeTiled, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2033197165668999170.json, 视频生成/图生视频/2033156764371263490.json, 视频生成/图生视频/2044341747362304001.json, 视频生成/图生视频/2049303254957297665.json, 视频生成/图生视频/2052949271544123393.json, 视频生成/图生视频/2047731840944967682.json, 视频生成/图生视频/2044586983204327425.json, 视频生成/图生视频/2052216878214467585.json, 视频生成/图生视频/2051164751694184449.json, 视频生成/图生视频/2038794251055669250.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_29

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2033197165668999170.json、视频生成/图生视频/2033156764371263490.json、视频生成/图生视频/2044341747362304001.json、视频生成/图生视频/2049303254957297665.json、视频生成/图生视频/2052949271544123393.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
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
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 9/10 个有
- `LTXVChunkFeedForward` —— 9/10 个有
- `LTXVEmptyLatentAudio` —— 9/10 个有
- `ModelPatchTorchSettings` —— 9/10 个有
- `PathchSageAttentionKJ` —— 9/10 个有
- `SaveVideo` —— 9/10 个有
- `SimpleMath+` —— 9/10 个有
- `Resize` —— 3/10 个有
- `ResizeImageMaskNode` —— 3/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `kkResize` —— 2/10 个有
- `AILab_QwenVL` —— 1/10 个有
- `Bjornulf_ShowInt` —— 1/10 个有
- `CM_FloatToInt` —— 1/10 个有
- `CR Prompt Text` —— 1/10 个有
- `CombineImagesForQwen3VL` —— 1/10 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `INTConstant` —— 1/10 个有
- `ImageResize+` —— 1/10 个有
- `LTXVAudioVAEEncode` —— 1/10 个有
- `PainterAudioLength` —— 1/10 个有
- `ResizeAndPadImage` —— 1/10 个有
- `SaveAudio` —— 1/10 个有
- `SetLatentNoiseMask` —— 1/10 个有
- `SolidMask` —— 1/10 个有
- `TextCombinerTwo` —— 1/10 个有
- `VHS_VideoCombine` —— 1/10 个有

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
