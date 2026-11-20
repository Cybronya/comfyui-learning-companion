---
key: 平台全量/F.1美女摄影超写实FLUX_1834866126617559042.json
name: F.1美女摄影超写实FLUX_1834866126617559042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.1美女摄影超写实FLUX_1834866126617559042.json
hash: bcc264a76357a7e8
coverage: 0.933333
learned_at: 2026-11-14 00:24:04
nodes: [BasicGuider, RandomNoise, BasicScheduler, KSamplerSelect, SamplerCustomAdvanced, VAELoader, DualCLIPLoader, SaveImage, SDXLEmptyLatentSizePicker+, UNETLoader, LoraLoader, CLIPTextEncodeFlux, PreviewImage, VAEDecode, SaveImage]
patterns: [lora]
missing: []
parameters: {"batch_size": 0, "height": 1, "lora_name": "flux_king_replicate.safetensors", "strength_clip": 1, "strength_model": 1, "width": "832x1152 (0.72)"}
---

# 平台全量/F.1美女摄影超写实FLUX_1834866126617559042.json

> 来源文件 `comfyui_library/workflows/平台全量/F.1美女摄影超写实FLUX_1834866126617559042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `BasicGuider`
- `RandomNoise`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `SaveImage`
- `SDXLEmptyLatentSizePicker+` ★核心
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncodeFlux` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `width` = `832x1152 (0.72)`
- `height` = `1`
- `batch_size` = `0`
- `lora_name` = `flux_king_replicate.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`BasicGuider`、`RandomNoise`、`BasicScheduler`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAELoader`、`DualCLIPLoader`、`SaveImage`、`SDXLEmptyLatentSizePicker+`、`UNETLoader`、`LoraLoader`、`CLIPTextEncodeFlux`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、CLIPTextEncodeFlux、SDXLEmptyLatentSizePicker+、LoraLoader
