---
key: comfyui-workflow-templates-json/sdxl_refiner_prompt_example.json
name: sdxl_refiner_prompt_example
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/sdxl_refiner_prompt_example.json
hash: c376af45ad93aeb5
official: true
coverage: 0.55
learned_at: 2026-10-07 21:36:17
nodes: [Note, Note, Note, Note, CheckpointLoaderSimple, CheckpointLoaderSimple, Note, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, PrimitiveNode, PrimitiveNode, EmptyLatentImage, KSamplerAdvanced, Note, KSamplerAdvanced, VAEDecode, SaveImage, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 25, "checkpoint": "sd_xl_base_1.0.safetensors", "denoise": "normal", "height": 1024, "sampler_name": 8, "scheduler": "euler", "seed": "disable", "steps": "fixed", "width": 1024}
---

# comfyui-workflow-templates-json/sdxl_refiner_prompt_example.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/sdxl_refiner_prompt_example.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `Note`
- `Note`
- `Note`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `EmptyLatentImage` ★核心
- `KSamplerAdvanced` ★核心
- `Note`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `MarkdownNote`

## 关键参数

- `checkpoint` = `sd_xl_base_1.0.safetensors`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `25`
- `sampler_name` = `8`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **55%**（11/20）

**有卡**：`CheckpointLoaderSimple`、`CLIPTextEncode`、`EmptyLatentImage`、`KSamplerAdvanced`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、KSamplerAdvanced、SaveImage、KSampler、sd15-t2i-basic
