---
key: 视频生成/图生视频/video_hunyuan_video_1.5_720p_i2v-混元Video1.5大模型——图生视频工作流_1994018725741477890.json
name: video_hunyuan_video_1.5_720p_i2v-混元Video1.5大模型——图生视频工作流_1994018725741477890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1994018725741477890.json
hash: f84cd6d9b407259c
coverage: 0.814815
learned_at: 2026-10-15 22:33:20
nodes: [CLIPVisionLoader, DualCLIPLoader, CLIPVisionEncode, CLIPTextEncode, VAELoader, HunyuanVideo15ImageToVideo, UNETLoader, MarkdownNote, BasicScheduler, RandomNoise, KSamplerSelect, CFGGuider, ModelSamplingSD3, SamplerCustomAdvanced, EasyCache, VAEDecode, LoadImage, CLIPTextEncode, AddLabel, SaveVideo, VAEDecodeTiled, Note, Note, CreateVideo, RH_Translator, MarkdownNote, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/video_hunyuan_video_1.5_720p_i2v-混元Video1.5大模型——图生视频工作流_1994018725741477890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1994018725741477890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（27 个）：
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `HunyuanVideo15ImageToVideo`
- `UNETLoader` ★核心
- `MarkdownNote`
- `BasicScheduler`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ModelSamplingSD3`
- `SamplerCustomAdvanced` ★核心
- `EasyCache`
- `VAEDecode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `AddLabel`
- `SaveVideo`
- `VAEDecodeTiled` ★核心
- `Note`
- `Note`
- `CreateVideo`
- `RH_Translator`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`CLIPVisionLoader`、`DualCLIPLoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`VAELoader`、`HunyuanVideo15ImageToVideo`、`UNETLoader`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`EasyCache`、`VAEDecode`、`LoadImage`、`AddLabel`、`SaveVideo`、`VAEDecodeTiled`、`CreateVideo`、`RH_Translator`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
