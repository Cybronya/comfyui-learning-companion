---
key: 视频生成/文生视频/文生视频  wan2.2真人转动漫_2041329650097463297.json
name: 文生视频  wan2.2真人转动漫_2041329650097463297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频  wan2.2真人转动漫_2041329650097463297.json
hash: 5749a494e2627ad0
coverage: 0.963636
learned_at: 2026-10-15 22:48:41
nodes: [CLIPSetLastLayer, FreeU_V2, ADE_StandardStaticContextOptions, VHS_VideoCombine, VAEDecode, KSamplerAdvanced //Inspire, BNK_CLIPTextEncodeAdvanced, VAEEncode, DWPreprocessor, ControlNetApplyAdvanced, AIO_Preprocessor, ControlNetApplyAdvanced, ControlNetApplyAdvanced, PreviewImage, VHS_VideoCombine, RIFE VFI, ControlNetLoaderAdvanced, ControlNetLoader, AIO_Preprocessor, ControlNetLoader, VAELoader, ImageScale, CheckpointLoaderSimple, BNK_CLIPTextEncodeAdvanced, ADE_AnimateDiffLoaderWithContext, VHS_LoadVideo, PreviewImage, ImageResizeKJ, CogVideoTextEncode, GetImageSizeAndCount, GetImageSizeAndCount, CogVideoImageEncode, CogVideoSampler, CogVideoDecode, CLIPLoader, DownloadAndLoadCogVideoModel, GetImageSizeAndCount, ImageConcanate, VHS_VideoCombine, VHS_LoadVideo, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, VHS_LoadVideo, ImageResizeKJ, WanVideoSampler, WanVideoEncode, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, WanVideoModelLoader, WanVideoVAELoader, LoraLoader, WanVideoTextEncode, CogVideoTextEncode]
patterns: [lora]
missing: []
parameters: {"cfg": 20, "checkpoint": "niji-动漫二次元加强版_2.0.safetensors", "controlnet_strength": 1, "denoise": "karras", "lora_name": "明亮动漫风格 _Niji默认风格 _ Niji Default style__v1.0.safetensors", "sampler_name": 7, "scheduler": "dpmpp_2m", "seed": true, "steps": "randomize", "strength_clip": 1, "strength_model": 0.5}
---

# 视频生成/文生视频/文生视频  wan2.2真人转动漫_2041329650097463297.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频  wan2.2真人转动漫_2041329650097463297.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `CLIPSetLastLayer`
- `FreeU_V2`
- `ADE_StandardStaticContextOptions`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSamplerAdvanced //Inspire` ★核心
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `VAEEncode` ★核心
- `DWPreprocessor`
- `ControlNetApplyAdvanced` ★核心
- `AIO_Preprocessor`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `VHS_VideoCombine`
- `RIFE VFI`
- `ControlNetLoaderAdvanced`
- `ControlNetLoader`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `VAELoader`
- `ImageScale`
- `CheckpointLoaderSimple` ★核心
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `ADE_AnimateDiffLoaderWithContext`
- `VHS_LoadVideo`
- `PreviewImage`
- `ImageResizeKJ`
- `CogVideoTextEncode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `CogVideoImageEncode`
- `CogVideoSampler` ★核心
- `CogVideoDecode`
- `CLIPLoader`
- `DownloadAndLoadCogVideoModel`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEmptyEmbeds`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoraLoader` ★核心
- `WanVideoTextEncode`
- `CogVideoTextEncode`

**识别到的模式**：lora

## 关键参数

- `seed` = `True`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `7`
- `scheduler` = `dpmpp_2m`
- `denoise` = `karras`
- `controlnet_strength` = `1`
- `checkpoint` = `niji-动漫二次元加强版_2.0.safetensors`
- `lora_name` = `明亮动漫风格 _Niji默认风格 _ Niji Default style__v1.0.safetensors`
- `strength_model` = `0.5`
- `strength_clip` = `1`

## 知识

覆盖率 **96%**（53/55）

**有卡**：`CLIPSetLastLayer`、`FreeU_V2`、`ADE_StandardStaticContextOptions`、`VHS_VideoCombine`、`VAEDecode`、`KSamplerAdvanced //Inspire`、`BNK_CLIPTextEncodeAdvanced`、`VAEEncode`、`DWPreprocessor`、`ControlNetApplyAdvanced`、`AIO_Preprocessor`、`RIFE VFI`、`ControlNetLoaderAdvanced`、`ControlNetLoader`、`VAELoader`、`ImageScale`、`CheckpointLoaderSimple`、`ADE_AnimateDiffLoaderWithContext`、`VHS_LoadVideo`、`ImageResizeKJ`、`CogVideoTextEncode`、`GetImageSizeAndCount`、`CogVideoImageEncode`、`CogVideoSampler`、`CogVideoDecode`、`CLIPLoader`、`DownloadAndLoadCogVideoModel`、`ImageConcanate`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoEncode`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoraLoader`、`WanVideoTextEncode`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPLoader、ControlNetApplyAdvanced、ControlNetLoader、ControlNetLoaderAdvanced、WanVideoSampler
