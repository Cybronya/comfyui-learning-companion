---
key: 视频生成/文生视频/LTX-2.3_图生_文生_视频工作流_2029830274397249538.json
name: LTX-2.3_图生_文生_视频工作流_2029830274397249538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3_图生_文生_视频工作流_2029830274397249538.json
hash: a01daf3ee62cc6f2
coverage: 0.474747
learned_at: 2026-10-15 22:44:42
nodes: [GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, EmptyLTXVLatentVideo, SetNode, SetNode, SetNode, PrimitiveFloat, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeTiled, LTXVConcatAVLatent, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, GetNode, SimpleCalculatorKJ, GetNode, GetNode, SetNode, GetNode, GetNode, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, INTConstant, INTConstant, SetNode, ResizeImageMaskNode, SetNode, SetNode, GetImageSize, ResizeImagesByLongerEdge, SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, SetNode, SetNode, LTXVPreprocess, ManualSigmas, LTXVScheduler, GetNode, GetNode, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVAudioVAEDecode, SimpleCalculatorKJ, INTConstant, RandomNoise, GetNode, CFGGuider, SamplerCustomAdvanced, RandomNoise, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, PrimitiveBoolean, MuyeTextEditOutput, LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, SetNode, SetNode, SetNode, SetNode, GetNode, LTXVConditioning, CLIPTextEncode, GetNode, DualCLIPLoaderGGUF, LoadImage, CLIPTextEncode, Power Lora Loader (rgthree), UNETLoader, GetNode, CFGGuider, SaveImage, SamplerCustomAdvanced, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/文生视频/LTX-2.3_图生_文生_视频工作流_2029830274397249538.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3_图生_文生_视频工作流_2029830274397249538.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `ResizeImageMaskNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `ManualSigmas`
- `LTXVScheduler`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `SimpleCalculatorKJ`
- `INTConstant`
- `RandomNoise`
- `GetNode`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveBoolean`
- `MuyeTextEditOutput`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `GetNode`
- `DualCLIPLoaderGGUF`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Power Lora Loader (rgthree)`
- `UNETLoader` ★核心
- `GetNode`
- `CFGGuider`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **47%**（47/99）

**有卡**：`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`KSamplerSelect`、`SimpleCalculatorKJ`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`INTConstant`、`ResizeImageMaskNode`、`GetImageSize`、`ResizeImagesByLongerEdge`、`ImageResizeKJv2`、`LTXVPreprocess`、`ManualSigmas`、`LTXVScheduler`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEDecode`、`RandomNoise`、`CFGGuider`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`MuyeTextEditOutput`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`LTXVConditioning`、`CLIPTextEncode`、`DualCLIPLoaderGGUF`、`LoadImage`、`Power Lora Loader (rgthree)`、`UNETLoader`、`SaveImage`、`VHS_VideoCombine`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、SaveImage、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
