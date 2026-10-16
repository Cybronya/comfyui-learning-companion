---
key: 视频生成/图生视频/wan2.2 control控制_1966742439342059521.json
name: wan2.2 control控制_1966742439342059521.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1966742439342059521.json
hash: c03146f3aa51c05b
coverage: 0.94
learned_at: 2026-10-15 22:31:39
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, Note, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoDecode, VHS_VideoCombine, SaveLatent, VAELoader, VAEEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSampler, PreviewImage, SaveImage, WanVideoContextOptions, GetImageSizeAndCount, WanVideoEncode, WanVideoControlEmbeds, WanVideoImageToVideoEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, VHS_LoadVideo, LoadImage, CR Prompt Text, easy seed, INTConstant, WanVideoSigmaToStep, Float, WanVideoSampler, WanVideoScheduler, WanVideoScheduler, StringToFloatList, WanVideoLoraSelect, WanVideoLoraSelect, StringToFloatList]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 control控制_1966742439342059521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966742439342059521.json`

## 结构

**生成流程**：Model → Encode → Sampling → Process → Output → Other

**节点**（50 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `Note`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `SaveLatent`
- `VAELoader`
- `VAEEncode` ★核心
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `PreviewImage`
- `SaveImage`
- `WanVideoContextOptions`
- `GetImageSizeAndCount`
- `WanVideoEncode`
- `WanVideoControlEmbeds`
- `WanVideoImageToVideoEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `VHS_LoadVideo`
- `LoadImage`
- `CR Prompt Text`
- `easy seed`
- `INTConstant`
- `WanVideoSigmaToStep`
- `Float`
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoScheduler`
- `StringToFloatList`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `StringToFloatList`

## 知识

覆盖率 **94%**（47/50）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoDecode`、`VHS_VideoCombine`、`SaveLatent`、`VAELoader`、`VAEEncode`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSampler`、`SaveImage`、`WanVideoContextOptions`、`GetImageSizeAndCount`、`WanVideoEncode`、`WanVideoControlEmbeds`、`WanVideoImageToVideoEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`VHS_LoadVideo`、`LoadImage`、`CR Prompt Text`、`easy seed`、`INTConstant`、`WanVideoSigmaToStep`、`Float`、`WanVideoScheduler`、`StringToFloatList`

**用到的条目**：VAELoader、LoadImage、WanVideoSampler、easy seed、SaveLatent、VAEEncode、LoadWanVideoT5TextEncoder、WanVideoDecode
