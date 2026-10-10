---
key: 视频生成/文生视频/Hunyuan_Video_1.5_720p_i2v + Upscaler_1998064669535404034.json
name: Hunyuan_Video_1.5_720p_i2v + Upscaler_1998064669535404034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Hunyuan_Video_1.5_720p_i2v + Upscaler_1998064669535404034.json
hash: 375384a42796a2f3
coverage: 0.847826
learned_at: 2026-10-11 02:57:36
nodes: [CLIPVisionLoader, DualCLIPLoader, LatentUpscaleModelLoader, UNETLoader, CLIPVisionEncode, HunyuanVideo15SuperResolution, CLIPTextEncode, CreateVideo, VAELoader, EasyCache, VAEDecode, BasicScheduler, RandomNoise, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, ModelSamplingSD3, BasicScheduler, SplitSigmas, DisableNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, CFGGuider, CFGGuider, Note, HunyuanVideo15LatentUpscaleWithModel, SaveVideo, UNETLoader, VAEDecodeTiled, SaveVideo, EasyCache, ModelSamplingSD3, MarkdownNote, Note, MarkdownNote, VAEDecode, VAEDecodeTiled, CreateVideo, Label (rgthree), MarkdownNote, LoadImage, CLIPTextEncode, Note, HunyuanVideo15ImageToVideo]
patterns: []
missing: [Label (rgthree)]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Hunyuan_Video_1.5_720p_i2v + Upscaler_1998064669535404034.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Hunyuan_Video_1.5_720p_i2v + Upscaler_1998064669535404034.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `CLIPVisionEncode`
- `HunyuanVideo15SuperResolution`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `VAELoader`
- `EasyCache`
- `VAEDecode` ★核心
- `BasicScheduler`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
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
- `UNETLoader` ★核心
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `EasyCache`
- `ModelSamplingSD3`
- `MarkdownNote`
- `Note`
- `MarkdownNote`
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `Label (rgthree)`
- `MarkdownNote`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Note`
- `HunyuanVideo15ImageToVideo`

## 知识

覆盖率 **85%**（39/46）

**有卡**：`CLIPVisionLoader`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`CLIPVisionEncode`、`HunyuanVideo15SuperResolution`、`CLIPTextEncode`、`CreateVideo`、`VAELoader`、`EasyCache`、`VAEDecode`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`SamplerCustomAdvanced`、`ModelSamplingSD3`、`SplitSigmas`、`DisableNoise`、`HunyuanVideo15LatentUpscaleWithModel`、`SaveVideo`、`VAEDecodeTiled`、`LoadImage`、`HunyuanVideo15ImageToVideo`

**缺卡**（1）：`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
