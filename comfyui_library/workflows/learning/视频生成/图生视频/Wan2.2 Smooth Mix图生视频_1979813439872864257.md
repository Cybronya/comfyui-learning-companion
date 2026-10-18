---
key: 视频生成/图生视频/Wan2.2 Smooth Mix图生视频_1979813439872864257.json
name: Wan2.2 Smooth Mix图生视频_1979813439872864257.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Smooth Mix图生视频_1979813439872864257.json
hash: ad4319a1cbd03c9e
coverage: 0.882353
learned_at: 2026-10-15 22:32:26
nodes: [VHS_VideoCombine, MathExpression|pysssss, MathExpression|pysssss, LayerUtility: BooleanOperatorV2, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, LayerUtility: If , LayerUtility: If , VHS_VideoCombine, SeedVR2GGUF, SeedVR2ExtraArgs, SeedVR2BlockSwap, CLIPTextEncode, UNETLoader, ModelSamplingSD3, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPLoader, ModelSamplingSD3, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, VAELoader, WanImageToVideo, CLIPVisionLoader, CLIPVisionEncode, UNETLoader, easy imageScaleDownToSize, PreviewImage, LayerUtility: BooleanOperatorV2, PreviewImage, easy showAnything, LoadImage, JWInteger, KSamplerAdvanced, KSamplerAdvanced, RIFE VFI, MathExpression|pysssss, GetImageSize, VAEDecode, ImageScale, CLIPTextEncode, ImpactSwitch, easy int, CR Text, easy int, VHS_VideoCombine, AILab_QwenVL, PreviewAny]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Smooth Mix图生视频_1979813439872864257.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979813439872864257.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LayerUtility: BooleanOperatorV2`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy showAnything`
- `LayerUtility: If `
- `LayerUtility: If `
- `VHS_VideoCombine`
- `SeedVR2GGUF`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VAELoader`
- `WanImageToVideo`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `easy imageScaleDownToSize`
- `PreviewImage`
- `LayerUtility: BooleanOperatorV2`
- `PreviewImage`
- `easy showAnything`
- `LoadImage`
- `JWInteger`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `RIFE VFI`
- `MathExpression|pysssss`
- `GetImageSize`
- `VAEDecode` ★核心
- `ImageScale`
- `CLIPTextEncode` ★核心
- `ImpactSwitch`
- `easy int`
- `CR Text`
- `easy int`
- `VHS_VideoCombine`
- `AILab_QwenVL`
- `PreviewAny`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（45/51）

**有卡**：`VHS_VideoCombine`、`MathExpression|pysssss`、`LayerUtility: BooleanOperatorV2`、`LayerUtility: If `、`SeedVR2GGUF`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`CLIPTextEncode`、`UNETLoader`、`ModelSamplingSD3`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`VAELoader`、`WanImageToVideo`、`CLIPVisionLoader`、`CLIPVisionEncode`、`easy imageScaleDownToSize`、`LoadImage`、`JWInteger`、`KSamplerAdvanced`、`RIFE VFI`、`GetImageSize`、`VAEDecode`、`ImageScale`、`easy int`、`CR Text`、`AILab_QwenVL`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、SeedVR2BlockSwap
