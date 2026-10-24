---
key: 图片生成/图生图/【上新】Flux canny model example_1860177603104739329.json
name: 【上新】Flux canny model example_1860177603104739329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【上新】Flux canny model example_1860177603104739329.json
hash: ff50887bddd4fec0
coverage: 0.833333
learned_at: 2026-10-23 11:49:16
nodes: [Label (rgthree), Label (rgthree), FluxGuidance, DualCLIPLoader, InstructPixToPixConditioning, CLIPTextEncode, CLIPTextEncode, Canny, PreviewImage, ShowText|pysssss, RH_Captioner, LoadImage, KSampler, UNETLoader, VAELoader, VAEDecode, SaveImage, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 61520283462654, "steps": 20}
---

# 图片生成/图生图/【上新】Flux canny model example_1860177603104739329.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【上新】Flux canny model example_1860177603104739329.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `FluxGuidance`
- `DualCLIPLoader`
- `InstructPixToPixConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Canny`
- `PreviewImage`
- `ShowText|pysssss`
- `RH_Captioner`
- `LoadImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`

## 关键参数

- `seed` = `61520283462654`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`Label (rgthree)`、`FluxGuidance`、`DualCLIPLoader`、`InstructPixToPixConditioning`、`CLIPTextEncode`、`Canny`、`RH_Captioner`、`LoadImage`、`KSampler`、`UNETLoader`、`VAELoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、Canny、FluxGuidance
