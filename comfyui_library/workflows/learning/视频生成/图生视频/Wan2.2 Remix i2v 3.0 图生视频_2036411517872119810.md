---
key: 视频生成/图生视频/Wan2.2 Remix i2v 3.0 图生视频_2036411517872119810.json
name: Wan2.2 Remix i2v 3.0 图生视频_2036411517872119810.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2036411517872119810.json
hash: 0a38a274a709933c
coverage: 0.815789
learned_at: 2026-10-15 22:35:52
nodes: [RH_LLMAPI_NODE, GetNode, CLIPTextEncode, LayerUtility: TextJoin, GetNode, CLIPTextEncode, Seed (rgthree), INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, SetNode, ImageResize+, ModelSamplingSD3, ModelSamplingSD3, WanImageToVideo, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, Fast Groups Bypasser (rgthree), KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, TextInput_, LayerUtility: PurgeVRAM V2, SetNode, ShowText|pysssss, TextInput_, Fast Groups Bypasser (rgthree), UNETLoader, CLIPLoader, VAELoader, LoadImage, TextInput_, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Remix i2v 3.0 图生视频_2036411517872119810.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036411517872119810.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `RH_LLMAPI_NODE`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LayerUtility: TextJoin`
- `GetNode`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `ImageResize+`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `TextInput_`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `ShowText|pysssss`
- `TextInput_`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `TextInput_`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（31/38）

**有卡**：`RH_LLMAPI_NODE`、`CLIPTextEncode`、`LayerUtility: TextJoin`、`Seed (rgthree)`、`INTConstant`、`ImageResize+`、`ModelSamplingSD3`、`WanImageToVideo`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`TextInput_`、`LayerUtility: PurgeVRAM V2`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
