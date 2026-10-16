---
key: 视频生成/图生视频/首尾帧 · 幻影引擎 _ Wan2.2双模型首尾帧视频生成工作流_2059769555181985793.json
name: 首尾帧 · 幻影引擎 _ Wan2.2双模型首尾帧视频生成工作流_2059769555181985793.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2059769555181985793.json
hash: 795ab8fc95e0dac2
coverage: 0.566667
learned_at: 2026-10-15 22:38:42
nodes: [PathchSageAttentionKJ, UNETLoader, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, CLIPVisionEncode, VAEDecode, ImageConcanate, ImageConcanate, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, MathExpression|pysssss, ImageResizeKJ, easy textSwitch, GetNode, GetNode, WanFirstLastFrameToVideo, GetNode, CLIPTextEncode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, easy showAnything, GetNode, VHS_VideoCombine, GetNode, VHS_VideoCombine, RIFE VFI, ImageScaleToTotalPixels, VHS_VideoInfoSource, Int, easy showAnything, easy showAnything, easy showAnything, easy showAnything, MathExpression_UTK, VHS_VideoInfoSource, easy showAnything, easy showAnything, GetNode, SetNode, SetNode, VHS_VideoCombine, SetNode, easy showAnything, Int, SeedVR2BlockSwap, SeedVR2ExtraArgs, MathExpression_UTK, GetNode, GetNode, GetNode, SetNode, SetNode, ImageScaleToTotalPixels, CheckpointLoaderSimple, CLIPTextEncode, KSamplerAdvanced, GetNode, SetNode, easy showAnything, GetNode, PreviewImage, GetNode, GetNode, VHS_VideoCombine, VHS_LoadVideo, SetNode, SetNode, CheckpointLoaderSimple, CLIPTextEncode, UNETLoader, ImageConcanate, GetNode, GetNode, GetNode, SetNode, Images to RGB, SetNode, Images to RGB, SetNode, SeedVR2, Int, VHS_LoadVideo, RIFE VFI, CR Text, SetNode, CLIPTextEncode, CLIPTextEncode, SetNode, Text, CLIPTextEncode, LoadImage, ModelPatchTorchSettings, ModelPatchTorchSettings, KSamplerAdvanced, GetNode, GetNode, SetNode, SetNode, CLIPLoader, VAELoader, CheckpointLoaderSimple, LoadImage, ModelSamplingSD3, ModelSamplingSD3, Qwen3_VQA, Fast Groups Bypasser (rgthree), TextInput_, Text, TextInput_]
patterns: []
missing: []
parameters: {"cfg": 6, "checkpoint": "Lock_8.32.safetensors", "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧 · 幻影引擎 _ Wan2.2双模型首尾帧视频生成工作流_2059769555181985793.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059769555181985793.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（120 个）：
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `MathExpression|pysssss`
- `ImageResizeKJ`
- `easy textSwitch`
- `GetNode`
- `GetNode`
- `WanFirstLastFrameToVideo`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `easy showAnything`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `RIFE VFI`
- `ImageScaleToTotalPixels`
- `VHS_VideoInfoSource`
- `Int`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `MathExpression_UTK`
- `VHS_VideoInfoSource`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `easy showAnything`
- `Int`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `MathExpression_UTK`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageScaleToTotalPixels`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `SetNode`
- `easy showAnything`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ImageConcanate`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Images to RGB`
- `SetNode`
- `Images to RGB`
- `SetNode`
- `SeedVR2`
- `Int`
- `VHS_LoadVideo`
- `RIFE VFI`
- `CR Text`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `Text`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Qwen3_VQA`
- `Fast Groups Bypasser (rgthree)`
- `TextInput_`
- `Text`
- `TextInput_`

## 关键参数

- `checkpoint` = `Lock_8.32.safetensors`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **57%**（68/120）

**有卡**：`PathchSageAttentionKJ`、`UNETLoader`、`wanBlockSwap`、`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`VAEDecode`、`ImageConcanate`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`ImageResizeKJ`、`easy textSwitch`、`WanFirstLastFrameToVideo`、`VHS_VideoCombine`、`RIFE VFI`、`ImageScaleToTotalPixels`、`VHS_VideoInfoSource`、`Int`、`MathExpression_UTK`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`CheckpointLoaderSimple`、`KSamplerAdvanced`、`VHS_LoadVideo`、`Images to RGB`、`SeedVR2`、`CR Text`、`Text`、`LoadImage`、`ModelPatchTorchSettings`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`Qwen3_VQA`、`TextInput_`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2
