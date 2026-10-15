---
key: 视频生成/文生视频/Wan2.2 FunCamera镜头控制_1986776770387062786.json
name: Wan2.2 FunCamera镜头控制_1986776770387062786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 FunCamera镜头控制_1986776770387062786.json
hash: 2ec950681897fc51
coverage: 0.837209
learned_at: 2026-10-15 22:47:09
nodes: [CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, CLIPLoader, VAELoader, LoraLoaderModelOnly, VAELoader, UNETLoader, UNETLoader, CLIPLoader, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CreateVideo, CLIPTextEncode, WanCameraEmbedding, MarkdownNote, MarkdownNote, WanCameraImageToVideo, WanCameraImageToVideo, SaveVideo, Note, CreateVideo, PrimitiveInt, PrimitiveFloat, UNETLoader, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, WanCameraEmbedding, LoadImage, CR SDXL Aspect Ratio, SimpleMath+, LoadImage, SaveVideo, KSamplerAdvanced, KSamplerAdvanced, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2 FunCamera镜头控制_1986776770387062786.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 FunCamera镜头控制_1986776770387062786.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（43 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `WanCameraEmbedding`
- `MarkdownNote`
- `MarkdownNote`
- `WanCameraImageToVideo`
- `WanCameraImageToVideo`
- `SaveVideo`
- `Note`
- `CreateVideo`
- `PrimitiveInt`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `WanCameraEmbedding`
- `LoadImage`
- `CR SDXL Aspect Ratio`
- `SimpleMath+`
- `LoadImage`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `5`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（36/43）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`KSamplerAdvanced`、`CreateVideo`、`WanCameraEmbedding`、`WanCameraImageToVideo`、`SaveVideo`、`LoadImage`、`CR SDXL Aspect Ratio`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced
