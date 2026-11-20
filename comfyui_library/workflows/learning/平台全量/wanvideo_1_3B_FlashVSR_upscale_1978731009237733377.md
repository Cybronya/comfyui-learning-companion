---
key: 平台全量/wanvideo_1_3B_FlashVSR_upscale_1978731009237733377.json
name: wanvideo_1_3B_FlashVSR_upscale_1978731009237733377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wanvideo_1_3B_FlashVSR_upscale_1978731009237733377.json
hash: 1158dd86d5f16d12
coverage: 0.882353
learned_at: 2026-11-14 01:20:07
nodes: [MarkdownNote, WanVideoFlashVSRDecoderLoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoExtraModelSelect, WanVideoTextEncode, Note, WanVideoEmptyEmbeds, WanVideoAddFlashVSRInput, GetImageSizeAndCount, WanVideoSampler, ImageConcatMulti, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, ImageResizeKJv2]
patterns: []
missing: []
---

# 平台全量/wanvideo_1_3B_FlashVSR_upscale_1978731009237733377.json

> 来源文件 `comfyui_library/workflows/平台全量/wanvideo_1_3B_FlashVSR_upscale_1978731009237733377.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（17 个）：
- `MarkdownNote`
- `WanVideoFlashVSRDecoderLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoExtraModelSelect`
- `WanVideoTextEncode`
- `Note`
- `WanVideoEmptyEmbeds`
- `WanVideoAddFlashVSRInput`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `ImageResizeKJv2`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`WanVideoFlashVSRDecoderLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoExtraModelSelect`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`WanVideoAddFlashVSRInput`、`GetImageSizeAndCount`、`WanVideoSampler`、`ImageConcatMulti`、`WanVideoDecode`、`VHS_VideoCombine`、`VHS_LoadVideo`、`ImageResizeKJv2`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoFlashVSRDecoderLoader、WanVideoTextEncode、GetImageSizeAndCount、ImageResizeKJv2、ImageConcatMulti
