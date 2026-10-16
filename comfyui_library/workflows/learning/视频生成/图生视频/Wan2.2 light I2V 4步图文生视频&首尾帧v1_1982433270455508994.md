---
key: 视频生成/图生视频/Wan2.2 light I2V 4步图文生视频&首尾帧v1_1982433270455508994.json
name: Wan2.2 light I2V 4步图文生视频&首尾帧v1_1982433270455508994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1982433270455508994.json
hash: 5ab592a809686b52
coverage: 0.868852
learned_at: 2026-10-15 22:32:41
nodes: [GIMMVFI_interpolate, VAELoader, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPTextEncode, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, CLIPVisionEncode, CLIPVisionEncode, PlaySound|pysssss, ImageResizeKJv2, wanBlockSwap, wanBlockSwap, VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode, PreviewImage, PlaySound|pysssss, VAEDecode, WanImageToVideo, wanBlockSwap, wanBlockSwap, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, VHS_VideoCombine, Note, ImageResizeKJv2, VHS_VideoCombine, DownloadAndLoadGIMMVFIModel, VAEDecode, WanFirstLastFrameToVideo, WanMoeKSampler, CLIPLoader, CLIPVisionLoader, VAELoader, CLIPLoader, Note, Note, WanMoeKSampler, LoadImage, LoadImage, LoadImage, UNETLoader, UNETLoader, UNETLoader, UNETLoader, ImageResizeKJv2, PreviewImage, CLIPTextEncode, CLIPTextEncode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 7, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 light I2V 4步图文生视频&首尾帧v1_1982433270455508994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982433270455508994.json`

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
- `ImageResizeKJv2`
- `wanBlockSwap`
- `wanBlockSwap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `PlaySound|pysssss`
- `VAEDecode` ★核心
- `WanImageToVideo`
- `wanBlockSwap`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VHS_VideoCombine`
- `Note`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `DownloadAndLoadGIMMVFIModel`
- `VAEDecode` ★核心
- `WanFirstLastFrameToVideo`
- `WanMoeKSampler` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPLoader`
- `Note`
- `Note`
- `WanMoeKSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `7`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **87%**（53/61）

**有卡**：`GIMMVFI_interpolate`、`VAELoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`DownloadAndLoadGIMMVFIModel`、`CLIPVisionEncode`、`PlaySound|pysssss`、`ImageResizeKJv2`、`wanBlockSwap`、`VHS_VideoCombine`、`VAEDecode`、`WanImageToVideo`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`WanFirstLastFrameToVideo`、`WanMoeKSampler`、`CLIPLoader`、`CLIPVisionLoader`、`LoadImage`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
