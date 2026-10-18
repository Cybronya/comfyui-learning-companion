---
key: 视频生成/图生视频/WAN2.2-LightX2V-图生视频，高速度、超听话（自动提示词）_1981316750769905665.json
name: WAN2.2-LightX2V-图生视频，高速度、超听话（自动提示词）_1981316750769905665.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2-LightX2V-图生视频，高速度、超听话（自动提示词）_1981316750769905665.json
hash: ae14848b19204228
coverage: 0.5
learned_at: 2026-10-15 22:32:37
nodes: [CLIPLoader, Reroute, Reroute, VAELoader, SetNode, SetNode, SetNode, Reroute, SetNode, PreviewImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Reroute, GetNode, GetNode, Reroute, Reroute, Reroute, GetNode, GetNode, GetNode, WanImageToVideo, SetNode, GetImageRangeFromBatch, GetNode, GetNode, VAEDecode, GetImageRangeFromBatch, CLIPTextEncode, VHS_VideoCombine, GetNode, SetNode, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, SetNode, ModelPatchTorchSettings, PathchSageAttentionKJ, MuyeTextEditOutput, SeedVR2BlockSwap, ModelSamplingSD3, SetNode, ModelSamplingSD3, VHS_VideoCombine, FlashVSRNode, ShowText|pysssss, SetNode, GetNode, GetNode, SeedVR2GGUF, RH_Captioner, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, GetNode, LoadImage, Int, VHS_VideoCombine, Int, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, INTConstant, INTConstant, RH_Captioner]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2-LightX2V-图生视频，高速度、超听话（自动提示词）_1981316750769905665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981316750769905665.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `Reroute`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideo`
- `SetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `SetNode`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `MuyeTextEditOutput`
- `SeedVR2BlockSwap`
- `ModelSamplingSD3`
- `SetNode`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `FlashVSRNode`
- `ShowText|pysssss`
- `SetNode`
- `GetNode`
- `GetNode`
- `SeedVR2GGUF`
- `RH_Captioner`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `LoadImage`
- `Int`
- `VHS_VideoCombine`
- `Int`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `INTConstant`
- `INTConstant`
- `RH_Captioner`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **50%**（38/76）

**有卡**：`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanImageToVideo`、`GetImageRangeFromBatch`、`VAEDecode`、`CLIPTextEncode`、`VHS_VideoCombine`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`MuyeTextEditOutput`、`SeedVR2BlockSwap`、`ModelSamplingSD3`、`FlashVSRNode`、`SeedVR2GGUF`、`RH_Captioner`、`KSamplerAdvanced`、`LoadImage`、`Int`、`UNETLoader`、`LoraLoaderModelOnly`、`INTConstant`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
