---
key: 视频生成/图生视频/Dasiwa I2V 图生视频 【 1.0 】_1998592352157622273.json
name: Dasiwa I2V 图生视频 【 1.0 】_1998592352157622273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Dasiwa I2V 图生视频 【 1.0 】_1998592352157622273.json
hash: 54bba0b30333fc6e
coverage: 0.666667
learned_at: 2026-10-15 22:33:32
nodes: [UNETLoader, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, LoadImage, GetNode, SetNode, SetNode, AILab_QwenVL, RH_LLMAPI_NODE, LayerUtility: PurgeVRAM V2, CLIPTextEncode, GetNode, CLIPLoader, VAELoader, GetImageSize, ImageResizeKJv2, CLIPTextEncode, WanImageToVideo, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, KSamplerAdvanced, KSamplerAdvanced, ImageFromBatch+, VAEDecode, RunningHub Deepcleaner, SetNode, Primitive integer [Crystools], SetNode, SetNode, Primitive integer [Crystools], GetNode, SimpleMath+, SetNode, SetNode, SimpleMath+, GetNode, GetNode, GetNode, GetNode, Primitive integer [Crystools], ModelSamplingSD3, LoadImage, VHS_VideoCombine, JjkText, ShowText|pysssss]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Dasiwa I2V 图生视频 【 1.0 】_1998592352157622273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998592352157622273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（48 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `LoadImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `AILab_QwenVL`
- `RH_LLMAPI_NODE`
- `LayerUtility: PurgeVRAM V2`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPLoader`
- `VAELoader`
- `GetImageSize`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageFromBatch+`
- `VAEDecode` ★核心
- `RunningHub Deepcleaner`
- `SetNode`
- `Primitive integer [Crystools]`
- `SetNode`
- `SetNode`
- `Primitive integer [Crystools]`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Primitive integer [Crystools]`
- `ModelSamplingSD3`
- `LoadImage`
- `VHS_VideoCombine`
- `JjkText`
- `ShowText|pysssss`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **67%**（32/48）

**有卡**：`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LoadImage`、`AILab_QwenVL`、`RH_LLMAPI_NODE`、`LayerUtility: PurgeVRAM V2`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`GetImageSize`、`ImageResizeKJv2`、`WanImageToVideo`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionEncode`、`KSamplerAdvanced`、`ImageFromBatch+`、`VAEDecode`、`RunningHub Deepcleaner`、`Primitive integer [Crystools]`、`SimpleMath+`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
