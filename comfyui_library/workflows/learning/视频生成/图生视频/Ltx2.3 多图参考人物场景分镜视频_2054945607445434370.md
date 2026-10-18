---
key: 视频生成/图生视频/Ltx2.3 多图参考人物场景分镜视频_2054945607445434370.json
name: Ltx2.3 多图参考人物场景分镜视频_2054945607445434370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3 多图参考人物场景分镜视频_2054945607445434370.json
hash: 01288814e032928d
coverage: 0.573427
learned_at: 2026-10-15 22:37:54
nodes: [GetNode, GetNode, SetNode, SetNode, SetNode, SimpleCalculatorKJ, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, LatentUpscaleModelLoader, SetNode, DualCLIPLoader, VAELoaderKJ, VAELoader, VAELoader, GetNode, GetNode, GetNode, PrimitiveBoolean, LTXVAudioVAEDecode, GetNode, SetNode, AILab_QwenVL, SetNode, GetNode, ResizeImagesByLongerEdge, SetNode, ResizeImageMaskNode, GetNode, SetNode, easy convertAnything, SetNode, GetImageSize, ResizeImagesByLongerEdge, SetNode, GetNode, VAEDecodeTiled, GetNode, KSamplerSelect, GetNode, GetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, RandomNoise, LoraLoaderModelOnly, SetNode, CFGGuider, ManualSigmas, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, ImageBatchMulti, GetNode, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVEnhanceAVideoKJ, CLIPTextEncode, ImageClone, PrimitiveFloat, INTConstant, INTConstant, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, GetNode, GetNode, LTXVEnhanceAVideoKJ, LTXVConditioning, SetNode, SetNode, GetNode, LTXVConcatAVLatent, BasicScheduler, VisualizeSigmasKJ, STGGuiderAdvanced, LTXVAddGuideMulti, LTX2_NAG, Reroute, ImageResizeKJv2, VAEDecodeTiled, SimpleCalculatorKJ, SetNode, INTConstant, LTXVEmptyLatentAudio, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, LTXVPreprocess, CFGGuider, VHS_VideoCombine, VHS_GetImageCount, CreateVideo, LoadImage, GetImagesFromBatchIndexed, GetNode, RandomNoise, GetNode, KSamplerSelect, LTXVScheduler, ManualSigmas, GetNode, LTX2SamplingPreviewOverride, VHS_VideoCombine, MathExpression|pysssss, GetImageRangeFromBatch, LTXVSeparateAVLatent, LoadImage, LTXVAddGuidesFromBatch, LTXVAddGuide, UnetLoaderGGUF, LoraLoaderModelOnly, LTXVChunkFeedForward, PathchSageAttentionKJ, SetNode, LTXVChunkFeedForward, ModelPatchTorchSettings, UNETLoader, PromptRelayEncodeTimeline, Fast Groups Bypasser (rgthree), SeedGenerator]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/图生视频/Ltx2.3 多图参考人物场景分镜视频_2054945607445434370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054945607445434370.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（143 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoader`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveBoolean`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `AILab_QwenVL`
- `SetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `ResizeImageMaskNode`
- `GetNode`
- `SetNode`
- `easy convertAnything`
- `SetNode`
- `GetImageSize`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `CFGGuider`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `ImageBatchMulti`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVEnhanceAVideoKJ`
- `CLIPTextEncode` ★核心
- `ImageClone`
- `PrimitiveFloat`
- `INTConstant`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVEnhanceAVideoKJ`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `BasicScheduler`
- `VisualizeSigmasKJ`
- `STGGuiderAdvanced`
- `LTXVAddGuideMulti`
- `LTX2_NAG`
- `Reroute`
- `ImageResizeKJv2`
- `VAEDecodeTiled` ★核心
- `SimpleCalculatorKJ`
- `SetNode`
- `INTConstant`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `CFGGuider`
- `VHS_VideoCombine`
- `VHS_GetImageCount`
- `CreateVideo`
- `LoadImage`
- `GetImagesFromBatchIndexed`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `ManualSigmas`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `GetImageRangeFromBatch`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LTXVAddGuidesFromBatch`
- `LTXVAddGuide`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `SetNode`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `PromptRelayEncodeTimeline`
- `Fast Groups Bypasser (rgthree)`
- `SeedGenerator`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **57%**（82/143）

**有卡**：`SimpleCalculatorKJ`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`VAELoader`、`PrimitiveBoolean`、`LTXVAudioVAEDecode`、`AILab_QwenVL`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`easy convertAnything`、`GetImageSize`、`VAEDecodeTiled`、`KSamplerSelect`、`LoraLoaderModelOnly`、`RandomNoise`、`CFGGuider`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`ImageResizeKJv2`、`ImageBatchMulti`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVEnhanceAVideoKJ`、`CLIPTextEncode`、`ImageClone`、`INTConstant`、`LTXVConditioning`、`BasicScheduler`、`VisualizeSigmasKJ`、`STGGuiderAdvanced`、`LTXVAddGuideMulti`、`LTX2_NAG`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`VHS_VideoCombine`、`VHS_GetImageCount`、`CreateVideo`、`LoadImage`、`GetImagesFromBatchIndexed`、`LTXVScheduler`、`LTX2SamplingPreviewOverride`、`MathExpression|pysssss`、`GetImageRangeFromBatch`、`LTXVAddGuidesFromBatch`、`LTXVAddGuide`、`UnetLoaderGGUF`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`PromptRelayEncodeTimeline`、`SeedGenerator`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
