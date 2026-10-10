---
key: comfyui-workflow-templates-json/sdxl_revision_text_prompts.json
name: sdxl_revision_text_prompts
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/sdxl_revision_text_prompts.json
hash: fb299a5caf94f8c2
official: true
coverage: 0.933333
learned_at: 2026-10-10 22:48:54
nodes: [CLIPVisionLoader, CLIPTextEncode, LoadImage, CLIPVisionEncode, unCLIPConditioning, CLIPVisionEncode, unCLIPConditioning, CheckpointLoaderSimple, EmptyLatentImage, LoadImage, KSampler, SaveImage, MarkdownNote, VAEDecode, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "sd_xl_base_1.0.safetensors", "denoise": 1, "height": 1024, "sampler_name": "dpmpp_3m_sde_gpu", "scheduler": "exponential", "seed": 900749379955168, "steps": 26, "width": 1024}
---

# comfyui-workflow-templates-json/sdxl_revision_text_prompts.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/sdxl_revision_text_prompts.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPVisionEncode`
- `unCLIPConditioning`
- `CLIPVisionEncode`
- `unCLIPConditioning`
- `CheckpointLoaderSimple` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `KSampler` ★核心
- `SaveImage`
- `MarkdownNote`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `sd_xl_base_1.0.safetensors`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `900749379955168`
- `steps` = `26`
- `cfg` = `8`
- `sampler_name` = `dpmpp_3m_sde_gpu`
- `scheduler` = `exponential`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`CLIPVisionLoader`、`CLIPTextEncode`、`LoadImage`、`CLIPVisionEncode`、`unCLIPConditioning`、`CheckpointLoaderSimple`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、CLIPVisionEncode、CLIPVisionLoader
