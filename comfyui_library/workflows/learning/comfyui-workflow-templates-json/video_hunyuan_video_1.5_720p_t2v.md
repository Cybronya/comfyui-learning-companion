---
key: comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_t2v.json
name: video_hunyuan_video_1.5_720p_t2v
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_t2v.json
hash: 9b945d0dd0ce8013
official: true
coverage: 0.857143
learned_at: 2026-10-10 22:50:12
nodes: [DualCLIPLoader, UNETLoader, VAELoader, VAEDecode, EasyCache, MarkdownNote, HunyuanVideo15SuperResolution, CLIPTextEncode, Note, UNETLoader, MarkdownNote, LatentUpscaleModelLoader, EasyCache, CLIPTextEncode, VAEDecodeTiled, Note, CreateVideo, VAEDecode, Note, BasicScheduler, RandomNoise, KSamplerSelect, CFGGuider, ModelSamplingSD3, SamplerCustomAdvanced, SaveVideo, CreateVideo, RandomNoise, KSamplerSelect, ModelSamplingSD3, BasicScheduler, SplitSigmas, DisableNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, CFGGuider, CFGGuider, Note, HunyuanVideo15LatentUpscaleWithModel, SaveVideo, VAEDecodeTiled, EmptyHunyuanVideo15Latent]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_t2v.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_t2v.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
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

## 知识

覆盖率 **86%**（36/42）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`VAELoader`、`VAEDecode`、`EasyCache`、`HunyuanVideo15SuperResolution`、`CLIPTextEncode`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`CreateVideo`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`SaveVideo`、`SplitSigmas`、`DisableNoise`、`HunyuanVideo15LatentUpscaleWithModel`、`EmptyHunyuanVideo15Latent`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled
