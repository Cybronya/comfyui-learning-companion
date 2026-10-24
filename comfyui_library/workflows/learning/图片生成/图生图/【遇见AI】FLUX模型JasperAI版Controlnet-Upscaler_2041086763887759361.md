---
key: 图片生成/图生图/【遇见AI】FLUX模型JasperAI版Controlnet-Upscaler_2041086763887759361.json
name: 【遇见AI】FLUX模型JasperAI版Controlnet-Upscaler_2041086763887759361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型JasperAI版Controlnet-Upscaler_2041086763887759361.json
hash: 2b6edb8b8c7a37ce
coverage: 0.863636
learned_at: 2026-10-23 11:51:59
nodes: [BasicGuider, VAEDecode, KSamplerSelect, SaveImage, BasicScheduler, ModelSamplingFlux, EmptyLatentImage, SamplerCustomAdvanced, RandomNoise, PrimitiveNode, CLIPTextEncodeFlux, ConditioningZeroOut, ControlNetApplySD3, Note, LoadImage, LoadImage, LoadImage, UnetLoaderGGUF, DualCLIPLoader, VAELoader, PrimitiveNode, ControlNetLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "controlnet_strength": 1, "height": 1536, "width": 1024}
---

# 图片生成/图生图/【遇见AI】FLUX模型JasperAI版Controlnet-Upscaler_2041086763887759361.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型JasperAI版Controlnet-Upscaler_2041086763887759361.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（22 个）：
- `BasicGuider`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SaveImage`
- `BasicScheduler`
- `ModelSamplingFlux`
- `EmptyLatentImage` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `PrimitiveNode`
- `CLIPTextEncodeFlux` ★核心
- `ConditioningZeroOut`
- `ControlNetApplySD3` ★核心
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `PrimitiveNode`
- `ControlNetLoader`

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `controlnet_strength` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`BasicGuider`、`VAEDecode`、`KSamplerSelect`、`SaveImage`、`BasicScheduler`、`ModelSamplingFlux`、`EmptyLatentImage`、`SamplerCustomAdvanced`、`RandomNoise`、`CLIPTextEncodeFlux`、`ConditioningZeroOut`、`ControlNetApplySD3`、`LoadImage`、`UnetLoaderGGUF`、`DualCLIPLoader`、`VAELoader`、`ControlNetLoader`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、ControlNetLoader、ControlNetApplySD3、KSamplerSelect
