---
key: 视频生成/文生视频/ltx23_inpaint_masked_Reference2Video 视频编辑工作流_2042807285466009602.json
name: ltx23_inpaint_masked_Reference2Video 视频编辑工作流_2042807285466009602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx23_inpaint_masked_Reference2Video 视频编辑工作流_2042807285466009602.json
hash: 33b56fd685d23b69
coverage: 0.387255
learned_at: 2026-10-10 23:08:38
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, GetImageSize, SolidMask, LTXVAudioVAEEncode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, VAEDecode, GetNode, LTXVConditioning, SimpleCalculatorKJ, GetNode, GetNode, GetNode, GetNode, VAEDecodeTiled, LTXVConcatAVLatent, Note, LTXVCropGuides, ImageScaleBy, GetNode, VAEEncode, easy cleanGpuUsed, SetNode, GetNode, GetNode, SetNode, GetNode, GrowMaskWithBlur, SetNode, GetNode, SetNode, SetNode, CFGGuider, GetNode, LTXVAddGuideMulti, GetNode, SamplerCustomAdvanced, VHS_VideoCombine, ImageConcanate, GetNode, GetNode, GetNode, LTXVEmptyLatentAudio, GetNode, SetNode, SetNode, SetNode, CLIPTextEncode, GetNode, SetNode, Note, SetNode, easy cleanGpuUsed, ReservedRegionFrameComposer, easy cleanGpuUsed, MaskToImage, GetNode, Note, GetNode, SetLatentNoiseMask, Reroute, GetNode, GetNode, GetNode, TrimAudioDuration, SetNode, Note, PreviewAudio, SetNode, Note, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, SAM3Segment, GetNode, VHS_VideoCombine, SetNode, ReservedRegionFrameComposer, KSamplerSelect, MarkdownNote, GetNode, BlockifyMask, GetNode, RandomNoise, SetNode, LTXVAudioVAEDecode, GetNode, GetNode, INTConstant, BasicScheduler, UNETLoader, UnetLoaderGGUF, SetNode, GetNode, GetNode, GetNode, LTXVLatentUpsampler, SetNode, GetNode, PrimitiveInt, LTXVPreprocess, SetNode, GetNode, LoraLoaderModelOnly, ImageScaleBy, LTXVAddGuideMulti, LTXVConcatAVLatent, CFGGuider, KSamplerSelect, ManualSigmas, SetNode, Fast Groups Bypasser (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcanate, GetNode, ImageConcanate, GetNode, GetNode, Note, LTXVCropGuides, SetNode, SetNode, SetNode, GetNode, ImageScaleBy, GetNode, ImageConcanate, VHS_VideoCombine, PrimitiveString, PrimitiveFloat, PrimitiveFloat, INTConstant, VHS_VideoCombine, EmptyImage, BlockifyMask, ImageCompositeFromMaskBatch+, Image Blank, ImageCompositeFromMaskBatch+, GetNode, Image Blank, GetImageSize+, ImageScaleBy, CheckpointLoaderSimple, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, CLIPTextEncode, LoadAudio, Note, LoraLoaderModelOnly, ManualSigmas, GetNode, SetNode, ResizeImageMaskNode, PreviewImage, Note, GetNode, GetNode, GetNode, GetNode, SAM3Segment, VHS_LoadVideo, PrimitiveFloat, SetNode, SetNode, RMBG, LoadImage, GetNode, VHS_VideoCombine, SetNode, GetNode, GrowMaskWithBlur, SetNode, MaskToImage, GetNode, GetImageSize+, LTXVSeparateAVLatent, GetNode, SamplerCustomAdvanced, RandomNoise, SetNode, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: [Image Blank, Image Blank, ImageCompositeFromMaskBatch+, ImageCompositeFromMaskBatch+, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, GetImageSize+, GetImageSize+]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
discoveries: [次要节点 `Image Blank` 知识库中没有该节点类型的任何知识, 次要节点 `Image Blank` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCompositeFromMaskBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCompositeFromMaskBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/ltx23_inpaint_masked_Reference2Video 视频编辑工作流_2042807285466009602.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx23_inpaint_masked_Reference2Video 视频编辑工作流_2042807285466009602.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（204 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVConditioning`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVConcatAVLatent`
- `Note`
- `LTXVCropGuides`
- `ImageScaleBy`
- `GetNode`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GrowMaskWithBlur`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `GetNode`
- `LTXVAddGuideMulti`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `ImageConcanate`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `Note`
- `SetNode`
- `easy cleanGpuUsed`
- `ReservedRegionFrameComposer`
- `easy cleanGpuUsed`
- `MaskToImage`
- `GetNode`
- `Note`
- `GetNode`
- `SetLatentNoiseMask`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `TrimAudioDuration`
- `SetNode`
- `Note`
- `PreviewAudio`
- `SetNode`
- `Note`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SAM3Segment`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `ReservedRegionFrameComposer`
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `GetNode`
- `BlockifyMask`
- `GetNode`
- `RandomNoise`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `INTConstant`
- `BasicScheduler`
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `SetNode`
- `GetNode`
- `PrimitiveInt`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleBy`
- `LTXVAddGuideMulti`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `GetNode`
- `ImageConcanate`
- `GetNode`
- `GetNode`
- `Note`
- `LTXVCropGuides`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageScaleBy`
- `GetNode`
- `ImageConcanate`
- `VHS_VideoCombine`
- `PrimitiveString`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `INTConstant`
- `VHS_VideoCombine`
- `EmptyImage`
- `BlockifyMask`
- `ImageCompositeFromMaskBatch+`
- `Image Blank`
- `ImageCompositeFromMaskBatch+`
- `GetNode`
- `Image Blank`
- `GetImageSize+`
- `ImageScaleBy`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `LoadAudio`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `GetNode`
- `SetNode`
- `ResizeImageMaskNode`
- `PreviewImage`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SAM3Segment`
- `VHS_LoadVideo`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `RMBG`
- `LoadImage`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GrowMaskWithBlur`
- `SetNode`
- `MaskToImage`
- `GetNode`
- `GetImageSize+`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **39%**（79/204）

**有卡**：`GetImageSize`、`SolidMask`、`LTXVAudioVAEEncode`、`VAEDecode`、`LTXVConditioning`、`SimpleCalculatorKJ`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`ImageScaleBy`、`VAEEncode`、`GrowMaskWithBlur`、`CFGGuider`、`LTXVAddGuideMulti`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`ImageConcanate`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`ReservedRegionFrameComposer`、`MaskToImage`、`SetLatentNoiseMask`、`TrimAudioDuration`、`PreviewAudio`、`LTXVSeparateAVLatent`、`SAM3Segment`、`KSamplerSelect`、`BlockifyMask`、`RandomNoise`、`LTXVAudioVAEDecode`、`INTConstant`、`BasicScheduler`、`UNETLoader`、`UnetLoaderGGUF`、`LTXVLatentUpsampler`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`ManualSigmas`、`EmptyImage`、`CheckpointLoaderSimple`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LoadAudio`、`ResizeImageMaskNode`、`VHS_LoadVideo`、`RMBG`、`LoadImage`

**缺卡**（9）：`Image Blank`、`Image Blank`、`ImageCompositeFromMaskBatch+`、`ImageCompositeFromMaskBatch+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`GetImageSize+`、`GetImageSize+`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 学习发现

- 次要节点 `Image Blank` 知识库中没有该节点类型的任何知识
- 次要节点 `Image Blank` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCompositeFromMaskBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCompositeFromMaskBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
