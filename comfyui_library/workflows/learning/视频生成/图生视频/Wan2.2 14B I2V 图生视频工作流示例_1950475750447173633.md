---
key: 视频生成/图生视频/Wan2.2 14B I2V 图生视频工作流示例_1950475750447173633.json
name: Wan2.2 14B I2V 图生视频工作流示例_1950475750447173633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 14B I2V 图生视频工作流示例_1950475750447173633.json
hash: fdca91f449323e8a
coverage: 0.95
learned_at: 2026-10-15 22:30:55
nodes: [CLIPLoader, VAEDecode, CLIPTextEncode, VAELoader, MarkdownNote, CLIPTextEncode, LayerUtility: PurgeVRAM V2, SaveVideo, LayerUtility: PurgeVRAM V2, CreateVideo, LoadImage, UNETLoader, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 15, "denoise": "simple", "sampler_name": 2, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 14B I2V 图生视频工作流示例_1950475750447173633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950475750447173633.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SaveVideo`
- `LayerUtility: PurgeVRAM V2`
- `CreateVideo`
- `LoadImage`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `15`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`CLIPLoader`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`LayerUtility: PurgeVRAM V2`、`SaveVideo`、`CreateVideo`、`LoadImage`、`UNETLoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`WanImageToVideo`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
