---
key: 图片生成/文生图/Flux.1-dev-lora-JoyC Beta-Y-Workflow_1934815242520043521.json
name: Flux.1-dev-lora-JoyC Beta-Y-Workflow_1934815242520043521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-dev-lora-JoyC Beta-Y-Workflow_1934815242520043521.json
hash: ed5d6313e59c53f0
coverage: 0.692308
learned_at: 2026-10-10 20:58:36
nodes: [BasicGuider, CLIPTextEncodeFlux, RandomNoise, ShowText|pysssss, JJC_JoyCaption_Custom, ShowText|pysssss, JJC_JoyCaption, ShowText|pysssss, KSamplerSelect, BasicScheduler, Reroute, EmptyLatentImage, SamplerCustomAdvanced, SaveImage, VAEDecode, SDXL Resolutions (JPS), UNETLoader, ShowText|pysssss, SeargePromptCombiner, DualCLIPLoader, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), DrawText+, LoraLoader, VAELoader]
patterns: [lora]
missing: [DrawText+, SDXL Resolutions (JPS)]
parameters: {"batch_size": 1, "height": 1024, "lora_name": "AWPortraitCN_2.safetensors", "strength_clip": 0.8500000000000002, "strength_model": 0.8500000000000002, "width": 768}
discoveries: [次要节点 `DrawText+` 知识库中没有该节点类型的任何知识, 次要节点 `SDXL Resolutions (JPS)` 仅有 Checkpoint/Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Flux.1-dev-lora-JoyC Beta-Y-Workflow_1934815242520043521.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-dev-lora-JoyC Beta-Y-Workflow_1934815242520043521.json`

## 结构

**节点**（26 个）：
- `BasicGuider`
- `CLIPTextEncodeFlux`
- `RandomNoise`
- `ShowText|pysssss`
- `JJC_JoyCaption_Custom`
- `ShowText|pysssss`
- `JJC_JoyCaption`
- `ShowText|pysssss`
- `KSamplerSelect`
- `BasicScheduler`
- `Reroute`
- `EmptyLatentImage`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `SDXL Resolutions (JPS)`
- `UNETLoader`
- `ShowText|pysssss`
- `SeargePromptCombiner`
- `DualCLIPLoader`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `DrawText+`
- `LoraLoader`
- `VAELoader`

**识别到的模式**：lora

## 关键参数

- `batch_size` = `1`
- `height` = `1024`
- `lora_name` = `AWPortraitCN_2.safetensors`
- `strength_clip` = `0.8500000000000002`
- `strength_model` = `0.8500000000000002`
- `width` = `768`

## 知识

覆盖率 **69%**（18/26）

**有卡**：`BasicGuider`、`CLIPTextEncodeFlux`、`RandomNoise`、`ShowText|pysssss`、`JJC_JoyCaption_Custom`、`JJC_JoyCaption`、`KSamplerSelect`、`BasicScheduler`、`Reroute`、`EmptyLatentImage`、`SamplerCustomAdvanced`、`SaveImage`、`VAEDecode`、`SDXL Resolutions (JPS)`、`UNETLoader`

**缺卡**（2）：`DrawText+`、`SDXL Resolutions (JPS)`

## 学习发现

- 次要节点 `DrawText+` 知识库中没有该节点类型的任何知识
- 次要节点 `SDXL Resolutions (JPS)` 仅有 Checkpoint/Resolution 的通用知识，没有该节点自己的说明
