---
key: 视频生成/文生视频/wan2.2-VACE-文生视频-动作迁移-视频高清放大_1969256411999969281.json
name: wan2.2-VACE-文生视频-动作迁移-视频高清放大_1969256411999969281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-VACE-文生视频-动作迁移-视频高清放大_1969256411999969281.json
hash: 8ea61c24c1e337f4
coverage: 0.9
learned_at: 2026-10-15 22:43:46
nodes: [LoraLoaderModelOnly, CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, DiffusionModelLoaderKJ, WanVaceToVideo, CLIPTextEncode, LayerUtility: PurgeVRAM V2, DiffusionModelSelector, DiffusionModelSelector, VAELoader, DiffusionModelLoaderKJ, Int, SetNode, easy showAnything, easy imageSwitch, VHS_LoadVideo, CLIPTextEncode, ImageResizeKJv2, Int, Int, VHS_VideoCombine, AIO_Preprocessor, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, Note, easy convertAnything, Int, GetNode, SeedVR2, Video_Upscale_With_Model, TrimVideoLatent, VAEDecode, easy cleanGpuUsed, easy clearCacheAll, KSamplerAdvanced, KSamplerAdvanced, FloatConstant, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/wan2.2-VACE-文生视频-动作迁移-视频高清放大_1969256411999969281.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1969256411999969281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（40 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `DiffusionModelSelector`
- `DiffusionModelSelector`
- `VAELoader`
- `DiffusionModelLoaderKJ`
- `Int`
- `SetNode`
- `easy showAnything`
- `easy imageSwitch`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `AIO_Preprocessor`
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `Note`
- `easy convertAnything`
- `Int`
- `GetNode`
- `SeedVR2`
- `Video_Upscale_With_Model`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `FloatConstant`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（36/40）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`ModelSamplingSD3`、`DiffusionModelLoaderKJ`、`WanVaceToVideo`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM V2`、`DiffusionModelSelector`、`VAELoader`、`Int`、`easy imageSwitch`、`VHS_LoadVideo`、`ImageResizeKJv2`、`VHS_VideoCombine`、`AIO_Preprocessor`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`easy convertAnything`、`SeedVR2`、`Video_Upscale_With_Model`、`TrimVideoLatent`、`VAEDecode`、`easy cleanGpuUsed`、`easy clearCacheAll`、`KSamplerAdvanced`、`FloatConstant`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、KSamplerAdvanced
