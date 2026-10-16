---
key: 视频生成/图生视频/最强首尾帧视频 - Wan2.2动漫模型DaSiWa-_2009700904043286530.json
name: 最强首尾帧视频 - Wan2.2动漫模型DaSiWa-_2009700904043286530.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2009700904043286530.json
hash: 12f6a04eeb9d930a
coverage: 0.754098
learned_at: 2026-10-15 22:34:14
nodes: [GetNode, CLIPVisionEncode, CLIPVisionEncode, ImageConcanate, CLIPTextEncode, GetNode, ImageResizeKJ, JWInteger, GetNode, KSamplerAdvanced, KSamplerAdvanced, WanFirstLastFrameToVideo, Reroute, Reroute, UNETLoader, UNETLoader, wanBlockSwap, ModelSamplingSD3, ModelPatchTorchSettings, ModelSamplingSD3, wanBlockSwap, ModelPatchTorchSettings, PathchSageAttentionKJ, SetNode, PathchSageAttentionKJ, SetNode, VAELoader, SetNode, JWInteger, MathExpression|pysssss, CLIPVisionLoader, ImageConcanate, Reroute, Reroute, CR Text, RH_LLMAPI_NODE, GetNode, SetNode, Maoyu_ListToString, Note, CLIPLoader, CLIPTextEncode, Qwen3_VQA, Qwen3_VQA, YC_SingleTextNode, YC_SingleTextNode, YC_SingleTextNode, VAEDecode, ImageConcanate, Reroute, Images to RGB, Images to RGB, VHS_VideoCombine, LoadImage, LoadImage, RH_LLMAPI_NODE, easy textSwitch, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, Qwen3_VQA]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/最强首尾帧视频 - Wan2.2动漫模型DaSiWa-_2009700904043286530.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009700904043286530.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（61 个）：
- `GetNode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `GetNode`
- `ImageResizeKJ`
- `JWInteger`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanFirstLastFrameToVideo`
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `VAELoader`
- `SetNode`
- `JWInteger`
- `MathExpression|pysssss`
- `CLIPVisionLoader`
- `ImageConcanate`
- `Reroute`
- `Reroute`
- `CR Text`
- `RH_LLMAPI_NODE`
- `GetNode`
- `SetNode`
- `Maoyu_ListToString`
- `Note`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Qwen3_VQA`
- `Qwen3_VQA`
- `YC_SingleTextNode`
- `YC_SingleTextNode`
- `YC_SingleTextNode`
- `VAEDecode` ★核心
- `ImageConcanate`
- `Reroute`
- `Images to RGB`
- `Images to RGB`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `easy textSwitch`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `Qwen3_VQA`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（46/61）

**有卡**：`CLIPVisionEncode`、`ImageConcanate`、`CLIPTextEncode`、`ImageResizeKJ`、`JWInteger`、`KSamplerAdvanced`、`WanFirstLastFrameToVideo`、`UNETLoader`、`wanBlockSwap`、`ModelSamplingSD3`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`VAELoader`、`MathExpression|pysssss`、`CLIPVisionLoader`、`CR Text`、`RH_LLMAPI_NODE`、`Maoyu_ListToString`、`CLIPLoader`、`Qwen3_VQA`、`YC_SingleTextNode`、`VAEDecode`、`Images to RGB`、`VHS_VideoCombine`、`LoadImage`、`easy textSwitch`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
