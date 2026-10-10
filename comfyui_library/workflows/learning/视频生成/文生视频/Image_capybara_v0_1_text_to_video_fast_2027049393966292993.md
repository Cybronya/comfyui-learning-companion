---
key: 视频生成/文生视频/Image_capybara_v0_1_text_to_video_fast_2027049393966292993.json
name: Image_capybara_v0_1_text_to_video_fast_2027049393966292993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Image_capybara_v0_1_text_to_video_fast_2027049393966292993.json
hash: 74969e5d4c64bb58
coverage: 0.842105
learned_at: 2026-10-11 03:16:44
nodes: [SamplerCustomAdvanced, ModelSamplingSD3, DualCLIPLoader, VAELoader, CLIPTextEncode, KSamplerSelect, RandomNoise, MarkdownNote, MarkdownNote, MarkdownNote, UNETLoader, BasicScheduler, CFGGuider, EmptyHunyuanVideo15Latent, VAEDecode, CreateVideo, SaveVideo, CLIPTextEncode, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/文生视频/Image_capybara_v0_1_text_to_video_fast_2027049393966292993.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Image_capybara_v0_1_text_to_video_fast_2027049393966292993.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `BasicScheduler`
- `CFGGuider`
- `EmptyHunyuanVideo15Latent`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **84%**（16/19）

**有卡**：`SamplerCustomAdvanced`、`ModelSamplingSD3`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSamplerSelect`、`RandomNoise`、`UNETLoader`、`BasicScheduler`、`CFGGuider`、`EmptyHunyuanVideo15Latent`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
