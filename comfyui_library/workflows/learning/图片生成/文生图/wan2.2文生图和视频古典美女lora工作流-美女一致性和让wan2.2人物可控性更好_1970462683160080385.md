---
key: 图片生成/文生图/wan2.2文生图和视频古典美女lora工作流-美女一致性和让wan2.2人物可控性更好_1970462683160080385.json
name: wan2.2文生图和视频古典美女lora工作流-美女一致性和让wan2.2人物可控性更好_1970462683160080385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生图和视频古典美女lora工作流-美女一致性和让wan2.2人物可控性更好_1970462683160080385.json
hash: 79d117dc40e30fcf
coverage: 0.589744
learned_at: 2026-10-10 20:59:27
nodes: [GetNode, GetNode, GetNode, CFGZeroStar, UNETLoader, VAELoader, SetNode, LoraLoaderModelOnly, VAEDecode, GetNode, SetNode, SetNode, WanVideoNAG, CLIPLoader, ModelSamplingSD3, PathchSageAttentionKJ, GetNode, MarkdownNote, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, SetNode, JoinStringMulti, SetNode, ModelSamplingSD3, GetNode, CLIPTextEncode, SetNode, Note, VHS_VideoCombine, Note, PreviewImage, EmptyHunyuanLatentVideo, String, JWStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 2.5, "scheduler": "ddim", "seed": "enable", "steps": "randomize"}
---

# 图片生成/文生图/wan2.2文生图和视频古典美女lora工作流-美女一致性和让wan2.2人物可控性更好_1970462683160080385.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2文生图和视频古典美女lora工作流-美女一致性和让wan2.2人物可控性更好_1970462683160080385.json`

## 结构

**节点**（39 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGZeroStar`
- `UNETLoader`
- `VAELoader`
- `SetNode`
- `LoraLoaderModelOnly`
- `VAEDecode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoNAG`
- `CLIPLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `GetNode`
- `MarkdownNote`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `SetNode`
- `JoinStringMulti`
- `SetNode`
- `ModelSamplingSD3`
- `GetNode`
- `CLIPTextEncode`
- `SetNode`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `PreviewImage`
- `EmptyHunyuanLatentVideo`
- `String`
- `JWStringMultiline`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `LoraLoaderModelOnly`

## 关键参数

- `cfg` = `8`
- `denoise` = `simple`
- `sampler_name` = `2.5`
- `scheduler` = `ddim`
- `seed` = `enable`
- `steps` = `randomize`

## 知识

覆盖率 **59%**（23/39）

**有卡**：`GetNode`、`CFGZeroStar`、`UNETLoader`、`VAELoader`、`SetNode`、`LoraLoaderModelOnly`、`VAEDecode`、`WanVideoNAG`、`CLIPLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`MarkdownNote`、`CLIPTextEncode`、`KSamplerAdvanced`、`JoinStringMulti`
