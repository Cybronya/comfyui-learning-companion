---
key: 图片生成/文生图/Wan2.2 Smooth Mix文生视频_1980468292714455042.json
name: Wan2.2 Smooth Mix文生视频_1980468292714455042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 Smooth Mix文生视频_1980468292714455042.json
hash: 1ed6c41a0fb55830
coverage: 0.590909
learned_at: 2026-10-15 22:27:35
nodes: [SetNode, SetNode, SetNode, INTConstant, SetNode, SimpleMath+, SetNode, CLIPLoader, easy cleanGpuUsed, GetNode, VAEDecode, easy cleanGpuUsed, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, easy cleanGpuUsed, GetNode, GetNode, GetNode, SetNode, VAELoader, WanImageToVideo, CLIPTextEncode, SetNode, SetNode, GetNode, ImageFromBatch+, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, easy cleanGpuUsed, SetNode, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, PathchSageAttentionKJ, FloatConstant, CLIPTextEncode, easy seed, SetNode, UNETLoader, INTConstant, INTConstant, UNETLoader, VHS_VideoCombine, easy clearCacheAll, GIMMVFI_interpolate, easy cleanGpuUsed, easy clearCacheAll, DownloadAndLoadGIMMVFIModel, Int, SimpleMath+, GetNode, Primitive string multiline [Crystools], VHS_VideoCombine, SimpleCondition+, GetNode, JjkShowText, RH_LLMAPI_NODE, SetNode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 图片生成/文生图/Wan2.2 Smooth Mix文生视频_1980468292714455042.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 Smooth Mix文生视频_1980468292714455042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（66 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `CLIPLoader`
- `easy cleanGpuUsed`
- `GetNode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAELoader`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageFromBatch+`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `FloatConstant`
- `CLIPTextEncode` ★核心
- `easy seed`
- `SetNode`
- `UNETLoader` ★核心
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `GIMMVFI_interpolate`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `DownloadAndLoadGIMMVFIModel`
- `Int`
- `SimpleMath+`
- `GetNode`
- `Primitive string multiline [Crystools]`
- `VHS_VideoCombine`
- `SimpleCondition+`
- `GetNode`
- `JjkShowText`
- `RH_LLMAPI_NODE`
- `SetNode`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **59%**（39/66）

**有卡**：`INTConstant`、`SimpleMath+`、`CLIPLoader`、`easy cleanGpuUsed`、`VAEDecode`、`VAELoader`、`WanImageToVideo`、`CLIPTextEncode`、`ImageFromBatch+`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`FloatConstant`、`easy seed`、`UNETLoader`、`VHS_VideoCombine`、`easy clearCacheAll`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`Int`、`Primitive string multiline [Crystools]`、`SimpleCondition+`、`JjkShowText`、`RH_LLMAPI_NODE`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、easy seed、FloatConstant
