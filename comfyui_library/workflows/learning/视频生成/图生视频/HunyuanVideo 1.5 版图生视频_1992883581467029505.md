---
key: 视频生成/图生视频/HunyuanVideo 1.5 版图生视频_1992883581467029505.json
name: HunyuanVideo 1.5 版图生视频_1992883581467029505.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1992883581467029505.json
hash: aee76ae0eba9d7bd
coverage: 0.846154
learned_at: 2026-10-15 22:33:17
nodes: [CLIPVisionLoader, DualCLIPLoader, VAELoader, MarkdownNote, KSamplerSelect, CLIPTextEncode, CLIPVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, SamplerCustomAdvanced, RandomNoise, MarkdownNote, MarkdownNote, BasicScheduler, CFGGuider, ModelSamplingSD3, EasyCache, Note, VAEDecodeTiled, CreateVideo, VAEDecode, HunyuanVideo15ImageToVideo, JWInteger, SaveVideo, LoadImage, CLIPTextEncode, UNETLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/HunyuanVideo 1.5 版图生视频_1992883581467029505.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992883581467029505.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `MarkdownNote`
- `MarkdownNote`
- `BasicScheduler`
- `CFGGuider`
- `ModelSamplingSD3`
- `EasyCache`
- `Note`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `HunyuanVideo15ImageToVideo`
- `JWInteger`
- `SaveVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心

## 知识

覆盖率 **85%**（22/26）

**有卡**：`CLIPVisionLoader`、`DualCLIPLoader`、`VAELoader`、`KSamplerSelect`、`CLIPTextEncode`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`SamplerCustomAdvanced`、`RandomNoise`、`BasicScheduler`、`CFGGuider`、`ModelSamplingSD3`、`EasyCache`、`VAEDecodeTiled`、`CreateVideo`、`VAEDecode`、`HunyuanVideo15ImageToVideo`、`JWInteger`、`SaveVideo`、`LoadImage`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
