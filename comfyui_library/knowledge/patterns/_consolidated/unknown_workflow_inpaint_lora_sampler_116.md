---
name: unknown_workflow_inpaint_lora_sampler_116
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8285
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, GetImageSize, GetVideoComponents, JWInteger, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuideAdvanced, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoConditionOnly, LTXVInpaintPreprocess, LTXVLaplacianPyramidBlend, LTXVPreprocess, LTXVSeparateAVLatent, LTXVSetAudioRefTokens, LTXVTiledVAEDecode, LoadImage, LoadVideo, LoraLoaderModelOnly, ManualSigmas, PreviewImage, PrimitiveBoolean, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled, VAEEncodeAudio, VAEEncodeTiled]
problems: []
missing: []
members: [平台全量/LTX-2.3-ICLORA视频局部重绘+自动优化提示词版V1_2067557746077159426.json, 视频生成/图生视频/LTX-2.3-ICLORA视频扩图+自动优化提示词版V1_2067552767505424386.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_116

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/LTX-2.3-ICLORA视频局部重绘+自动优化提示词版V1_2067557746077159426.json、视频生成/图生视频/LTX-2.3-ICLORA视频扩图+自动优化提示词版V1_2067552767505424386.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetVideoComponents`
- `JWInteger`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuideAdvanced`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoConditionOnly`
- `LTXVInpaintPreprocess`
- `LTXVLaplacianPyramidBlend`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LTXVSetAudioRefTokens`
- `LTXVTiledVAEDecode`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveBoolean`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`
- `VAEEncodeAudio`
- `VAEEncodeTiled`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 1/2 个有
- `DF_Get_image_size` —— 1/2 个有
- `GemmaAPITextEncode` —— 1/2 个有
- `INPAINT_ExpandMask` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImagePadForOutpaintTargetSize` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `LTXVDilateVideoMask` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `SAM3_Detect` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
