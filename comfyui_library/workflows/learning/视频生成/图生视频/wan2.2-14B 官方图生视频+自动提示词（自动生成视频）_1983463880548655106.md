---
key: 视频生成/图生视频/wan2.2-14B 官方图生视频+自动提示词（自动生成视频）_1983463880548655106.json
name: wan2.2-14B 官方图生视频+自动提示词（自动生成视频）_1983463880548655106.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-14B 官方图生视频+自动提示词（自动生成视频）_1983463880548655106.json
hash: 8c00e94c3390c067
coverage: 0.885714
learned_at: 2026-10-15 22:32:44
nodes: [DF_Integer, easy showAnything, easy ifElse, TextBox, LayerUtility: PurgeVRAM, easy int, CLIPLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, WanImageToVideo, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything, CR Text Replace, RH_Captioner, VAELoader, PrimitiveBoolean, TextBox, Note, LayerUtility: ImageScaleByAspectRatio V2, TorchCompileModelWanVideoV2, PathchSageAttentionKJ, TextBox, UNETLoader, UNETLoader, PatchModelPatcherOrder, KSamplerAdvanced, ModelSamplingSD3, CLIPVisionLoader, SimpleMath+, KSamplerAdvanced, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2-14B 官方图生视频+自动提示词（自动生成视频）_1983463880548655106.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983463880548655106.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `DF_Integer`
- `easy showAnything`
- `easy ifElse`
- `TextBox`
- `LayerUtility: PurgeVRAM`
- `easy int`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`
- `CR Text Replace`
- `RH_Captioner`
- `VAELoader`
- `PrimitiveBoolean`
- `TextBox`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TorchCompileModelWanVideoV2`
- `PathchSageAttentionKJ`
- `TextBox`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PatchModelPatcherOrder`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `CLIPVisionLoader`
- `SimpleMath+`
- `KSamplerAdvanced` ★核心
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`DF_Integer`、`TextBox`、`LayerUtility: PurgeVRAM`、`easy int`、`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`VAEDecode`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`CR Text Replace`、`RH_Captioner`、`VAELoader`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`TorchCompileModelWanVideoV2`、`PathchSageAttentionKJ`、`UNETLoader`、`PatchModelPatcherOrder`、`KSamplerAdvanced`、`CLIPVisionLoader`、`SimpleMath+`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
