---
key: 视频生成/图生视频/Wan2.2-LightX2V-I2V极致动态图生视频【高质量】_1981254959582928897.json
name: Wan2.2-LightX2V-I2V极致动态图生视频【高质量】_1981254959582928897.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1981254959582928897.json
hash: 827bb27aae28bc25
coverage: 0.969697
learned_at: 2026-10-15 22:32:36
nodes: [easy cleanGpuUsed, LoraLoaderModelOnly, WanImageToVideo, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, VAEDecode, UNETLoader, CLIPTextEncode, VAELoader, Int, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewImage, VHS_VideoCombine, RIFE VFI, VHS_VideoCombine, UNETLoader, RHHiddenNodes, LayerUtility: ImageScaleByAspectRatio V2, CR Text, LoadImage, CLIPTextEncode, CLIPLoader, wanBlockSwap, wanBlockSwap]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-LightX2V-I2V极致动态图生视频【高质量】_1981254959582928897.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981254959582928897.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideo`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Int`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `VHS_VideoCombine`
- `RIFE VFI`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `RHHiddenNodes`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `wanBlockSwap`
- `wanBlockSwap`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`WanImageToVideo`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`INTConstant`、`VAEDecode`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`Int`、`ModelPatchTorchSettings`、`VHS_VideoCombine`、`RIFE VFI`、`RHHiddenNodes`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`LoadImage`、`CLIPLoader`、`wanBlockSwap`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
