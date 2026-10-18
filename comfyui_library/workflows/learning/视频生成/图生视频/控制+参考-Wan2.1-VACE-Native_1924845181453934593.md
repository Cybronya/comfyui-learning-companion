---
key: 视频生成/图生视频/控制+参考-Wan2.1-VACE-Native_1924845181453934593.json
name: 控制+参考-Wan2.1-VACE-Native_1924845181453934593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/控制+参考-Wan2.1-VACE-Native_1924845181453934593.json
hash: 632f8f88f9f6314c
coverage: 1
learned_at: 2026-10-15 22:29:51
nodes: [LoadImage, VAEDecode, TrimVideoLatent, CLIPLoader, CLIPTextEncode, VAELoader, UNETLoader, ModelSamplingSD3, CFGZeroStarAndInit, WanVideoEnhanceAVideoKJ, TorchCompileModelWanVideo, PatchModelPatcherOrder, CLIPTextEncode, WanVaceToVideo, ImageResizeKJ, ImageResizeKJ, Florence2Run, LayerUtility: PurgeVRAM, Florence2ModelLoader, VHS_LoadVideo, VHS_VideoCombine, LoraLoaderModelOnly, AIO_Preprocessor, GetImageSizeAndCount, INTConstant, INTConstant, KSampler]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 2578414307595, "steps": 20}
---

# 视频生成/图生视频/控制+参考-Wan2.1-VACE-Native_1924845181453934593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1924845181453934593.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `LoadImage`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `WanVideoEnhanceAVideoKJ`
- `TorchCompileModelWanVideo`
- `PatchModelPatcherOrder`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `Florence2Run`
- `LayerUtility: PurgeVRAM`
- `Florence2ModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `AIO_Preprocessor`
- `GetImageSizeAndCount`
- `INTConstant`
- `INTConstant`
- `KSampler` ★核心

## 关键参数

- `seed` = `2578414307595`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`LoadImage`、`VAEDecode`、`TrimVideoLatent`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`CFGZeroStarAndInit`、`WanVideoEnhanceAVideoKJ`、`TorchCompileModelWanVideo`、`PatchModelPatcherOrder`、`WanVaceToVideo`、`ImageResizeKJ`、`Florence2Run`、`LayerUtility: PurgeVRAM`、`Florence2ModelLoader`、`VHS_LoadVideo`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`AIO_Preprocessor`、`GetImageSizeAndCount`、`INTConstant`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
