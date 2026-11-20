---
key: 平台全量/Bernini视频编辑-v1.0_2070757377581867010.json
name: Bernini视频编辑-v1.0_2070757377581867010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Bernini视频编辑-v1.0_2070757377581867010.json
hash: e497c21cf6f9d456
coverage: 0.928571
learned_at: 2026-11-14 00:20:40
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, VAELoader, easy setNode, easy setNode, easy setNode, UNETLoader, UNETLoader, LoraLoaderModelOnly, MarkdownNote, LoraLoaderModelOnly, SamplerCustom, BasicScheduler, KSamplerSelect, SplitSigmas, SamplerCustom, CLIPTextEncode, MathExpression|pysssss, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, BerniniConditioning, VAEDecode, CLIPLoader, VHS_VideoCombine, CLIPTextEncode, easy setNode, VHS_LoadVideo, easy setNode, CR Text, easy setNode, LoadImage, LoadImage, LoadImage, MarkdownNote, VHS_VideoInfoLoaded, Int, Int, Note]
patterns: []
missing: []
---

# 平台全量/Bernini视频编辑-v1.0_2070757377581867010.json

> 来源文件 `comfyui_library/workflows/平台全量/Bernini视频编辑-v1.0_2070757377581867010.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（42 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VAELoader`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustom` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `SamplerCustom` ★核心
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `BerniniConditioning`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `easy setNode`
- `VHS_LoadVideo`
- `easy setNode`
- `CR Text`
- `easy setNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `VHS_VideoInfoLoaded`
- `Int`
- `Int`
- `Note`

## 知识

覆盖率 **93%**（39/42）

**有卡**：`PathchSageAttentionKJ`、`VAELoader`、`easy setNode`、`UNETLoader`、`LoraLoaderModelOnly`、`SamplerCustom`、`BasicScheduler`、`KSamplerSelect`、`SplitSigmas`、`CLIPTextEncode`、`MathExpression|pysssss`、`easy getNode`、`BerniniConditioning`、`VAEDecode`、`CLIPLoader`、`VHS_VideoCombine`、`VHS_LoadVideo`、`CR Text`、`LoadImage`、`VHS_VideoInfoLoaded`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect
