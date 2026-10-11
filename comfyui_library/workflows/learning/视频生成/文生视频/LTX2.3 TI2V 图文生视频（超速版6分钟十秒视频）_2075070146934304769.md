---
key: 视频生成/文生视频/LTX2.3 TI2V 图文生视频（超速版6分钟十秒视频）_2075070146934304769.json
name: LTX2.3 TI2V 图文生视频（超速版6分钟十秒视频）_2075070146934304769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 TI2V 图文生视频（超速版6分钟十秒视频）_2075070146934304769.json
hash: 90b826ea92627e53
coverage: 0.478261
learned_at: 2026-10-11 20:38:34
nodes: [GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, MarkdownNote, GetNode, CFGGuider, MarkdownNote, MarkdownNote, MarkdownNote, ManualSigmas, MarkdownNote, GetNode, LTXVPreprocess, GetNode, GetNode, GetNode, LTX2SamplingPreviewOverride, SetNode, SetNode, LTX2_NAG, SetNode, SetNode, SetNode, SetNode, SetNode, VAELoaderKJ, VAELoader, VAELoader, GetNode, GetNode, SetNode, GetNode, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, GetNode, LTXVEmptyLatentAudio, GetNode, SimpleCalculatorKJ, GetNode, GetNode, LTXVConditioning, SetNode, SetNode, GetNode, KSamplerSelect, CFGGuider, GetNode, GetNode, LTXVLatentUpsampler, LTXVConcatAVLatent, SamplerCustomAdvanced, SimpleCalculatorKJ, SetNode, MarkdownNote, LTXVConcatAVLatent, GetNode, GetNode, GetNode, LTXVImgToVideoInplace, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, SetNode, SetNode, KSamplerSelect, ManualSigmas, VHS_VideoCombine, GetNode, GetImageSize, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, ResizeImagesByLongerEdge, SetNode, INTConstant, INTConstant, PrimitiveFloat, MarkdownNote, ManualSigmas, VHS_VideoCombine, Note, Fast Groups Bypasser (rgthree), LTXVScheduler, ImageScaleBy, DualCLIPLoader, GetNode, INTConstant, LoadImage, VHS_VideoCombine, PathchSageAttentionKJ, ModelPatchTorchSettings, UNETLoader, SetNode, RandomNoise, easy cleanGpuUsed, ShowText|pysssss, PrimitiveStringMultiline, llama_cpp_model_loader, llama_cpp_instruct_adv, GetNode, PrimitiveBoolean, Note, LatentUpscaleModelLoader, ImageResizeKJv2, ImageScaleBy, LoadImage, SaveImage]
patterns: []
missing: [easy cleanGpuUsed]
parameters: {"batch_size": 1, "height": 24, "width": 121}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3 TI2V 图文生视频（超速版6分钟十秒视频）_2075070146934304769.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 TI2V 图文生视频（超速版6分钟十秒视频）_2075070146934304769.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（115 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `GetNode`
- `CFGGuider`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ManualSigmas`
- `MarkdownNote`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `SetNode`
- `SetNode`
- `LTX2_NAG`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoader`
- `VAELoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SimpleCalculatorKJ`
- `SetNode`
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VHS_VideoCombine`
- `GetNode`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `PrimitiveFloat`
- `MarkdownNote`
- `ManualSigmas`
- `VHS_VideoCombine`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `LTXVScheduler`
- `ImageScaleBy`
- `DualCLIPLoader`
- `GetNode`
- `INTConstant`
- `LoadImage`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `SetNode`
- `RandomNoise`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `GetNode`
- `PrimitiveBoolean`
- `Note`
- `LatentUpscaleModelLoader`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `LoadImage`
- `SaveImage`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **48%**（55/115）

**有卡**：`CFGGuider`、`ManualSigmas`、`LTXVPreprocess`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`VAELoaderKJ`、`VAELoader`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SimpleCalculatorKJ`、`LTXVConditioning`、`KSamplerSelect`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`GetImageSize`、`CLIPTextEncode`、`ResizeImagesByLongerEdge`、`INTConstant`、`LTXVScheduler`、`ImageScaleBy`、`DualCLIPLoader`、`LoadImage`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`RandomNoise`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`PrimitiveBoolean`、`LatentUpscaleModelLoader`、`ImageResizeKJv2`、`SaveImage`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
