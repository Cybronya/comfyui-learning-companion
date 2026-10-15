---
key: 图片生成/文生图/Reality-Simulator真实摄影-QWen-Image_1959596933876756481.json
name: Reality-Simulator真实摄影-QWen-Image_1959596933876756481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Reality-Simulator真实摄影-QWen-Image_1959596933876756481.json
hash: d82c87d1de120565
coverage: 0.764706
learned_at: 2026-10-10 20:59:10
nodes: [KSampler, SaveImage, VAELoader, VAEDecode, CLIPLoader, CLIPTextEncode, UNETLoader, CFGNorm, ModelSamplingAuraFlow, LoraLoaderModelOnly, CLIPTextEncode, PrimitiveString, RH_Captioner, Text Concatenate, easy showAnything, LoadImage, CR SDXL Aspect Ratio]
patterns: []
missing: [Text Concatenate, CR SDXL Aspect Ratio]
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 260801771094525, "steps": 20}
discoveries: [次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Reality-Simulator真实摄影-QWen-Image_1959596933876756481.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Reality-Simulator真实摄影-QWen-Image_1959596933876756481.json`

## 结构

**节点**（17 个）：
- `KSampler`
- `SaveImage`
- `VAELoader`
- `VAEDecode`
- `CLIPLoader`
- `CLIPTextEncode`
- `UNETLoader`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `PrimitiveString`
- `RH_Captioner`
- `Text Concatenate`
- `easy showAnything`
- `LoadImage`
- `CR SDXL Aspect Ratio`

## 关键参数

- `cfg` = `2.5`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `260801771094525`
- `steps` = `20`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`KSampler`、`SaveImage`、`VAELoader`、`VAEDecode`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`CFGNorm`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`PrimitiveString`、`RH_Captioner`

**缺卡**（2）：`Text Concatenate`、`CR SDXL Aspect Ratio`

## 学习发现

- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
