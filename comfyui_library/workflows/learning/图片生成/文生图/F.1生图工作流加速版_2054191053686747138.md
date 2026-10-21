---
key: 图片生成/文生图/F.1生图工作流加速版_2054191053686747138.json
name: F.1生图工作流加速版_2054191053686747138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1生图工作流加速版_2054191053686747138.json
hash: 0d4a4063c442bf60
coverage: 1
learned_at: 2026-10-21 02:51:44
nodes: [EmptyLatentImage, CLIPTextEncode, VAEDecode, UNETLoader, VAELoader, DualCLIPLoader, FluxGuidance, LoraLoaderModelOnly, RescaleCFG, BasicGuider, BasicScheduler, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1960, "width": 1080}
---

# 图片生成/文生图/F.1生图工作流加速版_2054191053686747138.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1生图工作流加速版_2054191053686747138.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `LoraLoaderModelOnly` ★核心
- `RescaleCFG`
- `BasicGuider`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SaveImage`

## 关键参数

- `width` = `1080`
- `height` = `1960`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`EmptyLatentImage`、`CLIPTextEncode`、`VAEDecode`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`FluxGuidance`、`LoraLoaderModelOnly`、`RescaleCFG`、`BasicGuider`、`BasicScheduler`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、EmptyLatentImage、FluxGuidance、KSamplerSelect
