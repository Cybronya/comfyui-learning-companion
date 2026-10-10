---
key: comfyui-workflow-templates-json/sdxlturbo_example.json
name: sdxlturbo_example
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/sdxlturbo_example.json
hash: d3ece55064f10b31
official: true
coverage: 0.9
learned_at: 2026-10-10 22:48:55
nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSamplerSelect, EmptyLatentImage, SDTurboScheduler, CLIPTextEncode, SamplerCustom, MarkdownNote, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "sd_xl_turbo_1.0_fp16.safetensors", "height": 512, "width": 512}
---

# comfyui-workflow-templates-json/sdxlturbo_example.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/sdxlturbo_example.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `KSamplerSelect` ★核心
- `EmptyLatentImage` ★核心
- `SDTurboScheduler`
- `CLIPTextEncode` ★核心
- `SamplerCustom` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `checkpoint` = `sd_xl_turbo_1.0_fp16.safetensors`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`CLIPTextEncode`、`CheckpointLoaderSimple`、`KSamplerSelect`、`EmptyLatentImage`、`SDTurboScheduler`、`SamplerCustom`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、KSamplerSelect、SamplerCustom、SaveImage、SDTurboScheduler
