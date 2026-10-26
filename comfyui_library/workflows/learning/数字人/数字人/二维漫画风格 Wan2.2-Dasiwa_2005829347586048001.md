---
key: 数字人/数字人/二维漫画风格 Wan2.2-Dasiwa_2005829347586048001.json
name: 二维漫画风格 Wan2.2-Dasiwa_2005829347586048001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/二维漫画风格 Wan2.2-Dasiwa_2005829347586048001.json
hash: 2a6012805da26e83
coverage: 0.843137
learned_at: 2026-10-26 02:00:11
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, GetNode, GetNode, SeedVR2GGUF, VHS_VideoCombine, VHS_VideoCombine, JWInteger, RIFE VFI, CLIPTextEncode, CLIPVisionLoader, CLIPTextEncode, WanImageToVideo, MathExpression|pysssss, CLIPVisionEncode, CLIPLoader, VAELoader, VHS_VideoCombine, Fast Groups Bypasser (rgthree), LayerUtility: PurgeVRAM V2, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, easy showAnything, Note, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, VAEDecode, JWInteger, easy cleanGpuUsed, easy cleanGpuUsed, RH_LLMAPI_NODE, Note, CombinationText, LoadImage, CR Text, AILab_QwenVL, CR Text Input Switch (4 way)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 数字人/数字人/二维漫画风格 Wan2.2-Dasiwa_2005829347586048001.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/二维漫画风格 Wan2.2-Dasiwa_2005829347586048001.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（51 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `GetNode`
- `GetNode`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `RIFE VFI`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `MathExpression|pysssss`
- `CLIPVisionEncode`
- `CLIPLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: PurgeVRAM V2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `easy showAnything`
- `Note`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `JWInteger`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `RH_LLMAPI_NODE`
- `Note`
- `CombinationText`
- `LoadImage`
- `CR Text`
- `AILab_QwenVL`
- `CR Text Input Switch (4 way)`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（43/51）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2GGUF`、`VHS_VideoCombine`、`JWInteger`、`RIFE VFI`、`CLIPTextEncode`、`CLIPVisionLoader`、`WanImageToVideo`、`MathExpression|pysssss`、`CLIPVisionEncode`、`CLIPLoader`、`VAELoader`、`LayerUtility: PurgeVRAM V2`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`UNETLoader`、`VAEDecode`、`easy cleanGpuUsed`、`RH_LLMAPI_NODE`、`CombinationText`、`LoadImage`、`CR Text`、`AILab_QwenVL`、`CR Text Input Switch (4 way)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
