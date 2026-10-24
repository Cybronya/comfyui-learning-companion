---
key: 图片生成/图生图/QWEN image 2.1分镜图制作_2112527551305441282.json
name: QWEN image 2.1分镜图制作_2112527551305441282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QWEN image 2.1分镜图制作_2112527551305441282.json
hash: 44d1c6aa87f228d0
coverage: 0.851852
learned_at: 2026-10-23 11:11:08
nodes: [Reroute, VAELoader, Reroute, QwenImage21BlockCacheT8, TextEncodeQwenImage21GH, QwenImage21SpectrumT8, CLIPLoader, KSampler, QwenImage21SageAttentionT8, VAEDecode, UNETLoader, RestoreQwenImage21GH, llama_cpp_parameters, llama_cpp_model_loader, easy promptLine, easy cleanGpuUsed, Note, easy promptConcat, LoadImage, llama_cpp_instruct_adv, CR Text, ShowText|pysssss, SaveImage, QwenImagePromptOptimizer, CR Text, GoohaiRatioAndResolution, GoohaiDisplayAny]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 70110409369953, "steps": 30}
---

# 图片生成/图生图/QWEN image 2.1分镜图制作_2112527551305441282.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QWEN image 2.1分镜图制作_2112527551305441282.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `Reroute`
- `VAELoader`
- `Reroute`
- `QwenImage21BlockCacheT8`
- `TextEncodeQwenImage21GH`
- `QwenImage21SpectrumT8`
- `CLIPLoader`
- `KSampler` ★核心
- `QwenImage21SageAttentionT8`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `RestoreQwenImage21GH`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `easy promptLine`
- `easy cleanGpuUsed`
- `Note`
- `easy promptConcat`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `CR Text`
- `ShowText|pysssss`
- `SaveImage`
- `QwenImagePromptOptimizer`
- `CR Text`
- `GoohaiRatioAndResolution`
- `GoohaiDisplayAny`

## 关键参数

- `seed` = `70110409369953`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`VAELoader`、`QwenImage21BlockCacheT8`、`TextEncodeQwenImage21GH`、`QwenImage21SpectrumT8`、`CLIPLoader`、`KSampler`、`QwenImage21SageAttentionT8`、`VAEDecode`、`UNETLoader`、`RestoreQwenImage21GH`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`easy promptLine`、`easy cleanGpuUsed`、`easy promptConcat`、`LoadImage`、`llama_cpp_instruct_adv`、`CR Text`、`SaveImage`、`QwenImagePromptOptimizer`、`GoohaiRatioAndResolution`、`GoohaiDisplayAny`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImage21GH、QwenImagePromptOptimizer
