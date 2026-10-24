---
key: 图片生成/图生图/2025-04-15 nunchaku-flux.1-depth-lora_1912081673633366018.json
name: 2025-04-15 nunchaku-flux.1-depth-lora_1912081673633366018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/2025-04-15 nunchaku-flux.1-depth-lora_1912081673633366018.json
hash: 5329cee272b581fe
coverage: 0.944444
learned_at: 2026-10-23 10:48:06
nodes: [VAEDecode, KSampler, CLIPTextEncode, NunchakuFluxDiTLoader, VAELoader, Florence2Run, DualCLIPLoader, Florence2ModelLoader, CLIPTextEncode, ImageScaleToMegapixels, InstructPixToPixConditioning, DepthAnythingPreprocessor, FluxGuidance, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, SaveImage, PreviewImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 677729013463731, "steps": 20}
---

# 图片生成/图生图/2025-04-15 nunchaku-flux.1-depth-lora_1912081673633366018.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2025-04-15 nunchaku-flux.1-depth-lora_1912081673633366018.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `NunchakuFluxDiTLoader`
- `VAELoader`
- `Florence2Run`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `CLIPTextEncode` ★核心
- `ImageScaleToMegapixels`
- `InstructPixToPixConditioning`
- `DepthAnythingPreprocessor`
- `FluxGuidance`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `SaveImage`
- `PreviewImage`
- `LoadImage`

## 关键参数

- `seed` = `677729013463731`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`VAEDecode`、`KSampler`、`CLIPTextEncode`、`NunchakuFluxDiTLoader`、`VAELoader`、`Florence2Run`、`DualCLIPLoader`、`Florence2ModelLoader`、`ImageScaleToMegapixels`、`InstructPixToPixConditioning`、`DepthAnythingPreprocessor`、`FluxGuidance`、`NunchakuFluxLoraLoader`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、DepthAnythingPreprocessor、FluxGuidance、NunchakuFluxLoraLoader
