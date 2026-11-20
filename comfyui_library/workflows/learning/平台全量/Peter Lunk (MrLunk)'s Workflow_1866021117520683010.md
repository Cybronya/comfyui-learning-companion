---
key: 平台全量/Peter Lunk (MrLunk)'s Workflow_1866021117520683010.json
name: Peter Lunk (MrLunk)'s Workflow_1866021117520683010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Peter Lunk (MrLunk)'s Workflow_1866021117520683010.json
hash: 98b4a6d41d21c083
coverage: 0.443038
learned_at: 2026-11-14 00:47:58
nodes: [CheckpointLoaderSimple, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPTextEncode, CLIPTextEncodeSDXLRefiner, CLIPTextEncode, CLIPTextEncodeSDXL, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, LoraLoader, LoraLoader, PrimitiveNode, PrimitiveNode, PrimitiveNode, PrimitiveNode, Reroute, SaveImage, Text Concatenate, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, UpscaleModelLoader, LoraLoader, LoraLoader, Reroute, Reroute, Reroute, KSamplerAdvanced, Reroute, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, Reroute, EmptyLatentImage, PrimitiveNode, Reroute, UltimateSDUpscale, easy prompt, Text Concatenate, easy prompt, LoraLoader, LoraLoader, VAEDecode, VAEDecode, SaveImage, PreviewImage, VAEDecode, SaveImage, PreviewImage, PreviewImage, SaveImage, CheckpointLoaderSimple, easy prompt, easy negative]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "cfg": 50, "checkpoint": "sd_xl_refiner_1.0_0.9vae_1.0.safetensors", "denoise": "karras", "height": 1024, "lora_name": "skin_4-000015.safetensors", "sampler_name": 1.5, "scheduler": "dpmpp_2m_sde_gpu", "seed": "enable", "steps": "randomize", "strength_clip": 1, "strength_model": 0.5, "width": 1024}
---

# 平台全量/Peter Lunk (MrLunk)'s Workflow_1866021117520683010.json

> 来源文件 `comfyui_library/workflows/平台全量/Peter Lunk (MrLunk)'s Workflow_1866021117520683010.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncodeSDXLRefiner` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncodeSDXL` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `Reroute`
- `SaveImage`
- `Text Concatenate`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `UpscaleModelLoader`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `Reroute`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Reroute`
- `EmptyLatentImage` ★核心
- `PrimitiveNode`
- `Reroute`
- `UltimateSDUpscale`
- `easy prompt`
- `Text Concatenate`
- `easy prompt`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `easy prompt`
- `easy negative`

**识别到的模式**：lora

## 关键参数

- `checkpoint` = `sd_xl_refiner_1.0_0.9vae_1.0.safetensors`
- `lora_name` = `skin_4-000015.safetensors`
- `strength_model` = `0.5`
- `strength_clip` = `1`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `50`
- `sampler_name` = `1.5`
- `scheduler` = `dpmpp_2m_sde_gpu`
- `denoise` = `karras`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **44%**（35/79）

**有卡**：`CheckpointLoaderSimple`、`CLIPTextEncode`、`CLIPTextEncodeSDXLRefiner`、`CLIPTextEncodeSDXL`、`LoraLoader`、`SaveImage`、`Text Concatenate`、`UpscaleModelLoader`、`KSamplerAdvanced`、`EmptyLatentImage`、`UltimateSDUpscale`、`easy prompt`、`VAEDecode`、`easy negative`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、KSamplerAdvanced、CLIPTextEncodeSDXL、CLIPTextEncodeSDXLRefiner、LoraLoader
