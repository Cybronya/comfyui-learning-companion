---
key: 平台全量/视频扩展-Wan2.1-VACE-Native_1925061061618429953.json
name: 视频扩展-Wan2.1-VACE-Native_1925061061618429953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频扩展-Wan2.1-VACE-Native_1925061061618429953.json
hash: dcf25a14e55c6751
coverage: 1
learned_at: 2026-11-14 02:37:58
nodes: [VAEDecode, TrimVideoLatent, CLIPLoader, CLIPTextEncode, VAELoader, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, CFGZeroStarAndInit, WanVideoEnhanceAVideoKJ, TorchCompileModelWanVideo, PatchModelPatcherOrder, KSampler, CLIPTextEncode, VHS_VideoCombine, VHS_VideoCombine, GetImageSize+, MaskToImage, WanVaceToVideo, String Literal, INTConstant, VHS_LoadVideo, ImagePadKJ, INTConstant, VHS_VideoCombine, ImageResizeKJ]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 87974367444552, "steps": 20}
---

# 平台全量/视频扩展-Wan2.1-VACE-Native_1925061061618429953.json

> 来源文件 `comfyui_library/workflows/平台全量/视频扩展-Wan2.1-VACE-Native_1925061061618429953.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（26 个）：
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `WanVideoEnhanceAVideoKJ`
- `TorchCompileModelWanVideo`
- `PatchModelPatcherOrder`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSize+`
- `MaskToImage`
- `WanVaceToVideo`
- `String Literal`
- `INTConstant`
- `VHS_LoadVideo`
- `ImagePadKJ`
- `INTConstant`
- `VHS_VideoCombine`
- `ImageResizeKJ`

## 关键参数

- `seed` = `87974367444552`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`VAEDecode`、`TrimVideoLatent`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`CFGZeroStarAndInit`、`WanVideoEnhanceAVideoKJ`、`TorchCompileModelWanVideo`、`PatchModelPatcherOrder`、`KSampler`、`VHS_VideoCombine`、`GetImageSize+`、`MaskToImage`、`WanVaceToVideo`、`String Literal`、`INTConstant`、`VHS_LoadVideo`、`ImagePadKJ`、`ImageResizeKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、CFGZeroStarAndInit
