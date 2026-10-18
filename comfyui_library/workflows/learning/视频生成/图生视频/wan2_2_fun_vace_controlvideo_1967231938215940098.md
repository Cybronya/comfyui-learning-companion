---
key: 视频生成/图生视频/wan2_2_fun_vace_controlvideo_1967231938215940098.json
name: wan2_2_fun_vace_controlvideo_1967231938215940098.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2_2_fun_vace_controlvideo_1967231938215940098.json
hash: d9c73556cdd95e2a
coverage: 0.530303
learned_at: 2026-10-15 22:31:40
nodes: [KSamplerAdvanced, SetNode, SetNode, GetNode, SetNode, CLIPTextEncode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, INTConstant, INTConstant, INTConstant, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), CLIPLoader, VAELoader, ModelSamplingSD3, SetNode, SetNode, VAEDecode, DiffusionModelSelector, LoraLoaderModelOnly, DiffusionModelLoaderKJ, ModelSamplingSD3, LoadImage, SetNode, SetNode, SetNode, VHS_VideoCombine, CLIPTextEncode, LoraLoaderModelOnly, SetNode, GetNode, SetNode, SetNode, WanVaceToVideo, RMBG, DiffusionModelSelector, DiffusionModelLoaderKJ, KSamplerAdvanced, TrimVideoLatent, GetNode, ImageResizeKJv2, VHS_LoadVideo, GetNode, GetNode, GetNode, PreviewImage, AIO_Preprocessor, ImageResizeKJv2, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2_2_fun_vace_controlvideo_1967231938215940098.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967231938215940098.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `KSamplerAdvanced` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `DiffusionModelSelector`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `ModelSamplingSD3`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVaceToVideo`
- `RMBG`
- `DiffusionModelSelector`
- `DiffusionModelLoaderKJ`
- `KSamplerAdvanced` ★核心
- `TrimVideoLatent`
- `GetNode`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `AIO_Preprocessor`
- `ImageResizeKJv2`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **53%**（35/66）

**有卡**：`KSamplerAdvanced`、`CLIPTextEncode`、`INTConstant`、`Label (rgthree)`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`VAEDecode`、`DiffusionModelSelector`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`LoadImage`、`VHS_VideoCombine`、`WanVaceToVideo`、`RMBG`、`TrimVideoLatent`、`ImageResizeKJv2`、`VHS_LoadVideo`、`AIO_Preprocessor`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、TrimVideoLatent
