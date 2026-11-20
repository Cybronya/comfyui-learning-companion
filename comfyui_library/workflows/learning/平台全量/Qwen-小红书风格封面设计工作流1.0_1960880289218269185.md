---
key: 平台全量/Qwen-小红书风格封面设计工作流1.0_1960880289218269185.json
name: Qwen-小红书风格封面设计工作流1.0_1960880289218269185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-小红书风格封面设计工作流1.0_1960880289218269185.json
hash: 9242a2518515d71c
coverage: 0.916667
learned_at: 2026-11-14 00:52:18
nodes: [CLIPLoader, ModelSamplingAuraFlow, KSampler, VAELoader, VAEDecode, ConditioningZeroOut, CR SDXL Aspect Ratio, Note, SaveImage, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 140266914266967, "steps": 30}
---

# 平台全量/Qwen-小红书风格封面设计工作流1.0_1960880289218269185.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-小红书风格封面设计工作流1.0_1960880289218269185.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `CR SDXL Aspect Ratio`
- `Note`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `140266914266967`
- `steps` = `30`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`CLIPLoader`、`ModelSamplingAuraFlow`、`KSampler`、`VAELoader`、`VAEDecode`、`ConditioningZeroOut`、`CR SDXL Aspect Ratio`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut
