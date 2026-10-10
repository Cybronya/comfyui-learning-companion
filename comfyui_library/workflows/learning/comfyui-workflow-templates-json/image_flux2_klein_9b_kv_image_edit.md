---
key: comfyui-workflow-templates-json/image_flux2_klein_9b_kv_image_edit.json
name: image_flux2_klein_9b_kv_image_edit
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_flux2_klein_9b_kv_image_edit.json
hash: 23cb1b1d9a0f7851
official: true
coverage: 0.826087
learned_at: 2026-10-10 22:47:35
nodes: [KSamplerSelect, UNETLoader, CLIPLoader, CFGGuider, VAELoader, CLIPTextEncode, FluxKVCache, SamplerCustomAdvanced, RandomNoise, VAEDecode, SaveImage, ConditioningZeroOut, Flux2Scheduler, EmptyFlux2LatentImage, GetImageSize, ImageScaleToTotalPixels, ImageScaleToTotalPixels, LoadImage, LoadImage, 27eacb9f-0da2-421d-a0bf-b4b4e5fe5709, MarkdownNote, MarkdownNote, 93041a64-452a-477a-9447-40330b7c1136]
patterns: []
missing: [27eacb9f-0da2-421d-a0bf-b4b4e5fe5709, 93041a64-452a-477a-9447-40330b7c1136]
discoveries: [次要节点 `27eacb9f-0da2-421d-a0bf-b4b4e5fe5709` 知识库中没有该节点类型的任何知识, 次要节点 `93041a64-452a-477a-9447-40330b7c1136` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_flux2_klein_9b_kv_image_edit.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_flux2_klein_9b_kv_image_edit.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CFGGuider`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `FluxKVCache`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadImage`
- `27eacb9f-0da2-421d-a0bf-b4b4e5fe5709`
- `MarkdownNote`
- `MarkdownNote`
- `93041a64-452a-477a-9447-40330b7c1136`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`KSamplerSelect`、`UNETLoader`、`CLIPLoader`、`CFGGuider`、`VAELoader`、`CLIPTextEncode`、`FluxKVCache`、`SamplerCustomAdvanced`、`RandomNoise`、`VAEDecode`、`SaveImage`、`ConditioningZeroOut`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`GetImageSize`、`ImageScaleToTotalPixels`、`LoadImage`

**缺卡**（2）：`27eacb9f-0da2-421d-a0bf-b4b4e5fe5709`、`93041a64-452a-477a-9447-40330b7c1136`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider

## 学习发现

- 次要节点 `27eacb9f-0da2-421d-a0bf-b4b4e5fe5709` 知识库中没有该节点类型的任何知识
- 次要节点 `93041a64-452a-477a-9447-40330b7c1136` 知识库中没有该节点类型的任何知识
