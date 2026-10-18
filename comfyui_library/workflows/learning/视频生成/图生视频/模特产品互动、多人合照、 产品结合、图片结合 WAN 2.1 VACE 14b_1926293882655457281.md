---
key: 视频生成/图生视频/模特产品互动、多人合照、 产品结合、图片结合 WAN 2.1 VACE 14b_1926293882655457281.json
name: 模特产品互动、多人合照、 产品结合、图片结合 WAN 2.1 VACE 14b_1926293882655457281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/模特产品互动、多人合照、 产品结合、图片结合 WAN 2.1 VACE 14b_1926293882655457281.json
hash: 3062dac38ca9b80f
coverage: 0.74359
learned_at: 2026-10-15 22:29:53
nodes: [SetNode, GetNode, GetNode, WanVideoDecode, GetNode, AddLabel, AddLabel, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, GetNode, GetNode, WanVideoTeaCache, WanVideoExperimentalArgs, WanVideoSLG, ImageConcanate, PreviewImage, WanVideoSampler, SetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, WanVideoVACEEncode, LayerUtility: ImageRemoveAlpha, InspyrenetRembg, PreviewImage, WanVideoVACEModelSelect, SetNode, WanVideoModelLoader, WanVideoBlockSwap, easy imageScaleDownToSize, LoadImage, LoadImage, easy imageScaleDownToSize, ImageResizeKJ, WanVideoTextEncode, VHS_VideoCombine, ImageConcatMulti, Note _O]
patterns: []
missing: []
---

# 视频生成/图生视频/模特产品互动、多人合照、 产品结合、图片结合 WAN 2.1 VACE 14b_1926293882655457281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1926293882655457281.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `AddLabel`
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `WanVideoTeaCache`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `ImageConcanate`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `SetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `LayerUtility: ImageRemoveAlpha`
- `InspyrenetRembg`
- `PreviewImage`
- `WanVideoVACEModelSelect`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `easy imageScaleDownToSize`
- `LoadImage`
- `LoadImage`
- `easy imageScaleDownToSize`
- `ImageResizeKJ`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `Note _O`

## 知识

覆盖率 **74%**（29/39）

**有卡**：`WanVideoDecode`、`AddLabel`、`EmptyImage`、`GetImageSizeAndCount`、`ImageConcatMulti`、`WanVideoTeaCache`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`ImageConcanate`、`WanVideoSampler`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoVACEEncode`、`LayerUtility: ImageRemoveAlpha`、`InspyrenetRembg`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`easy imageScaleDownToSize`、`LoadImage`、`ImageResizeKJ`、`WanVideoTextEncode`、`VHS_VideoCombine`、`Note _O`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、GetImageSizeAndCount
