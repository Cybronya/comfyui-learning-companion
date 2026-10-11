---
key: 视频生成/文生视频/wan 2.2 图生视频 工作流+全节点注释_2077715652751745025.json
name: wan 2.2 图生视频 工作流+全节点注释_2077715652751745025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan 2.2 图生视频 工作流+全节点注释_2077715652751745025.json
hash: c18c9ae49a714eb5
coverage: 0.46
learned_at: 2026-10-11 20:38:44
nodes: [PathchSageAttentionKJ, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, KSamplerAdvanced, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, CLIPLoader, UNETLoader, CLIPTextEncode, WanImageToVideo, ImageResize+, KSamplerAdvanced, VHS_VideoCombine, VAELoader, SimpleMath+, LoadImage, Int, CR Text, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, CLIPTextEncode, Note]
patterns: []
missing: [CR Text, SimpleMath+, ImageResize+]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "enable", "steps": "increment"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/wan 2.2 图生视频 工作流+全节点注释_2077715652751745025.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan 2.2 图生视频 工作流+全节点注释_2077715652751745025.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（50 个）：
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `ImageResize+`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VAELoader`
- `SimpleMath+`
- `LoadImage`
- `Int`
- `CR Text`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Note`

## 关键参数

- `seed` = `enable`
- `steps` = `increment`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **46%**（23/50）

**有卡**：`PathchSageAttentionKJ`、`wanBlockSwap`、`KSamplerAdvanced`、`VAEDecode`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`WanImageToVideo`、`VHS_VideoCombine`、`VAELoader`、`LoadImage`、`Int`

**缺卡**（3）：`CR Text`、`SimpleMath+`、`ImageResize+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
