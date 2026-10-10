---
key: comfyui-workflow-templates-json/sd3.5_simple_example.json
name: sd3.5_simple_example
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/sd3.5_simple_example.json
hash: 22636f8ea8d35f41
official: true
coverage: 0.875
learned_at: 2026-10-10 22:48:52
nodes: [VAEDecode, SaveImage, CLIPTextEncode, EmptySD3LatentImage, CheckpointLoaderSimple, CLIPTextEncode, KSampler, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 4.01, "checkpoint": "sd3.5_large_fp8_scaled.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 585483408983215, "steps": 20}
---

# comfyui-workflow-templates-json/sd3.5_simple_example.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/sd3.5_simple_example.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（8 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `MarkdownNote`

## 关键参数

- `checkpoint` = `sd3.5_large_fp8_scaled.safetensors`
- `seed` = `585483408983215`
- `steps` = `20`
- `cfg` = `4.01`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`EmptySD3LatentImage`、`CheckpointLoaderSimple`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、SaveImage、EmptySD3LatentImage、sd15-t2i-basic、sd15-t2i-lora
