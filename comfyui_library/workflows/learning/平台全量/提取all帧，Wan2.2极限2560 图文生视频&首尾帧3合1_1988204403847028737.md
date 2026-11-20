---
key: 平台全量/提取all帧，Wan2.2极限2560 图文生视频&首尾帧3合1_1988204403847028737.json
name: 提取all帧，Wan2.2极限2560 图文生视频&首尾帧3合1_1988204403847028737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/提取all帧，Wan2.2极限2560 图文生视频&首尾帧3合1_1988204403847028737.json
hash: c7bd490fd28b0fd6
coverage: 0.915493
learned_at: 2026-11-14 02:09:49
nodes: [GIMMVFI_interpolate, VAELoader, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, WanImageToVideo, UNETLoader, wanBlockSwap, wanBlockSwap, LoraLoaderModelOnly, UNETLoader, EmptyHunyuanLatentVideo, VHS_VideoCombine, DownloadAndLoadGIMMVFIModel, CLIPLoader, CLIPVisionLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, WanFirstLastFrameToVideo, CLIPTextEncode, VAEDecode, PlaySound|pysssss, PreviewImage, CLIPVisionEncode, CLIPVisionEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PlaySound|pysssss, PreviewImage, CLIPTextEncode, Fast Groups Bypasser (rgthree), LoadImage, Note, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, VHS_VideoCombine, GetImageSize+, MathExpression_UTK, GetImageRangeFromBatch, LayerUtility: ImageScaleByAspectRatio V2, WanMoeKSampler, SaveImage, Fast Groups Bypasser (rgthree), WanMoeKSampler, LoadImage, LoadImage, CLIPTextEncode, ImageResizeKJv2, wanBlockSwap, wanBlockSwap, UNETLoader, UNETLoader, Fast Groups Bypasser (rgthree), GetImageSize+, SaveImage, VAEDecode, MathExpression_UTK, GetImageRangeFromBatch, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 平台全量/提取all帧，Wan2.2极限2560 图文生视频&首尾帧3合1_1988204403847028737.json

> 来源文件 `comfyui_library/workflows/平台全量/提取all帧，Wan2.2极限2560 图文生视频&首尾帧3合1_1988204403847028737.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `GIMMVFI_interpolate`
- `VAELoader`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `EmptyHunyuanLatentVideo`
- `VHS_VideoCombine`
- `DownloadAndLoadGIMMVFIModel`
- `CLIPLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `WanFirstLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `PlaySound|pysssss`
- `PreviewImage`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PlaySound|pysssss`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Note`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VHS_VideoCombine`
- `GetImageSize+`
- `MathExpression_UTK`
- `GetImageRangeFromBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanMoeKSampler` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `WanMoeKSampler` ★核心
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `wanBlockSwap`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `SaveImage`
- `VAEDecode` ★核心
- `MathExpression_UTK`
- `GetImageRangeFromBatch`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **92%**（65/71）

**有卡**：`GIMMVFI_interpolate`、`VAELoader`、`DownloadAndLoadGIMMVFIModel`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanImageToVideo`、`UNETLoader`、`wanBlockSwap`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`WanFirstLastFrameToVideo`、`VAEDecode`、`PlaySound|pysssss`、`CLIPVisionEncode`、`LoadImage`、`GetImageSize+`、`MathExpression_UTK`、`GetImageRangeFromBatch`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanMoeKSampler`、`SaveImage`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、UNETLoader
