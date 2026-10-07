---
key: comfyui-workflow-templates-json/image_chroma_text_to_image.json
name: image_chroma_text_to_image
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_chroma_text_to_image.json
hash: fd89c0b70424d2b3
official: true
coverage: 0.833333
learned_at: 2026-10-07 21:35:36
nodes: [VAEDecode, CFGGuider, KSamplerSelect, ModelSamplingAuraFlow, VAELoader, RandomNoise, CLIPLoader, BasicScheduler, EmptySD3LatentImage, Note, SaveImage, T5TokenizerOptions, Note, SamplerCustomAdvanced, CLIPTextEncode, CLIPTextEncode, UNETLoader, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/image_chroma_text_to_image.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_chroma_text_to_image.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `VAEDecode` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `RandomNoise`
- `CLIPLoader`
- `BasicScheduler`
- `EmptySD3LatentImage`
- `Note`
- `SaveImage`
- `T5TokenizerOptions`
- `Note`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `MarkdownNote`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`VAEDecode`、`CFGGuider`、`KSamplerSelect`、`ModelSamplingAuraFlow`、`VAELoader`、`RandomNoise`、`CLIPLoader`、`BasicScheduler`、`EmptySD3LatentImage`、`SaveImage`、`T5TokenizerOptions`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
