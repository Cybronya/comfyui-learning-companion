---
key: 平台全量/Qwen-Image 手写艺术字海报直出工作流v1.0  by@阮旭东AIGC_1962304978536873985.json
name: Qwen-Image 手写艺术字海报直出工作流v1.0  by@阮旭东AIGC_1962304978536873985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image 手写艺术字海报直出工作流v1.0  by@阮旭东AIGC_1962304978536873985.json
hash: 02fb5fee08518208
coverage: 0.857143
learned_at: 2026-11-14 00:51:32
nodes: [KSampler, VAEDecode, PreviewImage, ConditioningZeroOut, CLIPLoader, ModelSamplingAuraFlow, VAELoader, LoadImage, UNETLoader, SaveImage, CLIPTextEncode, CR SDXL Aspect Ratio, LoraLoaderModelOnly, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 4.1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 174099300875449, "steps": 20}
---

# 平台全量/Qwen-Image 手写艺术字海报直出工作流v1.0  by@阮旭东AIGC_1962304978536873985.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image 手写艺术字海报直出工作流v1.0  by@阮旭东AIGC_1962304978536873985.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `ConditioningZeroOut`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `LoadImage`
- `UNETLoader` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CR SDXL Aspect Ratio`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`

## 关键参数

- `seed` = `174099300875449`
- `steps` = `20`
- `cfg` = `4.1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`KSampler`、`VAEDecode`、`ConditioningZeroOut`、`CLIPLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`LoadImage`、`UNETLoader`、`SaveImage`、`CLIPTextEncode`、`CR SDXL Aspect Ratio`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut
