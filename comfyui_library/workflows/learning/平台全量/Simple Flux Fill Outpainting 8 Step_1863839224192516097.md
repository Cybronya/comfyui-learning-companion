---
key: 平台全量/Simple Flux Fill Outpainting 8 Step_1863839224192516097.json
name: Simple Flux Fill Outpainting 8 Step_1863839224192516097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Simple Flux Fill Outpainting 8 Step_1863839224192516097.json
hash: 58463c7611310510
coverage: 0.904762
learned_at: 2026-11-14 01:00:40
nodes: [CLIPTextEncode, Image Resize To Height, LoadImage, UNETLoader, DualCLIPLoader, LoraLoader, PreviewImage, ImageRGBA2RGB, FluxGuidance, VAELoader, InpaintModelConditioning, DifferentialDiffusion, VAEDecode, PreviewImage, SaveImage, CLIPTextEncode, ImagePadForOutpaint, easy imageSize, ttN imageREMBG, MaskPreview+, KSampler]
patterns: [lora]
missing: []
parameters: {"cfg": 4.48, "denoise": 1, "lora_name": "alimama_diffusion_pytorch_model.safetensors", "sampler_name": "euler", "scheduler": "normal", "seed": 543710639682272, "steps": 14, "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Simple Flux Fill Outpainting 8 Step_1863839224192516097.json

> 来源文件 `comfyui_library/workflows/平台全量/Simple Flux Fill Outpainting 8 Step_1863839224192516097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPTextEncode` ★核心
- `Image Resize To Height`
- `LoadImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `PreviewImage`
- `ImageRGBA2RGB`
- `FluxGuidance`
- `VAELoader`
- `InpaintModelConditioning`
- `DifferentialDiffusion`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ImagePadForOutpaint`
- `easy imageSize`
- `ttN imageREMBG`
- `MaskPreview+`
- `KSampler` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `alimama_diffusion_pytorch_model.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `543710639682272`
- `steps` = `14`
- `cfg` = `4.48`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`CLIPTextEncode`、`Image Resize To Height`、`LoadImage`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`ImageRGBA2RGB`、`FluxGuidance`、`VAELoader`、`InpaintModelConditioning`、`DifferentialDiffusion`、`VAEDecode`、`SaveImage`、`ImagePadForOutpaint`、`easy imageSize`、`ttN imageREMBG`、`MaskPreview+`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、LoraLoader
