---
key: 视频生成/文生视频/wan2.2+GGUF+light4步加速lora图生视频工作流_1995845028314505218.json
name: wan2.2+GGUF+light4步加速lora图生视频工作流_1995845028314505218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2+GGUF+light4步加速lora图生视频工作流_1995845028314505218.json
hash: 41e03feec8afaa44
coverage: 0.944444
learned_at: 2026-10-11 02:57:39
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, VAEDecode, CLIPTextEncode, KSamplerAdvanced, UnetLoaderGGUF, CLIPTextEncode, CreateVideo, SaveVideo, UnetLoaderGGUF, KSamplerAdvanced, CLIPLoader, VAELoader, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, WanImageToVideo]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2+GGUF+light4步加速lora图生视频工作流_1995845028314505218.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2+GGUF+light4步加速lora图生视频工作流_1995845028314505218.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `SaveVideo`
- `UnetLoaderGGUF` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanImageToVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`VAEDecode`、`CLIPTextEncode`、`KSamplerAdvanced`、`UnetLoaderGGUF`、`CreateVideo`、`SaveVideo`、`CLIPLoader`、`VAELoader`、`LoadImage`、`WanImageToVideo`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、SaveVideo

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
