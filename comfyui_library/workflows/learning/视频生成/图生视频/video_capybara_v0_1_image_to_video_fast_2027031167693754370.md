---
key: 视频生成/图生视频/video_capybara_v0_1_image_to_video_fast_2027031167693754370.json
name: video_capybara_v0_1_image_to_video_fast_2027031167693754370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/video_capybara_v0_1_image_to_video_fast_2027031167693754370.json
hash: fec6a63e35f93ae2
coverage: 0.807692
learned_at: 2026-10-15 22:35:15
nodes: [SamplerCustomAdvanced, DualCLIPLoader, VAELoader, CLIPTextEncode, KSamplerSelect, RandomNoise, CLIPVisionLoader, MarkdownNote, CLIPVisionEncode, PrimitiveInt, PrimitiveInt, ResizeAndPadImage, MarkdownNote, CLIPTextEncode, SaveVideo, LoadImage, MarkdownNote, ImageResizeKJv2, HunyuanVideo15ImageToVideo, UNETLoader, CFGGuider, BasicScheduler, VAEDecode, CreateVideo, LoraLoaderModelOnly, ModelSamplingSD3]
patterns: []
missing: []
---

# 视频生成/图生视频/video_capybara_v0_1_image_to_video_fast_2027031167693754370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027031167693754370.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `SamplerCustomAdvanced` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CLIPVisionLoader`
- `MarkdownNote`
- `CLIPVisionEncode`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResizeAndPadImage`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `LoadImage`
- `MarkdownNote`
- `ImageResizeKJv2`
- `HunyuanVideo15ImageToVideo`
- `UNETLoader` ★核心
- `CFGGuider`
- `BasicScheduler`
- `VAEDecode` ★核心
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`SamplerCustomAdvanced`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSamplerSelect`、`RandomNoise`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ResizeAndPadImage`、`SaveVideo`、`LoadImage`、`ImageResizeKJv2`、`HunyuanVideo15ImageToVideo`、`UNETLoader`、`CFGGuider`、`BasicScheduler`、`VAEDecode`、`CreateVideo`、`LoraLoaderModelOnly`、`ModelSamplingSD3`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
