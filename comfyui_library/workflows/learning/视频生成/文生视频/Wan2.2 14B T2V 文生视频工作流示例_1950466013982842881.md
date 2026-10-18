---
key: 视频生成/文生视频/Wan2.2 14B T2V 文生视频工作流示例_1950466013982842881.json
name: Wan2.2 14B T2V 文生视频工作流示例_1950466013982842881.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 14B T2V 文生视频工作流示例_1950466013982842881.json
hash: dae31b1fa8f72b35
coverage: 0.947368
learned_at: 2026-10-15 22:43:36
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, VAEDecode, CLIPTextEncode, MarkdownNote, CreateVideo, SaveVideo, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, EmptyHunyuanLatentVideo]
patterns: []
missing: []
parameters: {"cfg": 15, "denoise": "simple", "sampler_name": 2, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2 14B T2V 文生视频工作流示例_1950466013982842881.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950466013982842881.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `CreateVideo`
- `SaveVideo`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `15`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`LayerUtility: PurgeVRAM V2`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
