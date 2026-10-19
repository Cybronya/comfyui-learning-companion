---
name: unknown_workflow_upscale_latent_upscale_lora_46
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.837667
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RH_LLMAPI_Pro_Node, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2073317124101201921.json, 视频生成/图生视频/2035320209401192449.json, 视频生成/图生视频/2033038199701905410.json, 视频生成/图生视频/2033197165668999170.json, 视频生成/图生视频/2033156764371263490.json, 视频生成/图生视频/2044341747362304001.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_46

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2073317124101201921.json、视频生成/图生视频/2035320209401192449.json、视频生成/图生视频/2033038199701905410.json、视频生成/图生视频/2033197165668999170.json、视频生成/图生视频/2033156764371263490.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LTXVEmptyLatentAudio` —— 5/6 个有
- `LTXVImgToVideoInplace` —— 5/6 个有
- `LTXVLatentUpsampler` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `FloatConstant` —— 4/6 个有
- `LTXVChunkFeedForward` —— 4/6 个有
- `LTXVImgToVideoInplaceKJ` —— 4/6 个有
- `ModelPatchTorchSettings` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `ResizeImageMaskNode` —— 4/6 个有
- `SimpleMath+` —— 4/6 个有
- `Resize` —— 3/6 个有
- `PrimitiveBoolean` —— 2/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `Bjornulf_ShowInt` —— 1/6 个有
- `CM_FloatToInt` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `CR String To Combo` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `ImpactStringSelector` —— 1/6 个有
- `LTXAddVideoICLoRAGuide` —— 1/6 个有
- `LTXICLoRALoaderModelOnly` —— 1/6 个有
- `LTXVAudioVAEEncode` —— 1/6 个有
- `LTXVImgToVideoConditionOnly` —— 1/6 个有
- `PainterAudioLength` —— 1/6 个有
- `SaveAudio` —— 1/6 个有
- `SetLatentNoiseMask` —— 1/6 个有
- `SolidMask` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `kkResize` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
