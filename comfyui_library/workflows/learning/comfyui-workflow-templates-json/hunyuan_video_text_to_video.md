---
key: comfyui-workflow-templates-json/hunyuan_video_text_to_video.json
name: hunyuan_video_text_to_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/hunyuan_video_text_to_video.json
hash: 3f221fb9cb178bf4
official: true
coverage: 0.842105
learned_at: 2026-10-10 22:47:21
nodes: [DualCLIPLoader, UNETLoader, Note, VAELoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerSelect, BasicScheduler, BasicGuider, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, FluxGuidance, VAEDecodeTiled, Note, VAEDecode, CreateVideo, SaveVideo, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/hunyuan_video_text_to_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/hunyuan_video_text_to_video.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `Note`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `FluxGuidance`
- `VAEDecodeTiled` ★核心
- `Note`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `MarkdownNote`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`ModelSamplingSD3`、`RandomNoise`、`SamplerCustomAdvanced`、`FluxGuidance`、`VAEDecodeTiled`、`VAEDecode`、`CreateVideo`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled
