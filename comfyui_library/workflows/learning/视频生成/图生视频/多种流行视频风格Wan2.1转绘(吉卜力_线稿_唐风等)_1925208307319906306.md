---
key: 视频生成/图生视频/多种流行视频风格Wan2.1转绘(吉卜力_线稿_唐风等)_1925208307319906306.json
name: 多种流行视频风格Wan2.1转绘(吉卜力_线稿_唐风等)_1925208307319906306.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/多种流行视频风格Wan2.1转绘(吉卜力_线稿_唐风等)_1925208307319906306.json
hash: cb80bdffb2128964
coverage: 0.757009
learned_at: 2026-10-15 22:29:51
nodes: [SetNode, GetNode, GetNode, GetNode, SetNode, Note, Note, MarkdownNote, SetNode, WanVideoTextEncode, GetNode, GetNode, Text Concatenate, Fast Groups Bypasser (rgthree), WanVideoModelLoader, WanVideoTorchCompileSettings, MarkdownNote, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoVACEModelSelect, WanVideoVACEEncode, GetNode, AddLabel, AddLabel, GetNode, WanVideoSampler, Primitive integer [Crystools], LoadImage, ImageResizeKJ, ImagePadKJ, SetNode, SetNode, GetImageSizeAndCount, VHS_VideoCombine, Reroute, ImageConcatMulti, GetImageSizeAndCount, EmptyImage, ImageConcatMulti, ImageResizeKJ, AIO_Preprocessor, ImageBlend, AIO_Preprocessor, BasicGuider, RandomNoise, KSamplerSelect, DualCLIPLoader, VAEDecode, PreviewImage, CLIPTextEncode, CLIPTextEncode, FluxGuidance, SamplerCustomAdvanced, ImageConcanate, ImageConcanate, easy cleanGpuUsed, Reroute, DownloadAndLoadFlorence2Model, Florence2Run, RH_Captioner, PreviewImage, VHS_LoadVideo, Primitive integer [Crystools], Primitive integer [Crystools], RepeatLatentBatch, WanVideoLoraSelect, ControlNetLoader, VAELoader, VAEEncode, ApplyFBCacheOnModel, ControlNetApplyAdvanced, BasicScheduler, AIO_Preprocessor, SetUnionControlNetType, GetImageRangeFromBatch, ShowText|pysssss, Primitive integer [Crystools], Text Concatenate, easy anythingIndexSwitch, Text Multiline, LoraLoaderModelOnly, ShowText|pysssss, WanVideoDecode, ColorMatch, VHS_VideoCombine, VHS_VideoCombine, DWPreprocessor, LoraLoaderModelOnly, Text Multiline, Text Multiline, UNETLoader, LoraLoaderModelOnly, SaveImage, Text Multiline, Note, Note, Text Multiline, RH_Captioner, easy anythingIndexSwitch, Text Multiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Text Multiline, Note, Primitive integer [Crystools], WanVideoBlockSwap]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.8000000000000002}
---

# 视频生成/图生视频/多种流行视频风格Wan2.1转绘(吉卜力_线稿_唐风等)_1925208307319906306.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1925208307319906306.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Note`
- `Note`
- `MarkdownNote`
- `SetNode`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `Text Concatenate`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `MarkdownNote`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVACEModelSelect`
- `WanVideoVACEEncode`
- `GetNode`
- `AddLabel`
- `AddLabel`
- `GetNode`
- `WanVideoSampler` ★核心
- `Primitive integer [Crystools]`
- `LoadImage`
- `ImageResizeKJ`
- `ImagePadKJ`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `Reroute`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `EmptyImage`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `AIO_Preprocessor`
- `ImageBlend`
- `AIO_Preprocessor`
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `Reroute`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `RH_Captioner`
- `PreviewImage`
- `VHS_LoadVideo`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `RepeatLatentBatch`
- `WanVideoLoraSelect`
- `ControlNetLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `ApplyFBCacheOnModel`
- `ControlNetApplyAdvanced` ★核心
- `BasicScheduler`
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `GetImageRangeFromBatch`
- `ShowText|pysssss`
- `Primitive integer [Crystools]`
- `Text Concatenate`
- `easy anythingIndexSwitch`
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `ShowText|pysssss`
- `WanVideoDecode`
- `ColorMatch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `LoraLoaderModelOnly` ★核心
- `Text Multiline`
- `Text Multiline`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Text Multiline`
- `Note`
- `Note`
- `Text Multiline`
- `RH_Captioner`
- `easy anythingIndexSwitch`
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text Multiline`
- `Note`
- `Primitive integer [Crystools]`
- `WanVideoBlockSwap`

## 关键参数

- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **76%**（81/107）

**有卡**：`WanVideoTextEncode`、`Text Concatenate`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVACEModelSelect`、`WanVideoVACEEncode`、`AddLabel`、`WanVideoSampler`、`Primitive integer [Crystools]`、`LoadImage`、`ImageResizeKJ`、`ImagePadKJ`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`ImageConcatMulti`、`EmptyImage`、`AIO_Preprocessor`、`ImageBlend`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`DualCLIPLoader`、`VAEDecode`、`CLIPTextEncode`、`FluxGuidance`、`SamplerCustomAdvanced`、`ImageConcanate`、`easy cleanGpuUsed`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`RH_Captioner`、`VHS_LoadVideo`、`RepeatLatentBatch`、`WanVideoLoraSelect`、`ControlNetLoader`、`VAELoader`、`VAEEncode`、`ApplyFBCacheOnModel`、`ControlNetApplyAdvanced`、`BasicScheduler`、`SetUnionControlNetType`、`GetImageRangeFromBatch`、`easy anythingIndexSwitch`、`Text Multiline`、`LoraLoaderModelOnly`、`WanVideoDecode`、`ColorMatch`、`DWPreprocessor`、`UNETLoader`、`SaveImage`、`WanVideoBlockSwap`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
