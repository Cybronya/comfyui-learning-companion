---
key: 平台全量/【Wan2.1系列】深度控制Depth工作流_1919378897581051906.json
name: 【Wan2.1系列】深度控制Depth工作流_1919378897581051906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【Wan2.1系列】深度控制Depth工作流_1919378897581051906.json
hash: 8711a2e5fa255376
coverage: 0.75
learned_at: 2026-11-14 01:22:21
nodes: [CLIPLoader, PrimitiveNode, Reroute, PrimitiveNode, PreviewImage, DepthAnythingV2Preprocessor, VHS_VideoCombine, UNETLoader, PrimitiveNode, VAEDecode, VAELoader, CLIPTextEncode, ModelSamplingSD3, BasicScheduler, VHS_LoadVideo, ImageScale, CLIPTextEncode, KSamplerSelect, SplitSigmas, SamplerCustom, InstructPixToPixConditioning, LoraLoaderModelOnly, SamplerCustom, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/【Wan2.1系列】深度控制Depth工作流_1919378897581051906.json

> 来源文件 `comfyui_library/workflows/平台全量/【Wan2.1系列】深度控制Depth工作流_1919378897581051906.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `PrimitiveNode`
- `Reroute`
- `PrimitiveNode`
- `PreviewImage`
- `DepthAnythingV2Preprocessor`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `PrimitiveNode`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `BasicScheduler`
- `VHS_LoadVideo`
- `ImageScale`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `SamplerCustom` ★核心
- `InstructPixToPixConditioning`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustom` ★核心
- `MarkdownNote`

## 知识

覆盖率 **75%**（18/24）

**有卡**：`CLIPLoader`、`DepthAnythingV2Preprocessor`、`VHS_VideoCombine`、`UNETLoader`、`VAEDecode`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`BasicScheduler`、`VHS_LoadVideo`、`ImageScale`、`KSamplerSelect`、`SplitSigmas`、`SamplerCustom`、`InstructPixToPixConditioning`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、DepthAnythingV2Preprocessor、KSamplerSelect
