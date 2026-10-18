---
key: 视频生成/图生视频/WAN2.2-LightX2V-I2V 图生视频最强动态搭配_1982410881613078529.json
name: WAN2.2-LightX2V-I2V 图生视频最强动态搭配_1982410881613078529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2-LightX2V-I2V 图生视频最强动态搭配_1982410881613078529.json
hash: eae8a3cda3d61476
coverage: 0.792453
learned_at: 2026-10-15 22:32:41
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, wanBlockSwap, wanBlockSwap, CLIPLoader, VAELoader, SetNode, SetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, SetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, SetNode, ModelSamplingSD3, ModelSamplingSD3, Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, GetNode, CLIPVisionLoader, RH_LLMAPI_NODE, CLIPVisionEncode, MathExpression|pysssss, WanImageToVideo, GetNode, Wan22PromptSelector, Note, ShowText|pysssss, JWInteger, JWInteger, CR Text, LoadImage, VHS_VideoCombine, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, VHS_VideoCombine, RIFE VFI, VHS_VideoCombine, ImpactSwitch]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/WAN2.2-LightX2V-I2V 图生视频最强动态搭配_1982410881613078529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982410881613078529.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（53 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `SetNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Text Concatenate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `CLIPVisionLoader`
- `RH_LLMAPI_NODE`
- `CLIPVisionEncode`
- `MathExpression|pysssss`
- `WanImageToVideo`
- `GetNode`
- `Wan22PromptSelector`
- `Note`
- `ShowText|pysssss`
- `JWInteger`
- `JWInteger`
- `CR Text`
- `LoadImage`
- `VHS_VideoCombine`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `RIFE VFI`
- `VHS_VideoCombine`
- `ImpactSwitch`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **79%**（42/53）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`wanBlockSwap`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`Text Concatenate`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`、`CLIPVisionLoader`、`RH_LLMAPI_NODE`、`CLIPVisionEncode`、`MathExpression|pysssss`、`WanImageToVideo`、`Wan22PromptSelector`、`JWInteger`、`CR Text`、`LoadImage`、`VHS_VideoCombine`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2GGUF`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
