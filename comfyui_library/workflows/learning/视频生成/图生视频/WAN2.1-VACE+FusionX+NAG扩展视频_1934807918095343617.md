---
key: 视频生成/图生视频/WAN2.1-VACE+FusionX+NAG扩展视频_1934807918095343617.json
name: WAN2.1-VACE+FusionX+NAG扩展视频_1934807918095343617.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.1-VACE+FusionX+NAG扩展视频_1934807918095343617.json
hash: a76ca3ba339b7215
coverage: 0.961538
learned_at: 2026-10-15 22:30:19
nodes: [ImageResizeKJ, GetImageRangeFromBatch, GetImageSizeAndCount, WanVideoSLG, ImageConcatMulti, GetImageSizeAndCount, VHS_VideoCombine, WanVideoApplyNAG, WanVideoVAELoader, EmptyImage, VHS_LoadVideo, GetImageRangeFromBatch, ImagePadKJ, PreviewImage, MaskPreview+, WanVideoExperimentalArgs, WanVideoVACEEncode, WanVideoDecode, AddLabel, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, LoadWanVideoT5TextEncoder, WanVideoMagCache, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1-VACE+FusionX+NAG扩展视频_1934807918095343617.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1934807918095343617.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（26 个）：
- `ImageResizeKJ`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `WanVideoSLG`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoVAELoader`
- `EmptyImage`
- `VHS_LoadVideo`
- `GetImageRangeFromBatch`
- `ImagePadKJ`
- `PreviewImage`
- `MaskPreview+`
- `WanVideoExperimentalArgs`
- `WanVideoVACEEncode`
- `WanVideoDecode`
- `AddLabel`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `LoadWanVideoT5TextEncoder`
- `WanVideoMagCache`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **96%**（25/26）

**有卡**：`ImageResizeKJ`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`WanVideoSLG`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoApplyNAG`、`WanVideoVAELoader`、`EmptyImage`、`VHS_LoadVideo`、`ImagePadKJ`、`MaskPreview+`、`WanVideoExperimentalArgs`、`WanVideoVACEEncode`、`WanVideoDecode`、`AddLabel`、`WanVideoTextEncodeSingle`、`LoadWanVideoT5TextEncoder`、`WanVideoMagCache`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSampler`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoVACEEncode、GetImageSizeAndCount、ImageResizeKJ
