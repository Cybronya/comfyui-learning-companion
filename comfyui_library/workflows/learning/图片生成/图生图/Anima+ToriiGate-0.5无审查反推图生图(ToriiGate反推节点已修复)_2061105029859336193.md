---
key: 图片生成/图生图/Anima+ToriiGate-0.5无审查反推图生图(ToriiGate反推节点已修复)_2061105029859336193.json
name: Anima+ToriiGate-0.5无审查反推图生图(ToriiGate反推节点已修复)_2061105029859336193
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Anima+ToriiGate-0.5无审查反推图生图(ToriiGate反推节点已修复)_2061105029859336193.json
hash: a2eb6f5fba3b42b5
coverage: 0.928571
learned_at: 2026-10-23 10:51:08
nodes: [CLIPTextEncode, ConcatTextOfUtils, CR Prompt Text, CLIPTextEncode, SaveImage, VAEDecode, KSampler, UNETLoader, CLIPLoader, VAELoader, easy showAnything, EmptyLatentImage, LoadImage, ToriiGateT8_LlamaCppVisionGenerate]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1600, "sampler_name": "dpmpp_2m_sde_gpu", "scheduler": "beta57", "seed": 287312689854087, "steps": 40, "width": 1200}
---

# 图片生成/图生图/Anima+ToriiGate-0.5无审查反推图生图(ToriiGate反推节点已修复)_2061105029859336193.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Anima+ToriiGate-0.5无审查反推图生图(ToriiGate反推节点已修复)_2061105029859336193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `ConcatTextOfUtils`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ToriiGateT8_LlamaCppVisionGenerate`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `287312689854087`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `dpmpp_2m_sde_gpu`
- `scheduler` = `beta57`
- `denoise` = `1`
- `width` = `1200`
- `height` = `1600`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CLIPTextEncode`、`ConcatTextOfUtils`、`CR Prompt Text`、`SaveImage`、`VAEDecode`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`LoadImage`、`ToriiGateT8_LlamaCppVisionGenerate`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
