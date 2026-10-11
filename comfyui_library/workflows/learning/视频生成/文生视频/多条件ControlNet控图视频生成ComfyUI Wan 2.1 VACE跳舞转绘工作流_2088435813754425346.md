---
key: 视频生成/文生视频/多条件ControlNet控图视频生成ComfyUI Wan 2.1 VACE跳舞转绘工作流_2088435813754425346.json
name: 多条件ControlNet控图视频生成ComfyUI Wan 2.1 VACE跳舞转绘工作流_2088435813754425346
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/多条件ControlNet控图视频生成ComfyUI Wan 2.1 VACE跳舞转绘工作流_2088435813754425346.json
hash: 96653af6d29763c3
coverage: 0.582418
learned_at: 2026-10-11 20:53:53
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, SetNode, GetNode, WanVideoTextEncode, SetNode, SetNode, SetNode, WanVideoDecode, SetNode, DWPreprocessor, INTConstant, INTConstant, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, GetNode, INTConstant, WanVideoSampler, WanVideoVACEEncode, VHS_VideoCombine, VHS_VideoCombine, AIO_Preprocessor, WanVideoVACEEncode, StringConstantMultiline, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoVACEModelSelect, WanVideoLoraSelect, VHS_LoadVideo, LoadImage, Fast Groups Bypasser (rgthree), VHS_VideoCombine, SetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, PreviewImage, LoadImage, SetNode, GetNode, GetNode, GetNode, SetNode, DWPreprocessor, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: [LayerUtility: PurgeVRAM]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/多条件ControlNet控图视频生成ComfyUI Wan 2.1 VACE跳舞转绘工作流_2088435813754425346.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/多条件ControlNet控图视频生成ComfyUI Wan 2.1 VACE跳舞转绘工作流_2088435813754425346.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `WanVideoTextEncode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoDecode`
- `SetNode`
- `DWPreprocessor`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoVACEEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `AIO_Preprocessor`
- `WanVideoVACEEncode`
- `StringConstantMultiline`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `VHS_LoadVideo`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `DWPreprocessor`
- `孤海注释`
- `孤海注释`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **58%**（53/91）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoDecode`、`DWPreprocessor`、`INTConstant`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoVACEEncode`、`VHS_VideoCombine`、`AIO_Preprocessor`、`StringConstantMultiline`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoInfo`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`

**缺卡**（1）：`LayerUtility: PurgeVRAM`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
