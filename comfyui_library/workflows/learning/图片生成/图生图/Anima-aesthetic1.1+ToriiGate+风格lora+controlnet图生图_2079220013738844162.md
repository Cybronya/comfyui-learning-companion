---
key: 图片生成/图生图/Anima-aesthetic1.1+ToriiGate+风格lora+controlnet图生图_2079220013738844162.json
name: Anima-aesthetic1.1+ToriiGate+风格lora+controlnet图生图_2079220013738844162
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Anima-aesthetic1.1+ToriiGate+风格lora+controlnet图生图_2079220013738844162.json
hash: 6c8fcf7a37dc5b32
coverage: 0.806452
learned_at: 2026-10-23 10:51:11
nodes: [easy showAnything, RegexExtract, easy showAnything, easy showAnything, StringTrim, StringSubstring, StringCompare, StringReplace, StringReplace, StringTrim, LayerUtility: If , easy showAnything, ConcatTextOfUtils, CR Prompt Text, CR Prompt Text, easy showAnything, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, SaveImage, 孤海注释, LoadImage, ToriiGateT8_LlamaCppVisionGenerate, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, ModelPatchLoader, AnimaLLLiteApply]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1920, "sampler_name": "dpmpp_2m_sde_gpu", "scheduler": "beta57", "seed": 1027533805992585, "steps": 40, "width": 1080}
---

# 图片生成/图生图/Anima-aesthetic1.1+ToriiGate+风格lora+controlnet图生图_2079220013738844162.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Anima-aesthetic1.1+ToriiGate+风格lora+controlnet图生图_2079220013738844162.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（31 个）：
- `easy showAnything`
- `RegexExtract`
- `easy showAnything`
- `easy showAnything`
- `StringTrim`
- `StringSubstring`
- `StringCompare`
- `StringReplace`
- `StringReplace`
- `StringTrim`
- `LayerUtility: If `
- `easy showAnything`
- `ConcatTextOfUtils`
- `CR Prompt Text`
- `CR Prompt Text`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `孤海注释`
- `LoadImage`
- `ToriiGateT8_LlamaCppVisionGenerate`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelPatchLoader`
- `AnimaLLLiteApply`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `1027533805992585`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `dpmpp_2m_sde_gpu`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **81%**（25/31）

**有卡**：`RegexExtract`、`StringTrim`、`StringSubstring`、`StringCompare`、`StringReplace`、`LayerUtility: If `、`ConcatTextOfUtils`、`CR Prompt Text`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`、`ToriiGateT8_LlamaCppVisionGenerate`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelPatchLoader`、`AnimaLLLiteApply`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage
