---
key: 平台全量/Change product background_1878682372546928641.json
name: Change product background_1878682372546928641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Change product background_1878682372546928641.json
hash: 3985a3f05b5b3d96
coverage: 0.958333
learned_at: 2026-11-14 00:22:11
nodes: [ControlNetLoader, PreviewImage, CheckpointLoaderSimple, IPAdapterUnifiedLoader, PrepImageForClipVision, ImageRemoveBackground+, DifferentialDiffusion, MaskPreview+, InvertMask, GrowMask, CLIPVisionLoader, KSampler, InpaintModelConditioning, ControlNetApplyAdvanced, DepthAnythingPreprocessor, RemBGSession+, CLIPTextEncode, VAEDecode, SaveImage, IPAdapterAdvanced, CLIPTextEncode, LoadImage, LoadImage, ImageResize+]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 1, "denoise": 1, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 448891175561923, "steps": 7}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Change product background_1878682372546928641.json

> 来源文件 `comfyui_library/workflows/平台全量/Change product background_1878682372546928641.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `ControlNetLoader`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `IPAdapterUnifiedLoader`
- `PrepImageForClipVision`
- `ImageRemoveBackground+`
- `DifferentialDiffusion`
- `MaskPreview+`
- `InvertMask`
- `GrowMask`
- `CLIPVisionLoader`
- `KSampler` ★核心
- `InpaintModelConditioning`
- `ControlNetApplyAdvanced` ★核心
- `DepthAnythingPreprocessor`
- `RemBGSession+`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `IPAdapterAdvanced`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `ImageResize+`

## 关键参数

- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`
- `seed` = `448891175561923`
- `steps` = `7`
- `cfg` = `2`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `controlnet_strength` = `1`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`ControlNetLoader`、`CheckpointLoaderSimple`、`IPAdapterUnifiedLoader`、`PrepImageForClipVision`、`ImageRemoveBackground+`、`DifferentialDiffusion`、`MaskPreview+`、`InvertMask`、`GrowMask`、`CLIPVisionLoader`、`KSampler`、`InpaintModelConditioning`、`ControlNetApplyAdvanced`、`DepthAnythingPreprocessor`、`RemBGSession+`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`IPAdapterAdvanced`、`LoadImage`、`ImageResize+`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、DepthAnythingPreprocessor

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
