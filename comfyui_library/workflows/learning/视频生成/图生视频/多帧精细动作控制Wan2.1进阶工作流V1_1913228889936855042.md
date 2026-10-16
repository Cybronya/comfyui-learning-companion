---
key: 视频生成/图生视频/多帧精细动作控制Wan2.1进阶工作流V1_1913228889936855042.json
name: 多帧精细动作控制Wan2.1进阶工作流V1_1913228889936855042.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1913228889936855042.json
hash: 63678bcb09574972
coverage: 0.890244
learned_at: 2026-10-15 22:29:33
nodes: [GetNode, AddLabel, WanVideoDecode, ImageConcatMulti, WanVideoTextEncode, ImageConcatMulti, WanVideoVACEEncode, WanVideoTeaCache, GetImageSizeAndCount, MaskPreview+, WanVideoBlockSwap, WanVideoExperimentalArgs, WanVideoSLG, Note Plus (mtb), WanVideoVAELoader, LoadWanVideoT5TextEncoder, AddLabel, GetNode, EmptyImage, WanVideoModelLoader, WanVideoSampler, LayerUtility: PurgeVRAM V2, PreviewImage, GetNode, AddLabel, ImageConcatMulti, WanVideoTextEncode, WanVideoVACEEncode, WanVideoTeaCache, GetImageSizeAndCount, MaskPreview+, WanVideoExperimentalArgs, WanVideoSLG, AddLabel, GetNode, EmptyImage, WanVideoSampler, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, PreviewImage, WanVideoDecode, GetNode, AddLabel, ImageConcatMulti, WanVideoTextEncode, ImageConcatMulti, WanVideoVACEEncode, WanVideoTeaCache, GetImageSizeAndCount, MaskPreview+, WanVideoExperimentalArgs, WanVideoSLG, AddLabel, GetNode, EmptyImage, WanVideoSampler, LayerUtility: PurgeVRAM V2, PreviewImage, WanVideoDecode, ImageConcatMulti, ImageResizeKJ, ImageResizeKJ, ImageResizeKJ, ImageResizeKJ, ImageResizeKJ, ImageResizeKJ, GetImageSizeAndCount, GetImageSizeAndCount, GetImageSizeAndCount, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, ImageFromBatch+, WanVideoVACEStartToEndFrame, WanVideoVACEStartToEndFrame, ImageFromBatch+, WanVideoVACEStartToEndFrame, VHS_VideoCombine, ImageBatchMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/多帧精细动作控制Wan2.1进阶工作流V1_1913228889936855042.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1913228889936855042.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（82 个）：
- `GetNode`
- `AddLabel`
- `WanVideoDecode`
- `ImageConcatMulti`
- `WanVideoTextEncode`
- `ImageConcatMulti`
- `WanVideoVACEEncode`
- `WanVideoTeaCache`
- `GetImageSizeAndCount`
- `MaskPreview+`
- `WanVideoBlockSwap`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `Note Plus (mtb)`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `AddLabel`
- `GetNode`
- `EmptyImage`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `GetNode`
- `AddLabel`
- `ImageConcatMulti`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoTeaCache`
- `GetImageSizeAndCount`
- `MaskPreview+`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `AddLabel`
- `GetNode`
- `EmptyImage`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `WanVideoDecode`
- `GetNode`
- `AddLabel`
- `ImageConcatMulti`
- `WanVideoTextEncode`
- `ImageConcatMulti`
- `WanVideoVACEEncode`
- `WanVideoTeaCache`
- `GetImageSizeAndCount`
- `MaskPreview+`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `AddLabel`
- `GetNode`
- `EmptyImage`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `WanVideoDecode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageFromBatch+`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEStartToEndFrame`
- `ImageFromBatch+`
- `WanVideoVACEStartToEndFrame`
- `VHS_VideoCombine`
- `ImageBatchMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **89%**（73/82）

**有卡**：`AddLabel`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`WanVideoTeaCache`、`GetImageSizeAndCount`、`MaskPreview+`、`WanVideoBlockSwap`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`Note Plus (mtb)`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`EmptyImage`、`WanVideoModelLoader`、`WanVideoSampler`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`ImageResizeKJ`、`LoadImage`、`ImageFromBatch+`、`WanVideoVACEStartToEndFrame`、`ImageBatchMulti`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、GetImageSizeAndCount
