---
key: 视频生成/文生视频/Wan2.2_文生视频4步LoRA加速-B站UP主@好奇漫步_1983147396660129793.json
name: Wan2.2_文生视频4步LoRA加速-B站UP主@好奇漫步_1983147396660129793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2_文生视频4步LoRA加速-B站UP主@好奇漫步_1983147396660129793.json
hash: 1185b17f308897dd
coverage: 0.868421
learned_at: 2026-10-11 02:45:02
nodes: [CLIPLoader, VAELoader, ModelSamplingSD3, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, CreateVideo, SaveVideo, MarkdownNote, VAEDecode, ModelSamplingSD3, CLIPTextEncode, CreateVideo, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, VAEDecode, KSamplerAdvanced, SaveImage, EmptyHunyuanLatentVideo, Note, SaveVideo, SaveImage, KSamplerAdvanced, UNETLoader, UNETLoader, MarkdownNote, MarkdownNote, Note, CLIPTextEncode, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2_文生视频4步LoRA加速-B站UP主@好奇漫步_1983147396660129793.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2_文生视频4步LoRA加速-B站UP主@好奇漫步_1983147396660129793.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（38 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `SaveVideo`
- `MarkdownNote`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `EmptyHunyuanLatentVideo`
- `Note`
- `SaveVideo`
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **87%**（33/38）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CreateVideo`、`SaveVideo`、`VAEDecode`、`CLIPTextEncode`、`SaveImage`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
