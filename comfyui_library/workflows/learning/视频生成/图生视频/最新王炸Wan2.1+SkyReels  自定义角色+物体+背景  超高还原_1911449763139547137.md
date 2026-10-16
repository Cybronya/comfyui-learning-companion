---
key: 视频生成/图生视频/最新王炸Wan2.1+SkyReels  自定义角色+物体+背景  超高还原_1911449763139547137.json
name: 最新王炸Wan2.1+SkyReels  自定义角色+物体+背景  超高还原_1911449763139547137.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1911449763139547137.json
hash: 57870a6ddcfb9916
coverage: 0.680556
learned_at: 2026-10-15 22:29:31
nodes: [ImageRemoveBackground+, ImageCompositeMasked, EmptyImage, GetImageSizeAndCount, TransparentBGSession+, ImageRemoveBackground+, EmptyImage, GetImageSizeAndCount, TransparentBGSession+, SetNode, ImageCompositeMasked, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ImageResizeKJ, GetNode, AddLabel, GetNode, GetNode, AddLabel, AddLabel, ImageResizeKJ, PreviewImage, SetNode, SetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, SimpleMath+, INTConstant, SetNode, ImageConcatMulti, GetNode, ImageResizeKJ, GetNode, WanVideoBlockSwap, ImagePadKJ, ImagePadKJ, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSampler, GetImageRangeFromBatch, WanVideoModelLoader, WanVideoVAELoader, GetNode, GetNode, INTConstant, ImageBatchMulti, ImageBatch, ImageBatchRepeatInterleaving, SetNode, PreviewImage, ImageBatch, GetImageSizeAndCount, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoDecode, WanVideoImageToVideoEncode, LoadImage, LoadImage, LoadImage, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/最新王炸Wan2.1+SkyReels  自定义角色+物体+背景  超高还原_1911449763139547137.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1911449763139547137.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（72 个）：
- `ImageRemoveBackground+`
- `ImageCompositeMasked`
- `EmptyImage`
- `GetImageSizeAndCount`
- `TransparentBGSession+`
- `ImageRemoveBackground+`
- `EmptyImage`
- `GetImageSizeAndCount`
- `TransparentBGSession+`
- `SetNode`
- `ImageCompositeMasked`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJ`
- `GetNode`
- `AddLabel`
- `GetNode`
- `GetNode`
- `AddLabel`
- `AddLabel`
- `ImageResizeKJ`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `SimpleMath+`
- `INTConstant`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `WanVideoBlockSwap`
- `ImagePadKJ`
- `ImagePadKJ`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `GetImageRangeFromBatch`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageBatch`
- `ImageBatchRepeatInterleaving`
- `SetNode`
- `PreviewImage`
- `ImageBatch`
- `GetImageSizeAndCount`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanVideoTextEncode`

## 知识

覆盖率 **68%**（49/72）

**有卡**：`ImageRemoveBackground+`、`ImageCompositeMasked`、`EmptyImage`、`GetImageSizeAndCount`、`TransparentBGSession+`、`ImageResizeKJ`、`AddLabel`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`SimpleMath+`、`INTConstant`、`ImageConcatMulti`、`WanVideoBlockSwap`、`ImagePadKJ`、`VHS_VideoCombine`、`WanVideoSampler`、`GetImageRangeFromBatch`、`WanVideoModelLoader`、`WanVideoVAELoader`、`ImageBatchMulti`、`ImageBatch`、`ImageBatchRepeatInterleaving`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
