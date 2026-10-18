---
key: 视频生成/图生视频/原生-Wan2.1-GGUF-图生视频+放大补帧_1897558094359285761.json
name: 原生-Wan2.1-GGUF-图生视频+放大补帧_1897558094359285761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/原生-Wan2.1-GGUF-图生视频+放大补帧_1897558094359285761.json
hash: 000f865c98ba77e2
coverage: 1
learned_at: 2026-10-15 22:29:18
nodes: [CLIPTextEncode, CLIPVisionEncode, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, KSampler, VAEDecode, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, VAELoader, CLIPVisionLoader, WanVideoTeaCacheKJ, CLIPLoader, UnetLoaderGGUF, CLIPTextEncode, WanImageToVideo, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 727046368701461, "steps": 20}
---

# 视频生成/图生视频/原生-Wan2.1-GGUF-图生视频+放大补帧_1897558094359285761.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1897558094359285761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（18 个）：
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `VAELoader`
- `CLIPVisionLoader`
- `WanVideoTeaCacheKJ`
- `CLIPLoader`
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `seed` = `727046368701461`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`CLIPTextEncode`、`CLIPVisionEncode`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`KSampler`、`VAEDecode`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`VAELoader`、`CLIPVisionLoader`、`WanVideoTeaCacheKJ`、`CLIPLoader`、`UnetLoaderGGUF`、`WanImageToVideo`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode、ImageUpscaleWithModel
