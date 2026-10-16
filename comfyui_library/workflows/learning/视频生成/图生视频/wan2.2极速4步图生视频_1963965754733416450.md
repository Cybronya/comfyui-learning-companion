---
key: 视频生成/图生视频/wan2.2极速4步图生视频_1963965754733416450.json
name: wan2.2极速4步图生视频_1963965754733416450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1963965754733416450.json
hash: 90f1bc7cba511121
coverage: 0.833333
learned_at: 2026-10-15 22:31:34
nodes: [RIFE VFI, FlashVSRNode, CLIPLoader, VAELoader, ModelSamplingSD3, CLIPTextEncode, MarkdownNote, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, MarkdownNote, Note, WanImageToVideo, VAEDecode, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoadImage, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, CreateVideo]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2极速4步图生视频_1963965754733416450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963965754733416450.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（24 个）：
- `RIFE VFI`
- `FlashVSRNode`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `MarkdownNote`
- `Note`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `CreateVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`RIFE VFI`、`FlashVSRNode`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSamplerAdvanced`、`WanImageToVideo`、`VAEDecode`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`CreateVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
