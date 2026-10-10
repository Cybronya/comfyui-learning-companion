---
key: 视频生成/文生视频/重磅发布 Wan 2.1 VACE 14B - 更好更高质量的免费开源AI视频编辑-课程对应工作流_1924830177174429697.json
name: 重磅发布 Wan 2.1 VACE 14B - 更好更高质量的免费开源AI视频编辑-课程对应工作流_1924830177174429697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/重磅发布 Wan 2.1 VACE 14B - 更好更高质量的免费开源AI视频编辑-课程对应工作流_1924830177174429697.json
hash: 328f5d1b6f32dee3
coverage: 0.61039
learned_at: 2026-10-10 23:14:14
nodes: [GetNode, GetNode, SetNode, AIO_Preprocessor, GetNode, GetNode, GetNode, VHS_LoadVideo, PreviewImage, LoadImage, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, WanVideoVACEEncode, WanVideoSampler, LayerUtility: PurgeVRAM, WanVideoVACEStartToEndFrame, SetNode, GetImageSizeAndCount, PreviewImage, MaskPreview+, WanVideoSLG, WanVideoExperimentalArgs, WanVideoDecode, ImageResizeKJv2, PreviewImage, RMBG, RMBG, LoadImage, LoadImage, Note, GetNode, WanVideoDecode, LayerUtility: PurgeVRAM, ImageConcanate, ImageResizeKJv2, ImageResizeKJv2, WanVideoSampler, ImageResizeKJv2, RMBG, VHS_VideoCombine, SetNode, SetNode, SetNode, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, WanVideoVACEEncode, GrowMaskWithBlur, ImageResizeKJv2, GetNode, PreviewImage, ImageFromBatch, GetNode, ImageConcatMulti, ImageResizeKJv2, WanVideoSLG, WanVideoExperimentalArgs, WanVideoSLG, WanVideoExperimentalArgs, WanVideoSampler, GetImageSizeAndCount, ImageConcatMulti, GetNode, GetNode, GetNode, VHS_LoadVideoPath, ImagePadKJ, INTConstant, GetNode, WanVideoDecode, LayerUtility: PurgeVRAM, WanVideoTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoVACEEncode, GetNode, GetNode, VHS_VideoCombine, Fast Groups Bypasser (rgthree), INTConstant, VHS_VideoCombine, GetImageSizeAndCount, GetNode, WanVideoVACEEncode, ImageResizeKJv2, WanVideoExperimentalArgs, WanVideoSLG, Fast Groups Bypasser (rgthree), WanVideoTextEncode, WanVideoTextEncode, Fast Groups Bypasser (rgthree), WanVideoSampler, WanVideoExperimentalArgs, Note, Note, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, Fast Groups Bypasser (rgthree), WanVideoBlockSwap, VHS_VideoCombine, WanVideoTextEncode, INTConstant, Fast Groups Bypasser (rgthree), WanVideoDecode, WanVideoDecode, VHS_VideoCombine, GetNode, LoadImage, LoadImage, GetNode, SetNode, SetNode, WanVideoVACEModelSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, LoadImage, StringConstantMultiline, StringConstant, LayerMask: SegmentAnythingUltra V2, WanVideoVACEModelSelect, WanVideoVAELoader, WanVideoModelLoader, ImageResizeKJv2, INTConstant, INTConstant, INTConstant, Note, WanVideoLoraSelect, VideoInterlacedV2, VHS_VideoCombine, MaskToImage, Mix Color By Mask, Note, VHS_LoadVideo, VHS_VideoCombine, VideoInterlacedV2, VHS_VideoCombine, Note]
patterns: []
missing: [LayerMask: SegmentAnythingUltra V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, Mix Color By Mask, MaskPreview+]
discoveries: [次要节点 `LayerMask: SegmentAnythingUltra V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `Mix Color By Mask` 知识库中没有该节点类型的任何知识, 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/重磅发布 Wan 2.1 VACE 14B - 更好更高质量的免费开源AI视频编辑-课程对应工作流_1924830177174429697.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/重磅发布 Wan 2.1 VACE 14B - 更好更高质量的免费开源AI视频编辑-课程对应工作流_1924830177174429697.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（154 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `AIO_Preprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `PreviewImage`
- `LoadImage`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `WanVideoVACEStartToEndFrame`
- `SetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `MaskPreview+`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `ImageResizeKJv2`
- `PreviewImage`
- `RMBG`
- `RMBG`
- `LoadImage`
- `LoadImage`
- `Note`
- `GetNode`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `ImageConcanate`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `RMBG`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVACEEncode`
- `GrowMaskWithBlur`
- `ImageResizeKJv2`
- `GetNode`
- `PreviewImage`
- `ImageFromBatch`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideoPath`
- `ImagePadKJ`
- `INTConstant`
- `GetNode`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoVACEEncode`
- `ImageResizeKJv2`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoTextEncode`
- `WanVideoTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `Note`
- `Note`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `INTConstant`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoDecode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `LoadImage`
- `StringConstantMultiline`
- `StringConstant`
- `LayerMask: SegmentAnythingUltra V2`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `Note`
- `WanVideoLoraSelect`
- `VideoInterlacedV2`
- `VHS_VideoCombine`
- `MaskToImage`
- `Mix Color By Mask`
- `Note`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VideoInterlacedV2`
- `VHS_VideoCombine`
- `Note`

## 知识

覆盖率 **61%**（94/154）

**有卡**：`AIO_Preprocessor`、`VHS_LoadVideo`、`LoadImage`、`WanVideoSampler`、`ImageResizeKJv2`、`WanVideoVACEEncode`、`WanVideoVACEStartToEndFrame`、`GetImageSizeAndCount`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`RMBG`、`ImageConcanate`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoTeaCache`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`GrowMaskWithBlur`、`ImageFromBatch`、`ImageConcatMulti`、`VHS_LoadVideoPath`、`ImagePadKJ`、`INTConstant`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`WanVideoModelLoader`、`StringConstantMultiline`、`StringConstant`、`WanVideoLoraSelect`、`VideoInterlacedV2`、`MaskToImage`

**缺卡**（9）：`LayerMask: SegmentAnythingUltra V2`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`Mix Color By Mask`、`MaskPreview+`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect

## 学习发现

- 次要节点 `LayerMask: SegmentAnythingUltra V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `Mix Color By Mask` 知识库中没有该节点类型的任何知识
- 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明
