---
key: 平台全量/混元视频生成大模型-视频生视频(V2V) ComfyUI-HunyuanVideoWrapper_1864644037138411521.json
name: 混元视频生成大模型-视频生视频(V2V) ComfyUI-HunyuanVideoWrapper_1864644037138411521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/混元视频生成大模型-视频生视频(V2V) ComfyUI-HunyuanVideoWrapper_1864644037138411521.json
hash: e2055003ad5b198c
coverage: 1
learned_at: 2026-11-14 02:20:28
nodes: [HyVideoModelLoader, HyVideoVAELoader, ImageResizeKJ, GetImageSizeAndCount, HyVideoEncode, ImageConcatMulti, VHS_VideoCombine, VHS_LoadVideo, HyVideoSampler, HyVideoDecode, DownloadAndLoadHyVideoTextEncoder, HyVideoTextEncode]
patterns: []
missing: []
---

# 平台全量/混元视频生成大模型-视频生视频(V2V) ComfyUI-HunyuanVideoWrapper_1864644037138411521.json

> 来源文件 `comfyui_library/workflows/平台全量/混元视频生成大模型-视频生视频(V2V) ComfyUI-HunyuanVideoWrapper_1864644037138411521.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（12 个）：
- `HyVideoModelLoader`
- `HyVideoVAELoader`
- `ImageResizeKJ`
- `GetImageSizeAndCount`
- `HyVideoEncode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `HyVideoSampler` ★核心
- `HyVideoDecode`
- `DownloadAndLoadHyVideoTextEncoder`
- `HyVideoTextEncode`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`HyVideoModelLoader`、`HyVideoVAELoader`、`ImageResizeKJ`、`GetImageSizeAndCount`、`HyVideoEncode`、`ImageConcatMulti`、`VHS_VideoCombine`、`VHS_LoadVideo`、`HyVideoSampler`、`HyVideoDecode`、`DownloadAndLoadHyVideoTextEncoder`、`HyVideoTextEncode`

**用到的条目**：HyVideoSampler、DownloadAndLoadHyVideoTextEncoder、HyVideoDecode、HyVideoEncode、HyVideoTextEncode、HyVideoVAELoader、GetImageSizeAndCount、ImageResizeKJ
