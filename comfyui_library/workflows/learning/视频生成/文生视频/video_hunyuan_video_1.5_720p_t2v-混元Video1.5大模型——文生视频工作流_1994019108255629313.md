---
key: 视频生成/文生视频/video_hunyuan_video_1.5_720p_t2v-混元Video1.5大模型——文生视频工作流_1994019108255629313.json
name: video_hunyuan_video_1.5_720p_t2v-混元Video1.5大模型——文生视频工作流_1994019108255629313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/video_hunyuan_video_1.5_720p_t2v-混元Video1.5大模型——文生视频工作流_1994019108255629313.json
hash: de670312552a4cb8
coverage: 0.791667
learned_at: 2026-10-15 22:47:32
nodes: [DualCLIPLoader, VAELoader, VAEDecode, EasyCache, MarkdownNote, UNETLoader, MarkdownNote, CLIPTextEncode, VAEDecodeTiled, BasicScheduler, RandomNoise, KSamplerSelect, CFGGuider, ModelSamplingSD3, SamplerCustomAdvanced, EmptyHunyuanVideo15Latent, CLIPTextEncode, SaveVideo, Note, Note, AddLabel, CreateVideo, Note, RH_Translator]
patterns: []
missing: []
---

# 视频生成/文生视频/video_hunyuan_video_1.5_720p_t2v-混元Video1.5大模型——文生视频工作流_1994019108255629313.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/video_hunyuan_video_1.5_720p_t2v-混元Video1.5大模型——文生视频工作流_1994019108255629313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（24 个）：
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `EasyCache`
- `MarkdownNote`
- `UNETLoader` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `BasicScheduler`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ModelSamplingSD3`
- `SamplerCustomAdvanced` ★核心
- `EmptyHunyuanVideo15Latent`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `Note`
- `Note`
- `AddLabel`
- `CreateVideo`
- `Note`
- `RH_Translator`

## 知识

覆盖率 **79%**（19/24）

**有卡**：`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`EasyCache`、`UNETLoader`、`CLIPTextEncode`、`VAEDecodeTiled`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`EmptyHunyuanVideo15Latent`、`SaveVideo`、`AddLabel`、`CreateVideo`、`RH_Translator`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled
