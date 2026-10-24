---
key: 图片生成/图生图/Anima+ToriiGate-0.5无审查反推+controlnet强控图生图(已修复)_2061398059543785474.json
name: Anima+ToriiGate-0.5无审查反推+controlnet强控图生图(已修复)_2061398059543785474
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Anima+ToriiGate-0.5无审查反推+controlnet强控图生图(已修复)_2061398059543785474.json
hash: 8a433289e10a0cae
coverage: 0.933333
learned_at: 2026-10-23 10:51:08
nodes: [VAELoader, CLIPTextEncode, ConcatTextOfUtils, CR Prompt Text, CLIPTextEncode, SaveImage, VAEDecode, KSampler, LoadImage, ToriiGateT8_LlamaCppVisionGenerate, easy showAnything, EmptyLatentImage, AnimaLLLiteApply, CLIPLoader, UNETLoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1600, "sampler_name": "dpmpp_2m_sde_gpu", "scheduler": "beta57", "seed": 942769462711668, "steps": 40, "width": 1000}
---

# 图片生成/图生图/Anima+ToriiGate-0.5无审查反推+controlnet强控图生图(已修复)_2061398059543785474.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Anima+ToriiGate-0.5无审查反推+controlnet强控图生图(已修复)_2061398059543785474.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConcatTextOfUtils`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `ToriiGateT8_LlamaCppVisionGenerate`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `AnimaLLLiteApply`
- `CLIPLoader`
- `UNETLoader` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `942769462711668`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `dpmpp_2m_sde_gpu`
- `scheduler` = `beta57`
- `denoise` = `1`
- `width` = `1000`
- `height` = `1600`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`VAELoader`、`CLIPTextEncode`、`ConcatTextOfUtils`、`CR Prompt Text`、`SaveImage`、`VAEDecode`、`KSampler`、`LoadImage`、`ToriiGateT8_LlamaCppVisionGenerate`、`EmptyLatentImage`、`AnimaLLLiteApply`、`CLIPLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
