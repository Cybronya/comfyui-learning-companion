---
key: 图片生成/图生图/【遇见AI】FLUX模型alimama版Controlnet-Inpainting_2041074588796325889.json
name: 【遇见AI】FLUX模型alimama版Controlnet-Inpainting_2041074588796325889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型alimama版Controlnet-Inpainting_2041074588796325889.json
hash: 79231db2e2a1bbac
coverage: 0.863636
learned_at: 2026-10-23 11:52:01
nodes: [VAEDecode, KSamplerSelect, SaveImage, BasicScheduler, ModelSamplingFlux, EmptyLatentImage, PrimitiveNode, PrimitiveNode, SamplerCustomAdvanced, CLIPTextEncodeFlux, ControlNetInpaintingAliMamaApply, ConditioningZeroOut, RandomNoise, BasicGuider, Note, LoadImage, LoadImage, ControlNetLoader, UnetLoaderGGUF, DualCLIPLoader, VAELoader, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/【遇见AI】FLUX模型alimama版Controlnet-Inpainting_2041074588796325889.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型alimama版Controlnet-Inpainting_2041074588796325889.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（22 个）：
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SaveImage`
- `BasicScheduler`
- `ModelSamplingFlux`
- `EmptyLatentImage` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncodeFlux` ★核心
- `ControlNetInpaintingAliMamaApply`
- `ConditioningZeroOut`
- `RandomNoise`
- `BasicGuider`
- `Note`
- `LoadImage`
- `LoadImage`
- `ControlNetLoader`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`VAEDecode`、`KSamplerSelect`、`SaveImage`、`BasicScheduler`、`ModelSamplingFlux`、`EmptyLatentImage`、`SamplerCustomAdvanced`、`CLIPTextEncodeFlux`、`ControlNetInpaintingAliMamaApply`、`ConditioningZeroOut`、`RandomNoise`、`BasicGuider`、`LoadImage`、`ControlNetLoader`、`UnetLoaderGGUF`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、ControlNetInpaintingAliMamaApply、ControlNetLoader、KSamplerSelect
