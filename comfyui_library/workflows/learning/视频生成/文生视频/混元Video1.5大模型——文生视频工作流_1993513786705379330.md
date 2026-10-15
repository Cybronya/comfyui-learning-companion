---
key: 视频生成/文生视频/混元Video1.5大模型——文生视频工作流_1993513786705379330.json
name: 混元Video1.5大模型——文生视频工作流_1993513786705379330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/混元Video1.5大模型——文生视频工作流_1993513786705379330.json
hash: 70afc34897b1d0be
coverage: 0.860465
learned_at: 2026-10-15 22:48:54
nodes: [DualCLIPLoader, UNETLoader, VAELoader, VAEDecode, EasyCache, MarkdownNote, HunyuanVideo15SuperResolution, CLIPTextEncode, Note, UNETLoader, MarkdownNote, LatentUpscaleModelLoader, EasyCache, CLIPTextEncode, VAEDecodeTiled, Note, CreateVideo, VAEDecode, Note, BasicScheduler, RandomNoise, KSamplerSelect, CFGGuider, ModelSamplingSD3, SamplerCustomAdvanced, SaveVideo, CreateVideo, RandomNoise, KSamplerSelect, ModelSamplingSD3, BasicScheduler, SplitSigmas, DisableNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, CFGGuider, CFGGuider, Note, HunyuanVideo15LatentUpscaleWithModel, SaveVideo, VAEDecodeTiled, EmptyHunyuanVideo15Latent, Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/文生视频/混元Video1.5大模型——文生视频工作流_1993513786705379330.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/混元Video1.5大模型——文生视频工作流_1993513786705379330.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `EasyCache`
- `MarkdownNote`
- `HunyuanVideo15SuperResolution`
- `CLIPTextEncode` ★核心
- `Note`
- `UNETLoader` ★核心
- `MarkdownNote`
- `LatentUpscaleModelLoader`
- `EasyCache`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `Note`
- `CreateVideo`
- `VAEDecode` ★核心
- `Note`
- `BasicScheduler`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ModelSamplingSD3`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
- `CreateVideo`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `BasicScheduler`
- `SplitSigmas`
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `CFGGuider`
- `Note`
- `HunyuanVideo15LatentUpscaleWithModel`
- `SaveVideo`
- `VAEDecodeTiled` ★核心
- `EmptyHunyuanVideo15Latent`
- `Label (rgthree)`

## 知识

覆盖率 **86%**（37/43）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`VAELoader`、`VAEDecode`、`EasyCache`、`HunyuanVideo15SuperResolution`、`CLIPTextEncode`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`CreateVideo`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`SaveVideo`、`SplitSigmas`、`DisableNoise`、`HunyuanVideo15LatentUpscaleWithModel`、`EmptyHunyuanVideo15Latent`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled
