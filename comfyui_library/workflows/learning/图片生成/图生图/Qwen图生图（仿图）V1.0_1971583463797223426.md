---
key: 图片生成/图生图/Qwen图生图（仿图）V1.0_1971583463797223426.json
name: Qwen图生图（仿图）V1.0_1971583463797223426
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen图生图（仿图）V1.0_1971583463797223426.json
hash: 79815b5ba8029e41
coverage: 0.941176
learned_at: 2026-10-23 11:22:15
nodes: [VAELoader, ModelSamplingAuraFlow, EmptyLatentImage, CLIPTextEncode, LayerUtility: PurgeVRAM, PreviewImage, LoraLoaderModelOnly, LoraLoaderModelOnly, FluxResolutionNode, RH_LLMAPI_NODE, KSampler, LoadImage, CLIPLoader, UNETLoader, ConditioningZeroOut, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 553879971560013, "steps": 35, "width": 512}
---

# 图片生成/图生图/Qwen图生图（仿图）V1.0_1971583463797223426.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen图生图（仿图）V1.0_1971583463797223426.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `VAELoader`
- `ModelSamplingAuraFlow`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxResolutionNode`
- `RH_LLMAPI_NODE`
- `KSampler` ★核心
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `553879971560013`
- `steps` = `35`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`VAELoader`、`ModelSamplingAuraFlow`、`EmptyLatentImage`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM`、`LoraLoaderModelOnly`、`FluxResolutionNode`、`RH_LLMAPI_NODE`、`KSampler`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
