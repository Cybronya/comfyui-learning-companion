---
key: 视频生成/文生视频/LTX 2.3 参考引导局部重绘工作流_2041676758285553666.json
name: LTX 2.3 参考引导局部重绘工作流_2041676758285553666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 参考引导局部重绘工作流_2041676758285553666.json
hash: 1b9be3554f2724d6
coverage: 0.475962
learned_at: 2026-10-15 22:44:32
nodes: [SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetImageSize, SolidMask, LTXVAudioVAEEncode, GetNode, SetNode, GetNode, VAELoaderKJ, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, VAELoaderKJ, SetNode, RecordAudio, GetNode, GetNode, GetNode, LTXVCropGuides, SamplerCustomAdvanced, SetNode, GetNode, LTXVEmptyLatentAudio, GetNode, SetNode, GetNode, RandomNoise, LTXVConditioning, GetNode, SimpleCalculatorKJ, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, CLIPTextEncode, GetNode, GetNode, KSamplerSelect, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, SetNode, GetNode, GetNode, LTXVConcatAVLatent, Reroute, SetLatentNoiseMask, Note, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, PrimitiveFloat, SetNode, ManualSigmas, EmptyAudio, SetNode, TrimAudioDuration, Note, CFGGuider, BlockifyMask, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcanate, VHS_VideoCombine, ManualSigmas, KSamplerSelect, CFGGuider, BasicScheduler, Note, easy cleanGpuUsed, ImageConcanate, ImageConcanate, ImageScaleBy, GetNode, SetNode, GetNode, MarkdownNote, BlockifyMask, ImageCompositeFromMaskBatch+, GetNode, ImageCompositeFromMaskBatch+, GrowMaskWithBlur, GetNode, SetNode, GetNode, GetNode, ImageConcanate, GetNode, GetNode, GrowMaskWithBlur, Note, SetNode, SetNode, INTConstant, ReservedRegionFrameComposer, PrimitiveFloat, Note, Note, GetImageSize+, LoadAudio, DualCLIPLoader, PrimitiveFloat, BiRefNetRMBG, GetNode, EmptyImage, SetNode, GetNode, GetNode, easy cleanGpuUsed, UNETLoader, SetNode, VAEEncode, GetNode, SetNode, LTXVSeparateAVLatent, VAEDecode, VAEDecode, GetNode, ResizeImageMaskNode, SeCModelLoader_Ultra-Fast, GetNode, ImageFromBatch+, PreviewImage, SetNode, SetNode, LTXVPreprocess, PreviewImage, SeCVideoSegmentation_Ultra-Fast, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SetNode, ImageFromBatch+, DF_Get_image_size, ReservedRegionFrameComposer, easy mathInt, DF_Get_image_size, easy mathInt, EmptyImage, SeCModelLoader_Ultra-Fast, easy cleanGpuUsed, SeCVideoSegmentation_Ultra-Fast, SetNode, LTXVAddGuideMulti, LatentUpscaleModelLoader, GetNode, GetNode, LTXVLatentUpsampler, GetNode, LTXVAddGuideMulti, GetNode, GetNode, INTConstant, GetImageSize+, GetNode, GetNode, GetNode, ImageFromBatch+, PreviewImage, PrimitiveInt, VHS_VideoCombine, VHS_VideoCombine, SetNode, LoadImage, GetNode, CLIPTextEncode, llama_cpp_model_loader, JWImageResizeByLongerSide, JWImageResizeByLongerSide, easy showAnything, String Literal, JWStringConcat, VHS_LoadVideo, VRAMReserver, LoadImage, llama_cpp_instruct_adv, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageScaleBy, VHS_VideoCombine, GetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/文生视频/LTX 2.3 参考引导局部重绘工作流_2041676758285553666.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3 参考引导局部重绘工作流_2041676758285553666.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（208 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `RecordAudio`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `RandomNoise`
- `LTXVConditioning`
- `GetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `Reroute`
- `SetLatentNoiseMask`
- `Note`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `PrimitiveFloat`
- `SetNode`
- `ManualSigmas`
- `EmptyAudio`
- `SetNode`
- `TrimAudioDuration`
- `Note`
- `CFGGuider`
- `BlockifyMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `VHS_VideoCombine`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `BasicScheduler`
- `Note`
- `easy cleanGpuUsed`
- `ImageConcanate`
- `ImageConcanate`
- `ImageScaleBy`
- `GetNode`
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `BlockifyMask`
- `ImageCompositeFromMaskBatch+`
- `GetNode`
- `ImageCompositeFromMaskBatch+`
- `GrowMaskWithBlur`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `GetNode`
- `GetNode`
- `GrowMaskWithBlur`
- `Note`
- `SetNode`
- `SetNode`
- `INTConstant`
- `ReservedRegionFrameComposer`
- `PrimitiveFloat`
- `Note`
- `Note`
- `GetImageSize+`
- `LoadAudio`
- `DualCLIPLoader`
- `PrimitiveFloat`
- `BiRefNetRMBG`
- `GetNode`
- `EmptyImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `SetNode`
- `VAEEncode` ★核心
- `GetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `ResizeImageMaskNode`
- `SeCModelLoader_Ultra-Fast`
- `GetNode`
- `ImageFromBatch+`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `PreviewImage`
- `SeCVideoSegmentation_Ultra-Fast`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `ImageFromBatch+`
- `DF_Get_image_size`
- `ReservedRegionFrameComposer`
- `easy mathInt`
- `DF_Get_image_size`
- `easy mathInt`
- `EmptyImage`
- `SeCModelLoader_Ultra-Fast`
- `easy cleanGpuUsed`
- `SeCVideoSegmentation_Ultra-Fast`
- `SetNode`
- `LTXVAddGuideMulti`
- `LatentUpscaleModelLoader`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `LTXVAddGuideMulti`
- `GetNode`
- `GetNode`
- `INTConstant`
- `GetImageSize+`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch+`
- `PreviewImage`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `LoadImage`
- `GetNode`
- `CLIPTextEncode` ★核心
- `llama_cpp_model_loader`
- `JWImageResizeByLongerSide`
- `JWImageResizeByLongerSide`
- `easy showAnything`
- `String Literal`
- `JWStringConcat`
- `VHS_LoadVideo`
- `VRAMReserver`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScaleBy`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **48%**（99/208）

**有卡**：`GetImageSize`、`SolidMask`、`LTXVAudioVAEEncode`、`VAELoaderKJ`、`RecordAudio`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`RandomNoise`、`LTXVConditioning`、`SimpleCalculatorKJ`、`CLIPTextEncode`、`KSamplerSelect`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SetLatentNoiseMask`、`LTXVSeparateAVLatent`、`ManualSigmas`、`EmptyAudio`、`TrimAudioDuration`、`CFGGuider`、`BlockifyMask`、`ImageConcanate`、`VHS_VideoCombine`、`BasicScheduler`、`easy cleanGpuUsed`、`ImageScaleBy`、`ImageCompositeFromMaskBatch+`、`GrowMaskWithBlur`、`INTConstant`、`ReservedRegionFrameComposer`、`GetImageSize+`、`LoadAudio`、`DualCLIPLoader`、`BiRefNetRMBG`、`EmptyImage`、`UNETLoader`、`VAEEncode`、`VAEDecode`、`ResizeImageMaskNode`、`SeCModelLoader_Ultra-Fast`、`ImageFromBatch+`、`LTXVPreprocess`、`SeCVideoSegmentation_Ultra-Fast`、`DF_Get_image_size`、`easy mathInt`、`LTXVAddGuideMulti`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LoadImage`、`llama_cpp_model_loader`、`JWImageResizeByLongerSide`、`String Literal`、`JWStringConcat`、`VHS_LoadVideo`、`VRAMReserver`、`llama_cpp_instruct_adv`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
