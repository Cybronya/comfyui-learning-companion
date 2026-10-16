---
key: 视频生成/图生视频/混元Video1.5大模型——图生视频工作流_1993514480827121665.json
name: 混元Video1.5大模型——图生视频工作流_1993514480827121665.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1993514480827121665.json
hash: 622ba993539fcf3e
coverage: 0.869565
learned_at: 2026-10-15 22:33:18
nodes: [CLIPVisionLoader, DualCLIPLoader, LatentUpscaleModelLoader, UNETLoader, CreateVideo, CLIPVisionEncode, HunyuanVideo15SuperResolution, CLIPTextEncode, CreateVideo, VAELoader, MarkdownNote, HunyuanVideo15ImageToVideo, EasyCache, UNETLoader, Note, MarkdownNote, MarkdownNote, CLIPTextEncode, VAEDecode, VAEDecodeTiled, Note, BasicScheduler, RandomNoise, KSamplerSelect, CFGGuider, ModelSamplingSD3, SamplerCustomAdvanced, EasyCache, VAEDecode, SaveVideo, RandomNoise, KSamplerSelect, ModelSamplingSD3, BasicScheduler, SplitSigmas, DisableNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, CFGGuider, CFGGuider, Note, HunyuanVideo15LatentUpscaleWithModel, SaveVideo, VAEDecodeTiled, LoadImage, Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/混元Video1.5大模型——图生视频工作流_1993514480827121665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1993514480827121665.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `CreateVideo`
- `CLIPVisionEncode`
- `HunyuanVideo15SuperResolution`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `VAELoader`
- `MarkdownNote`
- `HunyuanVideo15ImageToVideo`
- `EasyCache`
- `UNETLoader` ★核心
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `Note`
- `BasicScheduler`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ModelSamplingSD3`
- `SamplerCustomAdvanced` ★核心
- `EasyCache`
- `VAEDecode` ★核心
- `SaveVideo`
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
- `LoadImage`
- `Label (rgthree)`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`CLIPVisionLoader`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`CreateVideo`、`CLIPVisionEncode`、`HunyuanVideo15SuperResolution`、`CLIPTextEncode`、`VAELoader`、`HunyuanVideo15ImageToVideo`、`EasyCache`、`VAEDecode`、`VAEDecodeTiled`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`SaveVideo`、`SplitSigmas`、`DisableNoise`、`HunyuanVideo15LatentUpscaleWithModel`、`LoadImage`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
