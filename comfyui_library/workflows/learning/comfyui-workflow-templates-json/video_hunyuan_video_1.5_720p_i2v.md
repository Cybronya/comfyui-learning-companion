---
key: comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_i2v.json
name: video_hunyuan_video_1.5_720p_i2v
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_i2v.json
hash: 8a86154c9dc2e7e0
official: true
coverage: 0.866667
learned_at: 2026-10-10 22:50:11
nodes: [CLIPVisionLoader, DualCLIPLoader, LatentUpscaleModelLoader, UNETLoader, CreateVideo, CLIPVisionEncode, HunyuanVideo15SuperResolution, CLIPTextEncode, CreateVideo, VAELoader, MarkdownNote, HunyuanVideo15ImageToVideo, EasyCache, UNETLoader, Note, MarkdownNote, MarkdownNote, CLIPTextEncode, LoadImage, VAEDecode, VAEDecodeTiled, Note, BasicScheduler, RandomNoise, KSamplerSelect, CFGGuider, ModelSamplingSD3, SamplerCustomAdvanced, EasyCache, VAEDecode, SaveVideo, RandomNoise, KSamplerSelect, ModelSamplingSD3, BasicScheduler, SplitSigmas, DisableNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, CFGGuider, CFGGuider, Note, HunyuanVideo15LatentUpscaleWithModel, SaveVideo, VAEDecodeTiled]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_i2v.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_i2v.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
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
- `LoadImage`
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

## 知识

覆盖率 **87%**（39/45）

**有卡**：`CLIPVisionLoader`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`CreateVideo`、`CLIPVisionEncode`、`HunyuanVideo15SuperResolution`、`CLIPTextEncode`、`VAELoader`、`HunyuanVideo15ImageToVideo`、`EasyCache`、`LoadImage`、`VAEDecode`、`VAEDecodeTiled`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`SaveVideo`、`SplitSigmas`、`DisableNoise`、`HunyuanVideo15LatentUpscaleWithModel`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
