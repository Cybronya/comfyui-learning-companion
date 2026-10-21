---
key: 图片生成/文生图/z_image_base+turbo+controlnet_2047566373903142913.json
name: z_image_base+turbo+controlnet_2047566373903142913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z_image_base+turbo+controlnet_2047566373903142913.json
hash: 4b767a02b104d7d9
coverage: 0.818182
learned_at: 2026-10-21 02:57:48
nodes: [ModelSamplingAuraFlow, PrimitiveNode, CLIPTextEncode, VAEDecode, PreviewImage, ModelSamplingAuraFlow, EmptySD3LatentImage, SaveImage, ImageScaleToTotalPixels, CLIPTextEncode, CLIPLoader, VAELoader, UNETLoader, ModelPatchLoader, UNETLoader, LoadImage, DWPreprocessor, QwenImageDiffsynthControlnet, KSamplerAdvanced, KSamplerAdvanced, PrimitiveNode, PrimitiveNode]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 4, "scheduler": "res_multistep", "seed": "enable", "steps": "randomize"}
---

# 图片生成/文生图/z_image_base+turbo+controlnet_2047566373903142913.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z_image_base+turbo+controlnet_2047566373903142913.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `ModelSamplingAuraFlow`
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelPatchLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `DWPreprocessor`
- `QwenImageDiffsynthControlnet`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveNode`
- `PrimitiveNode`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `4`
- `scheduler` = `res_multistep`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`ModelSamplingAuraFlow`、`CLIPTextEncode`、`VAEDecode`、`EmptySD3LatentImage`、`SaveImage`、`ImageScaleToTotalPixels`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelPatchLoader`、`LoadImage`、`DWPreprocessor`、`QwenImageDiffsynthControlnet`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、QwenImageDiffsynthControlnet、KSamplerAdvanced
