---
key: 视频生成/图生视频/首尾帧-Wan2.1-VACE-Native_1925061035089457154.json
name: 首尾帧-Wan2.1-VACE-Native_1925061035089457154.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧-Wan2.1-VACE-Native_1925061035089457154.json
hash: 9eb2a80c9689edb9
coverage: 1
learned_at: 2026-10-15 22:29:51
nodes: [VAEDecode, TrimVideoLatent, CLIPLoader, CLIPTextEncode, VAELoader, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, CFGZeroStarAndInit, WanVideoEnhanceAVideoKJ, TorchCompileModelWanVideo, PatchModelPatcherOrder, VHS_VideoCombine, KSampler, CLIPTextEncode, WanVaceToVideo, String Literal, ImageResizeKJ, INTConstant, LoadImage, LoadImage, INTConstant, GetImageSizeAndCount, ImageResizeKJ, WanVideoVACEStartToEndFrame]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 267162011080790, "steps": 20}
---

# 视频生成/图生视频/首尾帧-Wan2.1-VACE-Native_1925061035089457154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1925061035089457154.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
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
- `VHS_VideoCombine`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `String Literal`
- `ImageResizeKJ`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `WanVideoVACEStartToEndFrame`

## 关键参数

- `seed` = `267162011080790`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`VAEDecode`、`TrimVideoLatent`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`CFGZeroStarAndInit`、`WanVideoEnhanceAVideoKJ`、`TorchCompileModelWanVideo`、`PatchModelPatcherOrder`、`VHS_VideoCombine`、`KSampler`、`WanVaceToVideo`、`String Literal`、`ImageResizeKJ`、`INTConstant`、`LoadImage`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
