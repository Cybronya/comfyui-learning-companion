---
key: 视频生成/图生视频/Wan2.1-图生视频+放大补帧_1908814270581059585.json
name: Wan2.1-图生视频+放大补帧_1908814270581059585.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1-图生视频+放大补帧_1908814270581059585.json
hash: cf3e857a8341e42b
coverage: 1
learned_at: 2026-10-15 22:29:28
nodes: [KSampler, GIMMVFI_interpolate, UnetLoaderGGUF, CLIPVisionLoader, DownloadAndLoadGIMMVFIModel, WanVideoTeaCacheKJ, UpscaleModelLoader, CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, VHS_VideoCombine, WanImageToVideo, LoadImage, ImageUpscaleWithModel, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, ImageScaleBy, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 314831381144241, "steps": 20}
---

# 视频生成/图生视频/Wan2.1-图生视频+放大补帧_1908814270581059585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1908814270581059585.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（21 个）：
- `KSampler` ★核心
- `GIMMVFI_interpolate`
- `UnetLoaderGGUF` ★核心
- `CLIPVisionLoader`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoTeaCacheKJ`
- `UpscaleModelLoader`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `LoadImage`
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `ImageScaleBy`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `314831381144241`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`KSampler`、`GIMMVFI_interpolate`、`UnetLoaderGGUF`、`CLIPVisionLoader`、`DownloadAndLoadGIMMVFIModel`、`WanVideoTeaCacheKJ`、`UpscaleModelLoader`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`VHS_VideoCombine`、`WanImageToVideo`、`LoadImage`、`ImageUpscaleWithModel`、`LayerUtility: PurgeVRAM`、`ImageScaleBy`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
