---
key: 视频生成/图生视频/Wan2.2 Smooth Mix高动态图生视频V1_1979756399754383362.json
name: Wan2.2 Smooth Mix高动态图生视频V1_1979756399754383362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Smooth Mix高动态图生视频V1_1979756399754383362.json
hash: 6a83c4ef7ade0b01
coverage: 0.714286
learned_at: 2026-10-15 22:32:26
nodes: [CLIPVisionLoader, CLIPVisionEncode, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, LayerUtility: ImageScaleByAspectRatio V2, ModelPatchTorchSettings, CLIPLoader, VAELoader, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, MathExpression|pysssss, ShowText|pysssss, UNETLoader, UNETLoader, GetNode, GetNode, GetNode, GetNode, WanImageToVideo, JWInteger, Wan22PromptSelector, JWInteger, LoadImage, CLIPTextEncode, Note, CLIPTextEncode, ImpactSwitch, Text Concatenate, RH_LLMAPI_NODE, easy showAnything, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, CR Text, SetNode, SetNode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Smooth Mix高动态图生视频V1_1979756399754383362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979756399754383362.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（42 个）：
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SetNode`
- `MathExpression|pysssss`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideo`
- `JWInteger`
- `Wan22PromptSelector`
- `JWInteger`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `ImpactSwitch`
- `Text Concatenate`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `CR Text`
- `SetNode`
- `SetNode`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **71%**（30/42）

**有卡**：`CLIPVisionLoader`、`CLIPVisionEncode`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`MathExpression|pysssss`、`UNETLoader`、`WanImageToVideo`、`JWInteger`、`Wan22PromptSelector`、`LoadImage`、`CLIPTextEncode`、`Text Concatenate`、`RH_LLMAPI_NODE`、`VAEDecode`、`KSamplerAdvanced`、`VHS_VideoCombine`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
