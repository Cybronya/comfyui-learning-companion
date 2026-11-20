---
key: 平台全量/wan2.2-动作迁移-加速lora-4步极速-14B_fun_control_1956361254153670657.json
name: wan2.2-动作迁移-加速lora-4步极速-14B_fun_control_1956361254153670657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2-动作迁移-加速lora-4步极速-14B_fun_control_1956361254153670657.json
hash: 200a4412bda20407
coverage: 0.93617
learned_at: 2026-11-14 01:19:33
nodes: [CLIPTextEncode, CreateVideo, VAEDecode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, KSamplerAdvanced, SaveVideo, GetVideoComponents, PreviewImage, Canny, LoadVideo, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, LoadImage, Wan22FunControlToVideo, CLIPTextEncode, CreateVideo, VAEDecode, CLIPLoader, SaveVideo, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, MarkdownNote, CLIPTextEncode, VAELoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, GetVideoComponents, CLIPTextEncode, Canny, PreviewImage, easy clearCacheAll, AIO_Preprocessor, Wan22FunControlToVideo, Int, Int, SimpleMath+, LoadVideo, LoadImage, Int]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 平台全量/wan2.2-动作迁移-加速lora-4步极速-14B_fun_control_1956361254153670657.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2-动作迁移-加速lora-4步极速-14B_fun_control_1956361254153670657.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（47 个）：
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `SaveVideo`
- `GetVideoComponents`
- `PreviewImage`
- `Canny`
- `LoadVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoadImage`
- `Wan22FunControlToVideo`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `CLIPLoader`
- `SaveVideo`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetVideoComponents`
- `CLIPTextEncode` ★核心
- `Canny`
- `PreviewImage`
- `easy clearCacheAll`
- `AIO_Preprocessor`
- `Wan22FunControlToVideo`
- `Int`
- `Int`
- `SimpleMath+`
- `LoadVideo`
- `LoadImage`
- `Int`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（44/47）

**有卡**：`CLIPTextEncode`、`CreateVideo`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`SaveVideo`、`GetVideoComponents`、`Canny`、`LoadVideo`、`ModelSamplingSD3`、`LoadImage`、`Wan22FunControlToVideo`、`LoraLoaderModelOnly`、`easy clearCacheAll`、`AIO_Preprocessor`、`Int`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、Canny
