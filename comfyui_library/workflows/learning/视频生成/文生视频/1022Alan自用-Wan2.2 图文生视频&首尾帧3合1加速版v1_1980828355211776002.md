---
key: 视频生成/文生视频/1022Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1980828355211776002.json
name: 1022Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1980828355211776002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1022Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1980828355211776002.json
hash: 5ef7c57f18e36653
coverage: 0.868852
learned_at: 2026-10-15 22:43:17
nodes: [GIMMVFI_interpolate, VAELoader, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPTextEncode, DownloadAndLoadGIMMVFIModel, CLIPVisionEncode, CLIPVisionEncode, WanFirstLastFrameToVideo, PlaySound|pysssss, VAELoader, CLIPVisionLoader, CLIPLoader, VAEDecode, PreviewImage, VHS_VideoCombine, wanBlockSwap, ModelPatchTorchSettings, PathchSageAttentionKJ, VHS_VideoCombine, PlaySound|pysssss, Note, VAEDecode, wanBlockSwap, PathchSageAttentionKJ, UNETLoader, UNETLoader, CLIPLoader, PreviewImage, CLIPTextEncode, WanImageToVideo, ImageResizeKJv2, ImageResizeKJv2, wanBlockSwap, wanBlockSwap, WanMoeKSampler, DownloadAndLoadGIMMVFIModel, UNETLoader, UNETLoader, ImageResizeKJv2, Note, Note, WanMoeKSampler, ModelPatchTorchSettings, VHS_VideoCombine, EmptyHunyuanLatentVideo, VHS_VideoCombine, GIMMVFI_interpolate, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoadImage, CLIPTextEncode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/文生视频/1022Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1980828355211776002.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1022Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1980828355211776002.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `GIMMVFI_interpolate`
- `VAELoader`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `DownloadAndLoadGIMMVFIModel`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `WanFirstLastFrameToVideo`
- `PlaySound|pysssss`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `VHS_VideoCombine`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `PlaySound|pysssss`
- `Note`
- `VAEDecode` ★核心
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `wanBlockSwap`
- `wanBlockSwap`
- `WanMoeKSampler` ★核心
- `DownloadAndLoadGIMMVFIModel`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `Note`
- `Note`
- `WanMoeKSampler` ★核心
- `ModelPatchTorchSettings`
- `VHS_VideoCombine`
- `EmptyHunyuanLatentVideo`
- `VHS_VideoCombine`
- `GIMMVFI_interpolate`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **87%**（53/61）

**有卡**：`GIMMVFI_interpolate`、`VAELoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`DownloadAndLoadGIMMVFIModel`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`PlaySound|pysssss`、`CLIPVisionLoader`、`CLIPLoader`、`VAEDecode`、`VHS_VideoCombine`、`wanBlockSwap`、`UNETLoader`、`WanImageToVideo`、`ImageResizeKJv2`、`WanMoeKSampler`、`EmptyHunyuanLatentVideo`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
