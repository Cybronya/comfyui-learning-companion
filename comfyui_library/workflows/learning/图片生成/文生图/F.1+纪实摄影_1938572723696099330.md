---
key: 图片生成/文生图/F.1+纪实摄影_1938572723696099330.json
name: F.1+纪实摄影_1938572723696099330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1+纪实摄影_1938572723696099330.json
hash: 657e28f257a949a4
coverage: 0.933333
learned_at: 2026-10-10 20:58:30
nodes: [RandomNoise, KSamplerSelect, SamplerCustomAdvanced, BasicScheduler, BasicGuider, Note, VAELoader, CLIPTextEncodeFlux, VAEDecode, UNETLoader, DualCLIPLoader, LoraLoader, SeargePromptCombiner, SaveImage, EmptyLatentImage]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 1024, "lora_name": "纪实摄影 F.1_v1.0 (1).safetensors", "strength_clip": 1, "strength_model": 0.8000000000000002, "width": 768}
---

# 图片生成/文生图/F.1+纪实摄影_1938572723696099330.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1+纪实摄影_1938572723696099330.json`

## 结构

**节点**（15 个）：
- `RandomNoise`
- `KSamplerSelect`
- `SamplerCustomAdvanced`
- `BasicScheduler`
- `BasicGuider`
- `Note`
- `VAELoader`
- `CLIPTextEncodeFlux`
- `VAEDecode`
- `UNETLoader`
- `DualCLIPLoader`
- `LoraLoader`
- `SeargePromptCombiner`
- `SaveImage`
- `EmptyLatentImage`

**识别到的模式**：lora

## 关键参数

- `batch_size` = `1`
- `height` = `1024`
- `lora_name` = `纪实摄影 F.1_v1.0 (1).safetensors`
- `strength_clip` = `1`
- `strength_model` = `0.8000000000000002`
- `width` = `768`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicScheduler`、`BasicGuider`、`Note`、`VAELoader`、`CLIPTextEncodeFlux`、`VAEDecode`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`SeargePromptCombiner`、`SaveImage`
