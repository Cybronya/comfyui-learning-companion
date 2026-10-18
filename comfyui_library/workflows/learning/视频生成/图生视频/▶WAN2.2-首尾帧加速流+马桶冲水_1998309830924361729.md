---
key: 视频生成/图生视频/▶WAN2.2-首尾帧加速流+马桶冲水_1998309830924361729.json
name: ▶WAN2.2-首尾帧加速流+马桶冲水_1998309830924361729.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/▶WAN2.2-首尾帧加速流+马桶冲水_1998309830924361729.json
hash: cbb140de5f18e226
coverage: 0.955556
learned_at: 2026-10-15 22:33:31
nodes: [PreviewImage, PreviewImage, wanBlockSwap, WanVideoNAG, PathchSageAttentionKJ, ImageResizeKJ, ModelSamplingSD3, ModelSamplingSD3, FILM VFI, VAEDecode, SimpleMath+, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, ModelPatchTorchSettings, LayerUtility: PurgeVRAM, SimpleMath+, INTConstant, WanFirstLastFrameToVideo, ImageResizeKJ, VAELoader, CLIPLoader, CLIPTextEncode, wanBlockSwap, ModelPatchTorchSettings, UnetLoaderGGUF, LayerUtility: PurgeVRAM, UnetLoaderGGUF, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, SaveImage, LoadImage, VHS_VideoCombine, VHS_VideoCombine, DF_Integer, UNETLoader, CLIPTextEncode, RH_Nano_Banana_Image2Image, RH_Nano_Banana_Image2Image, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionLoader, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/▶WAN2.2-首尾帧加速流+马桶冲水_1998309830924361729.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998309830924361729.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `PreviewImage`
- `PreviewImage`
- `wanBlockSwap`
- `WanVideoNAG`
- `PathchSageAttentionKJ`
- `ImageResizeKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `FILM VFI`
- `VAEDecode` ★核心
- `SimpleMath+`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LayerUtility: PurgeVRAM`
- `SimpleMath+`
- `INTConstant`
- `WanFirstLastFrameToVideo`
- `ImageResizeKJ`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `UnetLoaderGGUF` ★核心
- `LayerUtility: PurgeVRAM`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DF_Integer`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `RH_Nano_Banana_Image2Image`
- `RH_Nano_Banana_Image2Image`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（43/45）

**有卡**：`wanBlockSwap`、`WanVideoNAG`、`PathchSageAttentionKJ`、`ImageResizeKJ`、`ModelSamplingSD3`、`FILM VFI`、`VAEDecode`、`SimpleMath+`、`KSamplerAdvanced`、`ModelPatchTorchSettings`、`LayerUtility: PurgeVRAM`、`INTConstant`、`WanFirstLastFrameToVideo`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`UnetLoaderGGUF`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`、`VHS_VideoCombine`、`DF_Integer`、`RH_Nano_Banana_Image2Image`、`CLIPVisionEncode`、`CLIPVisionLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
