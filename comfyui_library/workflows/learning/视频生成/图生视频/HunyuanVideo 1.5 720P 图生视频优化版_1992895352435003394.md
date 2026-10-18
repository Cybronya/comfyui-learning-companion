---
key: 视频生成/图生视频/HunyuanVideo 1.5 720P 图生视频优化版_1992895352435003394.json
name: HunyuanVideo 1.5 720P 图生视频优化版_1992895352435003394.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/HunyuanVideo 1.5 720P 图生视频优化版_1992895352435003394.json
hash: d5bb34a4c1a34318
coverage: 0.88
learned_at: 2026-10-15 22:33:17
nodes: [LayerUtility: ImageScaleByAspectRatio V2, JWInteger, CLIPVisionEncode, JjkText, LoadImage, SaveVideo, MarkdownNote, CFGGuider, UNETLoader, DualCLIPLoader, VAELoader, CLIPVisionLoader, HunyuanVideo15ImageToVideo, CLIPTextEncode, CLIPTextEncode, VAEDecode, ModelSamplingSD3, BasicScheduler, Note, VAEDecodeTiled, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, CreateVideo, EasyCache]
patterns: []
missing: []
---

# 视频生成/图生视频/HunyuanVideo 1.5 720P 图生视频优化版_1992895352435003394.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992895352435003394.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `CLIPVisionEncode`
- `JjkText`
- `LoadImage`
- `SaveVideo`
- `MarkdownNote`
- `CFGGuider`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `HunyuanVideo15ImageToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `BasicScheduler`
- `Note`
- `VAEDecodeTiled` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CreateVideo`
- `EasyCache`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`CLIPVisionEncode`、`LoadImage`、`SaveVideo`、`CFGGuider`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`HunyuanVideo15ImageToVideo`、`CLIPTextEncode`、`VAEDecode`、`ModelSamplingSD3`、`BasicScheduler`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`CreateVideo`、`EasyCache`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
