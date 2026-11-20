---
key: 平台全量/Bernini视频编辑-基于Wan2.2视频人物替换动作迁移等_2063291826559344641.json
name: Bernini视频编辑-基于Wan2.2视频人物替换动作迁移等_2063291826559344641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Bernini视频编辑-基于Wan2.2视频人物替换动作迁移等_2063291826559344641.json
hash: 23a5aec034f61340
coverage: 0.886364
learned_at: 2026-11-14 00:20:42
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, VAEDecode, VHS_VideoCombine, KSamplerSelect, SplitSigmas, CLIPTextEncode, MathExpression|pysssss, CLIPLoader, VAELoader, VHS_VideoInfoLoaded, easy getNode, easy setNode, BasicScheduler, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy setNode, LoadImage, LoraLoaderModelOnly, Note, UNETLoader, UNETLoader, LoraLoaderModelOnly, SamplerCustom, SamplerCustom, MarkdownNote, BerniniConditioning, BatchImagesNode, LoadImage, CLIPTextEncode, easy setNode, easy setNode, easy setNode, Int, Int, VHS_LoadVideo, Fast Groups Muter (rgthree), MarkdownNote, MarkdownNote, Int]
patterns: []
missing: []
---

# 平台全量/Bernini视频编辑-基于Wan2.2视频人物替换动作迁移等_2063291826559344641.json

> 来源文件 `comfyui_library/workflows/平台全量/Bernini视频编辑-基于Wan2.2视频人物替换动作迁移等_2063291826559344641.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（44 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `CLIPLoader`
- `VAELoader`
- `VHS_VideoInfoLoaded`
- `easy getNode`
- `easy setNode`
- `BasicScheduler`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `MarkdownNote`
- `BerniniConditioning`
- `BatchImagesNode`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `Int`
- `Int`
- `VHS_LoadVideo`
- `Fast Groups Muter (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `Int`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`PathchSageAttentionKJ`、`VAEDecode`、`VHS_VideoCombine`、`KSamplerSelect`、`SplitSigmas`、`CLIPTextEncode`、`MathExpression|pysssss`、`CLIPLoader`、`VAELoader`、`VHS_VideoInfoLoaded`、`easy getNode`、`easy setNode`、`BasicScheduler`、`LoadImage`、`LoraLoaderModelOnly`、`UNETLoader`、`SamplerCustom`、`BerniniConditioning`、`BatchImagesNode`、`Int`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect
