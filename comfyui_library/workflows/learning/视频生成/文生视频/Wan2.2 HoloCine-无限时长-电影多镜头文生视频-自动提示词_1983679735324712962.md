---
key: 视频生成/文生视频/Wan2.2 HoloCine-无限时长-电影多镜头文生视频-自动提示词_1983679735324712962.json
name: Wan2.2 HoloCine-无限时长-电影多镜头文生视频-自动提示词_1983679735324712962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 HoloCine-无限时长-电影多镜头文生视频-自动提示词_1983679735324712962.json
hash: 249ea46df9ef7228
coverage: 0.767442
learned_at: 2026-10-11 02:45:02
nodes: [INTConstant, INTConstant, VHS_VideoCombine, MarkdownNote, MarkdownNote, easy ifElse, CR Text Replace, TextBox, CLIPLoader, ImageFromBatch+, ImageSharpen, easy cleanGpuUsed, VAELoader, RH_Prompter, PathchSageAttentionKJ, TorchCompileModel, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, PathchSageAttentionKJ, TorchCompileModel, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, JjkText, CLIPTextEncode, SimpleMath+, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, MarkdownNote, ShowText, PrimitiveBoolean, Int, JjkText, Int, Int]
patterns: []
missing: [CR Text Replace, ImageFromBatch+, SimpleMath+, easy cleanGpuUsed]
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2 HoloCine-无限时长-电影多镜头文生视频-自动提示词_1983679735324712962.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 HoloCine-无限时长-电影多镜头文生视频-自动提示词_1983679735324712962.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（43 个）：
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `MarkdownNote`
- `MarkdownNote`
- `easy ifElse`
- `CR Text Replace`
- `TextBox`
- `CLIPLoader`
- `ImageFromBatch+`
- `ImageSharpen`
- `easy cleanGpuUsed`
- `VAELoader`
- `RH_Prompter`
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `JjkText`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `MarkdownNote`
- `ShowText`
- `PrimitiveBoolean`
- `Int`
- `JjkText`
- `Int`
- `Int`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **77%**（33/43）

**有卡**：`INTConstant`、`VHS_VideoCombine`、`TextBox`、`CLIPLoader`、`ImageSharpen`、`VAELoader`、`RH_Prompter`、`PathchSageAttentionKJ`、`TorchCompileModel`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`VAEDecode`、`ShowText`、`PrimitiveBoolean`、`Int`

**缺卡**（4）：`CR Text Replace`、`ImageFromBatch+`、`SimpleMath+`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
