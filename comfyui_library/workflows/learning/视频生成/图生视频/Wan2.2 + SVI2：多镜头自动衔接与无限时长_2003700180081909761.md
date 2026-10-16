---
key: 视频生成/图生视频/Wan2.2 + SVI2：多镜头自动衔接与无限时长_2003700180081909761.json
name: Wan2.2 + SVI2：多镜头自动衔接与无限时长_2003700180081909761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2003700180081909761.json
hash: 2b9038402eccc530
coverage: 0.68
learned_at: 2026-10-15 22:33:51
nodes: [INTConstant, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoSampler, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, WanVideoLoraSelect, WanVideoBlockSwap, SetNode, SetNode, SetNode, WanVideoSetBlockSwap, WanVideoSetBlockSwap, InvertMask, WanVideoLoraSelect, WanVideoImageToVideoEncode, GetNode, WanVideoSampler, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, GetNode, INTConstant, GetNode, InvertMask, WanVideoSampler, WanVideoImageToVideoEncode, GetImageSizeAndCount, WanVideoTorchCompileSettings, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, DF_Int_to_Float, SetNode, SetNode, GetNode, SetNode, GetNode, RepeatImageBatch, GetNode, WanVideoTextEncode, WanVideoTextEncode, CR Text, CR Text, WanVideoDecode, GetImageSizeAndCount, RepeatImageBatch, WanVideoVACEStartToEndFrame, GetNode, WanVideoDecode, ImageBatchMulti, VHS_VideoCombine, INTConstant, WanVideoVACEStartToEndFrame, SimpleMath+, MathExpression|pysssss, MathExpression|pysssss, GetImageRangeFromBatch, VHS_VideoCombine, JWInteger, JWInteger, GetNode, PreviewImage, MarkdownNote, JWInteger, JWInteger, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 + SVI2：多镜头自动衔接与无限时长_2003700180081909761.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2003700180081909761.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（75 个）：
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `InvertMask`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `INTConstant`
- `GetNode`
- `InvertMask`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `GetImageSizeAndCount`
- `WanVideoTorchCompileSettings`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `DF_Int_to_Float`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `RepeatImageBatch`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoTextEncode`
- `CR Text`
- `CR Text`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `RepeatImageBatch`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `WanVideoDecode`
- `ImageBatchMulti`
- `VHS_VideoCombine`
- `INTConstant`
- `WanVideoVACEStartToEndFrame`
- `SimpleMath+`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `GetNode`
- `PreviewImage`
- `MarkdownNote`
- `JWInteger`
- `JWInteger`
- `LoadImage`

## 知识

覆盖率 **68%**（51/75）

**有卡**：`INTConstant`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`InvertMask`、`WanVideoImageToVideoEncode`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`DF_Int_to_Float`、`RepeatImageBatch`、`WanVideoTextEncode`、`CR Text`、`WanVideoDecode`、`WanVideoVACEStartToEndFrame`、`ImageBatchMulti`、`VHS_VideoCombine`、`SimpleMath+`、`MathExpression|pysssss`、`GetImageRangeFromBatch`、`JWInteger`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
