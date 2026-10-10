---
key: 视频生成/文生视频/Wan 2.2-Fun-VACE-姿态视频引导加参考无敌控_1967578038525390850.json
name: Wan 2.2-Fun-VACE-姿态视频引导加参考无敌控_1967578038525390850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE-姿态视频引导加参考无敌控_1967578038525390850.json
hash: 22dfaa9b1b1ccaad
coverage: 1
learned_at: 2026-10-10 23:06:10
nodes: [TrimVideoLatent, VAEDecode, CLIPTextEncode, VHS_VideoCombine, WanVaceToVideo, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, VAELoader, KSamplerAdvanced, INTConstant, ImageResizeKJv2, GetImageSizeAndCount, INTConstant, LoraLoaderModelOnly, CLIPTextEncode, VHS_LoadVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, Miaoshouai_Tagger, UNETLoader, AIO_Preprocessor, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "sa_solver_pece", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan 2.2-Fun-VACE-姿态视频引导加参考无敌控_1967578038525390850.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE-姿态视频引导加参考无敌控_1967578038525390850.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Miaoshouai_Tagger`
- `UNETLoader` ★核心
- `AIO_Preprocessor`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `sa_solver_pece`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`CLIPTextEncode`、`VHS_VideoCombine`、`WanVaceToVideo`、`ModelSamplingSD3`、`CLIPLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`VAELoader`、`INTConstant`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`VHS_LoadVideo`、`UNETLoader`、`Miaoshouai_Tagger`、`AIO_Preprocessor`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
