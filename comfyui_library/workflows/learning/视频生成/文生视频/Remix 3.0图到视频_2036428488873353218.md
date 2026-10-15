---
key: 视频生成/文生视频/Remix 3.0图到视频_2036428488873353218.json
name: Remix 3.0图到视频_2036428488873353218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Remix 3.0图到视频_2036428488873353218.json
hash: c5cfd63f358ab78b
coverage: 0.970588
learned_at: 2026-10-15 22:46:53
nodes: [CLIPTextEncode, llama_cpp_instruct_adv, LayerUtility: PurgeVRAM V2, ShowText|pysssss, image_scale_pixel_v2, PainterVRAM, VAELoader, UNETLoader, UNETLoader, llama_cpp_model_loader, llama_cpp_model_loader, easy cleanGpuUsed, CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, WanVideoNAG, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, VAEDecodeTiled, llama_cpp_model_loader, TextInput_, TextInput_, Label (rgthree), UnetLoaderGGUF, ClipLoaderGGUF, PainterI2VAdvanced, VHS_VideoCombine, LoadImage, WanVideoNAG, CLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/Remix 3.0图到视频_2036428488873353218.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Remix 3.0图到视频_2036428488873353218.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（34 个）：
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `LayerUtility: PurgeVRAM V2`
- `ShowText|pysssss`
- `image_scale_pixel_v2`
- `PainterVRAM`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_model_loader`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `VAEDecodeTiled` ★核心
- `llama_cpp_model_loader`
- `TextInput_`
- `TextInput_`
- `Label (rgthree)`
- `UnetLoaderGGUF` ★核心
- `ClipLoaderGGUF`
- `PainterI2VAdvanced`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoNAG`
- `CLIPLoader`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（33/34）

**有卡**：`CLIPTextEncode`、`llama_cpp_instruct_adv`、`LayerUtility: PurgeVRAM V2`、`image_scale_pixel_v2`、`PainterVRAM`、`VAELoader`、`UNETLoader`、`llama_cpp_model_loader`、`easy cleanGpuUsed`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ModelSamplingSD3`、`KSamplerAdvanced`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`VAEDecodeTiled`、`TextInput_`、`Label (rgthree)`、`UnetLoaderGGUF`、`ClipLoaderGGUF`、`PainterI2VAdvanced`、`VHS_VideoCombine`、`LoadImage`、`CLIPLoader`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、VAEDecodeTiled、CLIPLoaderGGUF
