---
key: 视频生成/图生视频/Wan2.2子弹时间LORA模型，只需要上传一张人物全身照，AI再现《黑客帝国》躲子弹_1983855179189620738.json
name: Wan2.2子弹时间LORA模型，只需要上传一张人物全身照，AI再现《黑客帝国》躲子弹_1983855179189620738.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2子弹时间LORA模型，只需要上传一张人物全身照，AI再现《黑客帝国》躲子弹_1983855179189620738.json
hash: c6a9ab1d966c0740
coverage: 0.857143
learned_at: 2026-10-15 22:32:46
nodes: [CLIPLoader, VAELoader, ModelSamplingSD3, CLIPTextEncode, MarkdownNote, ModelSamplingSD3, CreateVideo, VAEDecode, SaveVideo, Note, MarkdownNote, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, KSamplerAdvanced, WanImageToVideo, KSamplerAdvanced, LoadImage, UNETLoader, Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2子弹时间LORA模型，只需要上传一张人物全身照，AI再现《黑客帝国》躲子弹_1983855179189620738.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983855179189620738.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `ModelSamplingSD3`
- `CreateVideo`
- `VAEDecode` ★核心
- `SaveVideo`
- `Note`
- `MarkdownNote`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `Label (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`CreateVideo`、`VAEDecode`、`SaveVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`WanImageToVideo`、`LoadImage`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
