---
key: 图片生成/图生图/Flux.2 Klein助力电商实现AI模特换装自由_ComfyUI工作流_2021893743644778498.json
name: Flux.2 Klein助力电商实现AI模特换装自由_ComfyUI工作流_2021893743644778498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2 Klein助力电商实现AI模特换装自由_ComfyUI工作流_2021893743644778498.json
hash: ec969763edd102ce
coverage: 1
learned_at: 2026-10-23 10:58:47
nodes: [RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, CLIPLoader, ReferenceLatent, SamplerCustomAdvanced, LoadImage, ReferenceLatent, ReferenceLatent, VAEEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, VAEEncode, ConditioningZeroOut, LoadImage, LoadImage, VAELoader, GetImageSizeAndCount, CLIPTextEncode, UNETLoader, VAEDecode, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.2 Klein助力电商实现AI模特换装自由_ComfyUI工作流_2021893743644778498.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2 Klein助力电商实现AI模特换装自由_ComfyUI工作流_2021893743644778498.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `CLIPLoader`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `GetImageSizeAndCount`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`CLIPLoader`、`ReferenceLatent`、`SamplerCustomAdvanced`、`LoadImage`、`VAEEncode`、`ConditioningZeroOut`、`VAELoader`、`GetImageSizeAndCount`、`CLIPTextEncode`、`UNETLoader`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
