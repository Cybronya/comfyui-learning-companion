---
key: 平台全量/视频变高清_FlashVSR_upscale_example_1987756849841811458.json
name: 视频变高清_FlashVSR_upscale_example_1987756849841811458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频变高清_FlashVSR_upscale_example_1987756849841811458.json
hash: 5db0179a27dd0b5c
coverage: 1
learned_at: 2026-11-14 02:37:15
nodes: [WanVideoAddFlashVSRInput, ImageConcatMulti, WanVideoDecode, GetImageSizeAndCount, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoTorchCompileSettings, WanVideoExtraModelSelect, WanVideoFlashVSRDecoderLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, VHS_VideoCombine, ImageResizeKJv2, WanVideoTextEncode, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/视频变高清_FlashVSR_upscale_example_1987756849841811458.json

> 来源文件 `comfyui_library/workflows/平台全量/视频变高清_FlashVSR_upscale_example_1987756849841811458.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（15 个）：
- `WanVideoAddFlashVSRInput`
- `ImageConcatMulti`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoExtraModelSelect`
- `WanVideoFlashVSRDecoderLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `WanVideoTextEncode`
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`WanVideoAddFlashVSRInput`、`ImageConcatMulti`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoExtraModelSelect`、`WanVideoFlashVSRDecoderLoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanVideoTextEncode`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoFlashVSRDecoderLoader、WanVideoTextEncode、GetImageSizeAndCount、ImageResizeKJv2、ImageConcatMulti
