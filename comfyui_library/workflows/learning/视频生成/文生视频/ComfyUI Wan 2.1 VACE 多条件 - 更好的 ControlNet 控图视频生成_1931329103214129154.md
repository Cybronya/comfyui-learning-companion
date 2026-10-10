---
key: 视频生成/文生视频/ComfyUI Wan 2.1 VACE 多条件 - 更好的 ControlNet 控图视频生成_1931329103214129154.json
name: ComfyUI Wan 2.1 VACE 多条件 - 更好的 ControlNet 控图视频生成_1931329103214129154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ComfyUI Wan 2.1 VACE 多条件 - 更好的 ControlNet 控图视频生成_1931329103214129154.json
hash: 0db674c3a56e3bf4
coverage: 0.41791
learned_at: 2026-10-10 22:58:48
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, SetNode, GetNode, WanVideoTextEncode, SetNode, SetNode, SetNode, WanVideoDecode, SetNode, DWPreprocessor, INTConstant, INTConstant, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, GetNode, INTConstant, WanVideoSampler, WanVideoVACEEncode, VHS_VideoCombine, VHS_VideoCombine, AIO_Preprocessor, WanVideoVACEEncode, StringConstantMultiline, Note, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoVACEModelSelect, WanVideoLoraSelect, Note, VHS_LoadVideo, LoadImage, Fast Groups Bypasser (rgthree), VHS_VideoCombine, SetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, ImageResizeKJv2, Note, PreviewImage, LoadImage, SetNode, GetNode, GetNode, GetNode, SetNode, DWPreprocessor, Note]
patterns: []
missing: [LayerUtility: PurgeVRAM]
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/ComfyUI Wan 2.1 VACE 多条件 - 更好的 ControlNet 控图视频生成_1931329103214129154.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ComfyUI Wan 2.1 VACE 多条件 - 更好的 ControlNet 控图视频生成_1931329103214129154.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（67 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `WanVideoTextEncode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoDecode`
- `SetNode`
- `DWPreprocessor`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoVACEEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `AIO_Preprocessor`
- `WanVideoVACEEncode`
- `StringConstantMultiline`
- `Note`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `Note`
- `VHS_LoadVideo`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `ImageResizeKJv2`
- `Note`
- `PreviewImage`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `DWPreprocessor`
- `Note`

## 知识

覆盖率 **42%**（28/67）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoDecode`、`DWPreprocessor`、`INTConstant`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoVACEEncode`、`VHS_VideoCombine`、`AIO_Preprocessor`、`StringConstantMultiline`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoInfo`

**缺卡**（1）：`LayerUtility: PurgeVRAM`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
