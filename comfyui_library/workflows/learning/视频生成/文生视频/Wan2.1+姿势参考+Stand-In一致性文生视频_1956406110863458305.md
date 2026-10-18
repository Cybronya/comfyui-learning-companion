---
key: 视频生成/文生视频/Wan2.1+姿势参考+Stand-In一致性文生视频_1956406110863458305.json
name: Wan2.1+姿势参考+Stand-In一致性文生视频_1956406110863458305.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1+姿势参考+Stand-In一致性文生视频_1956406110863458305.json
hash: 0bed14c4a99b7080
coverage: 0.803571
learned_at: 2026-10-15 22:43:41
nodes: [Wan22PromptSelector, ImpactSwitch, GetNode, WanVideoTextEncode, Text Concatenate, WanVideoModelLoader, GetNode, easy imageScaleDownToSize, JWInteger, JWInteger, WanVideoSampler, WanVideoAddStandInLatent, WanVideoEncode, SimpleMath+, VHS_VideoInfo, easy showAnything, VHS_VideoCombine, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, WanVideoVACEModelSelect, RH_LLMAPI_NODE, easy showAnything, FaceProcessorLoader, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, OpenposePreprocessor, VHS_LoadVideo, ImageFromBatch+, ImageConcatMulti, ImageConcanate, LoadImage, ImageResizeKJv2, InspyrenetRembg, LayerUtility: ImageRemoveAlpha, ApplyFaceProcessor, PreviewImage, ImageResizeKJv2, WanVideoVACEStartToEndFrame, WanVideoDecode, GetNode, WanVideoVAELoader, SetNode, SetNode, SetNode, WanVideoBlockSwap, JWInteger, CR Text, WanVideoVACEEncode, WanVideoLoraSelect, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1+姿势参考+Stand-In一致性文生视频_1956406110863458305.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1956406110863458305.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（56 个）：
- `Wan22PromptSelector`
- `ImpactSwitch`
- `GetNode`
- `WanVideoTextEncode`
- `Text Concatenate`
- `WanVideoModelLoader`
- `GetNode`
- `easy imageScaleDownToSize`
- `JWInteger`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoAddStandInLatent`
- `WanVideoEncode`
- `SimpleMath+`
- `VHS_VideoInfo`
- `easy showAnything`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `WanVideoVACEModelSelect`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `FaceProcessorLoader`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `OpenposePreprocessor`
- `VHS_LoadVideo`
- `ImageFromBatch+`
- `ImageConcatMulti`
- `ImageConcanate`
- `LoadImage`
- `ImageResizeKJv2`
- `InspyrenetRembg`
- `LayerUtility: ImageRemoveAlpha`
- `ApplyFaceProcessor`
- `PreviewImage`
- `ImageResizeKJv2`
- `WanVideoVACEStartToEndFrame`
- `WanVideoDecode`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `JWInteger`
- `CR Text`
- `WanVideoVACEEncode`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **80%**（45/56）

**有卡**：`Wan22PromptSelector`、`WanVideoTextEncode`、`Text Concatenate`、`WanVideoModelLoader`、`easy imageScaleDownToSize`、`JWInteger`、`WanVideoSampler`、`WanVideoAddStandInLatent`、`WanVideoEncode`、`SimpleMath+`、`VHS_VideoInfo`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`MultiTalkModelLoader`、`WanVideoVACEModelSelect`、`RH_LLMAPI_NODE`、`FaceProcessorLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`OpenposePreprocessor`、`VHS_LoadVideo`、`ImageFromBatch+`、`ImageConcatMulti`、`ImageConcanate`、`LoadImage`、`ImageResizeKJv2`、`InspyrenetRembg`、`LayerUtility: ImageRemoveAlpha`、`ApplyFaceProcessor`、`WanVideoVACEStartToEndFrame`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`CR Text`、`WanVideoVACEEncode`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、OpenposePreprocessor、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
