---
key: 图片生成/文生图/F.1一键毛坯变精装工作流 Bot_LXX V3.0_1930576899993686018.json
name: F.1一键毛坯变精装工作流 Bot_LXX V3.0_1930576899993686018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1一键毛坯变精装工作流 Bot_LXX V3.0_1930576899993686018.json
hash: 761afc87a93d32d9
coverage: 0.909091
learned_at: 2026-10-15 22:26:16
nodes: [KSampler, CLIPTextEncode, VAEDecode, CLIPTextEncode, FluxGuidance, DualCLIPLoader, AIO_Preprocessor, PreviewImage, ControlNetApplyAdvanced, ControlNetApplyAdvanced, PreviewImage, EmptySD3LatentImage, LayerUtility: ImageScaleByAspectRatio, LoadImage, VAELoader, ControlNetLoader, ControlNetLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, AIO_Preprocessor]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.38000000000000006, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 675936471075091, "steps": 30}
---

# 图片生成/文生图/F.1一键毛坯变精装工作流 Bot_LXX V3.0_1930576899993686018.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1一键毛坯变精装工作流 Bot_LXX V3.0_1930576899993686018.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `DualCLIPLoader`
- `AIO_Preprocessor`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `EmptySD3LatentImage`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadImage`
- `VAELoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `AIO_Preprocessor`

## 关键参数

- `seed` = `675936471075091`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `controlnet_strength` = `0.38000000000000006`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`KSampler`、`CLIPTextEncode`、`VAEDecode`、`FluxGuidance`、`DualCLIPLoader`、`AIO_Preprocessor`、`ControlNetApplyAdvanced`、`EmptySD3LatentImage`、`LayerUtility: ImageScaleByAspectRatio`、`LoadImage`、`VAELoader`、`ControlNetLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced
