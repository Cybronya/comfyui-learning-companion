---
key: comfyui-workflow-templates-json/sdxl_simple_example.json
name: sdxl_simple_example
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/sdxl_simple_example.json
hash: 7f3825deea7a3fc4
official: true
coverage: 0.44
learned_at: 2026-10-10 22:48:55
nodes: [EmptyLatentImage, Note, CheckpointLoaderSimple, PrimitiveNode, PrimitiveNode, Note, VAEDecode, Note, CLIPTextEncode, CLIPTextEncode, Note, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, CheckpointLoaderSimple, Note, Note, PrimitiveNode, PrimitiveNode, Note, Note, MarkdownNote, Note, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 25, "checkpoint": "sd_xl_refiner_1.0.safetensors", "denoise": "normal", "height": 1024, "sampler_name": 8, "scheduler": "euler", "seed": "disable", "steps": "fixed", "width": 1024}
---

# comfyui-workflow-templates-json/sdxl_simple_example.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/sdxl_simple_example.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `EmptyLatentImage` ★核心
- `Note`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `Note`
- `VAEDecode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `Note`
- `Note`
- `PrimitiveNode`
- `PrimitiveNode`
- `Note`
- `Note`
- `MarkdownNote`
- `Note`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `checkpoint` = `sd_xl_refiner_1.0.safetensors`
- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `25`
- `sampler_name` = `8`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **44%**（11/25）

**有卡**：`EmptyLatentImage`、`CheckpointLoaderSimple`、`VAEDecode`、`CLIPTextEncode`、`KSamplerAdvanced`、`SaveImage`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、KSamplerAdvanced、SaveImage、KSampler、sd15-t2i-basic
