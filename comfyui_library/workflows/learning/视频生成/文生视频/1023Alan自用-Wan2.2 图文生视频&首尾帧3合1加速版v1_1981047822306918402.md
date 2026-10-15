---
key: 视频生成/文生视频/1023Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1981047822306918402.json
name: 1023Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1981047822306918402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1023Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1981047822306918402.json
hash: 6f4bfe308db5749b
coverage: 0.868852
learned_at: 2026-10-15 22:43:17
nodes: [GIMMVFI_interpolate, VAELoader, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPTextEncode, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, CLIPVisionEncode, CLIPVisionEncode, PlaySound|pysssss, LoadImage, LoadImage, ImageResizeKJv2, ImageResizeKJv2, PreviewImage, CLIPTextEncode, wanBlockSwap, wanBlockSwap, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), CLIPTextEncode, PlaySound|pysssss, VAEDecode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, VHS_VideoCombine, Note, UNETLoader, DownloadAndLoadGIMMVFIModel, Note, VAEDecode, Note, WanFirstLastFrameToVideo, WanMoeKSampler, CLIPLoader, CLIPVisionLoader, VAELoader, UNETLoader, CLIPLoader, WanMoeKSampler, wanBlockSwap, wanBlockSwap, LoraLoaderModelOnly, PreviewImage, LoadImage, Fast Groups Bypasser (rgthree), ImageResizeKJv2, WanImageToVideo, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 7, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/文生视频/1023Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1981047822306918402.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1023Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1981047822306918402.json`

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
- `GIMMVFI_interpolate`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `PlaySound|pysssss`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `PlaySound|pysssss`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `EmptyHunyuanLatentVideo`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VHS_VideoCombine`
- `Note`
- `UNETLoader` ★核心
- `DownloadAndLoadGIMMVFIModel`
- `Note`
- `VAEDecode` ★核心
- `Note`
- `WanFirstLastFrameToVideo`
- `WanMoeKSampler` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `WanMoeKSampler` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `WanImageToVideo`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `7`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **87%**（53/61）

**有卡**：`GIMMVFI_interpolate`、`VAELoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`DownloadAndLoadGIMMVFIModel`、`CLIPVisionEncode`、`PlaySound|pysssss`、`LoadImage`、`ImageResizeKJv2`、`wanBlockSwap`、`VHS_VideoCombine`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`WanFirstLastFrameToVideo`、`WanMoeKSampler`、`CLIPLoader`、`CLIPVisionLoader`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
