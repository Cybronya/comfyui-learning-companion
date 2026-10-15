---
key: 图片生成/文生图/F.1-FLUX文生图工作流+LORA（一键运行）_1911723649815015426.json
name: F.1-FLUX文生图工作流+LORA（一键运行）_1911723649815015426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1-FLUX文生图工作流+LORA（一键运行）_1911723649815015426.json
hash: 4d44ff9982d06c54
coverage: 1
learned_at: 2026-10-10 20:58:30
nodes: [KSamplerSelect, RandomNoise, BasicGuider, SamplerCustomAdvanced, VAEDecode, SaveImage, UNETLoader, DualCLIPLoader, VAELoader, CLIPTextEncode, LoraLoader, EmptyLatentImage, BasicScheduler]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 1024, "lora_name": "xxc-1.safetensors", "strength_clip": 1, "strength_model": 0.8, "width": 768}
---

# 图片生成/文生图/F.1-FLUX文生图工作流+LORA（一键运行）_1911723649815015426.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1-FLUX文生图工作流+LORA（一键运行）_1911723649815015426.json`

## 结构

**节点**（13 个）：
- `KSamplerSelect`
- `RandomNoise`
- `BasicGuider`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `SaveImage`
- `UNETLoader`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `LoraLoader`
- `EmptyLatentImage`
- `BasicScheduler`

**识别到的模式**：lora

## 关键参数

- `batch_size` = `1`
- `height` = `1024`
- `lora_name` = `xxc-1.safetensors`
- `strength_clip` = `1`
- `strength_model` = `0.8`
- `width` = `768`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`KSamplerSelect`、`RandomNoise`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`LoraLoader`、`EmptyLatentImage`、`BasicScheduler`
