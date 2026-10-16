---
key: 视频生成/图生视频/（lora版）WAN2.2-LightX2V-I2V图生视频最强动态搭配_1980995649351061505.json
name: （lora版）WAN2.2-LightX2V-I2V图生视频最强动态搭配_1980995649351061505.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1980995649351061505.json
hash: 746c20b240a99a00
coverage: 0.863158
learned_at: 2026-10-15 22:32:36
nodes: [Note, Wan22PromptSelector, GetNode, CLIPVisionLoader, CLIPVisionEncode, SeedVR2BlockSwap, SeedVR2ExtraArgs, RIFE VFI, ModelPatchTorchSettings, CLIPTextEncode, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, Text Concatenate, GetNode, GetNode, VAEDecode, GetNode, WanImageToVideo, SeedVR2GGUF, VHS_VideoCombine, ShowText|pysssss, MathExpression|pysssss, SetNode, VAELoader, SetNode, ModelPatchTorchSettings, PathchSageAttentionKJ, SetNode, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, LoadImage, JWInteger, Fast Groups Bypasser (rgthree), RH_LLMAPI_NODE, LoraLoaderModelOnly, VHS_VideoCombine, VHS_LoadVideo, ImageConcanate, ImageConcanate, VHS_LoadVideo, VHS_LoadVideo, ImageConcanate, VHS_LoadVideo, VHS_LoadVideo, Text Multiline, VHS_VideoCombine, VHS_LoadVideo, VHS_LoadVideo, Text Multiline, VHS_VideoCombine, ImageConcanate, VHS_LoadVideo, VHS_LoadVideo, Text Multiline, ImageConcanate, VHS_LoadVideo, VHS_LoadVideo, VHS_VideoCombine, Text Multiline, ImageConcanate, SetNode, CLIPLoader, KSamplerAdvanced, ImageConcanate, VHS_LoadVideo, VHS_LoadVideo, VHS_VideoCombine, ImpactSwitch, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, ImageConcanate, CR Text, VHS_LoadVideo, VHS_LoadVideo, easy showAnything, LoraLoaderModelOnly, VHS_VideoCombine, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, wanBlockSwap, ModelSamplingSD3, wanBlockSwap, Text Multiline, Text Multiline, Text Multiline, Text Multiline, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/（lora版）WAN2.2-LightX2V-I2V图生视频最强动态搭配_1980995649351061505.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980995649351061505.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（95 个）：
- `Note`
- `Wan22PromptSelector`
- `GetNode`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `RIFE VFI`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Text Concatenate`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `WanImageToVideo`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `MathExpression|pysssss`
- `SetNode`
- `VAELoader`
- `SetNode`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SetNode`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `JWInteger`
- `Fast Groups Bypasser (rgthree)`
- `RH_LLMAPI_NODE`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `ImageConcanate`
- `ImageConcanate`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `ImageConcanate`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `Text Multiline`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `Text Multiline`
- `VHS_VideoCombine`
- `ImageConcanate`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `Text Multiline`
- `ImageConcanate`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `Text Multiline`
- `ImageConcanate`
- `SetNode`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `ImageConcanate`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcanate`
- `CR Text`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（82/95）

**有卡**：`Wan22PromptSelector`、`CLIPVisionLoader`、`CLIPVisionEncode`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`RIFE VFI`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`Text Concatenate`、`VAEDecode`、`WanImageToVideo`、`SeedVR2GGUF`、`VHS_VideoCombine`、`MathExpression|pysssss`、`VAELoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`LoadImage`、`RH_LLMAPI_NODE`、`LoraLoaderModelOnly`、`VHS_LoadVideo`、`ImageConcanate`、`Text Multiline`、`CLIPLoader`、`CR Text`、`UNETLoader`、`wanBlockSwap`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
