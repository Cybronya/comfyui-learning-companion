---
key: 图片生成/图生图/FLUX_图生图_赛博朋克风格V1.0_1922702310974308353.json
name: FLUX_图生图_赛博朋克风格V1.0_1922702310974308353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX_图生图_赛博朋克风格V1.0_1922702310974308353.json
hash: 7cdea28f7bdc610b
coverage: 0.814815
learned_at: 2026-10-23 10:54:46
nodes: [BasicGuider, VAEEncode, CR Latent Batch Size, CLIPTextEncode, VAEDecode, VAELoader, KSamplerSelect, RandomNoise, ImageResize+, SamplerCustomAdvanced, TextInput_, CR Text Concatenate, SaveImage, Florence2Run, Fast Groups Bypasser (rgthree), LoadImage, UNETLoader, DualCLIPLoader, Florence2ModelLoader, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoraLoader, LoraLoader, LoraLoader, Note, BasicScheduler]
patterns: [lora]
missing: []
parameters: {"lora_name": "赛博朋克奇幻风_V0.1.safetensors", "strength_clip": 1, "strength_model": 0.9000000000000001}
---

# 图片生成/图生图/FLUX_图生图_赛博朋克风格V1.0_1922702310974308353.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX_图生图_赛博朋克风格V1.0_1922702310974308353.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `BasicGuider`
- `VAEEncode` ★核心
- `CR Latent Batch Size`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ImageResize+`
- `SamplerCustomAdvanced` ★核心
- `TextInput_`
- `CR Text Concatenate`
- `SaveImage`
- `Florence2Run`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `Note`
- `BasicScheduler`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `赛博朋克奇幻风_V0.1.safetensors`
- `strength_model` = `0.9000000000000001`
- `strength_clip` = `1`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`BasicGuider`、`VAEEncode`、`CR Latent Batch Size`、`CLIPTextEncode`、`VAEDecode`、`VAELoader`、`KSamplerSelect`、`RandomNoise`、`ImageResize+`、`SamplerCustomAdvanced`、`TextInput_`、`CR Text Concatenate`、`SaveImage`、`Florence2Run`、`LoadImage`、`UNETLoader`、`DualCLIPLoader`、`Florence2ModelLoader`、`LoraLoader`、`BasicScheduler`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEEncode
