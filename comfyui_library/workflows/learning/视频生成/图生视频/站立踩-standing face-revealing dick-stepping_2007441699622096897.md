---
key: 视频生成/图生视频/站立踩-standing face-revealing dick-stepping_2007441699622096897.json
name: 站立踩-standing face-revealing dick-stepping_2007441699622096897.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/站立踩-standing face-revealing dick-stepping_2007441699622096897.json
hash: d321c080e624174b
coverage: 0.97561
learned_at: 2026-10-15 22:34:03
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, easy cleanGpuUsed, WanVideoDecode, LayerUtility: PurgeVRAM, ShowText|pysssss, TextInput_, TextCombinerTwo, ImageResizeKJ, WanVideoSampler, TextCombinerTwo, TextInput_, WanVideoLoraSelect, WanVideoSampler, WanVideoScheduler, WanVideoScheduler, INTConstant, WanVideoSigmaToStep, FloatConstant, CreateCFGScheduleFloatList, WanVideoImageToVideoEncode, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, Text Random Line, TextInput_, TextInput_, LoadImage, GetImageSizeAndCount, TT_img_enc, SaveImage]
patterns: []
missing: []
---

# 视频生成/图生视频/站立踩-standing face-revealing dick-stepping_2007441699622096897.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2007441699622096897.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `ShowText|pysssss`
- `TextInput_`
- `TextCombinerTwo`
- `ImageResizeKJ`
- `WanVideoSampler` ★核心
- `TextCombinerTwo`
- `TextInput_`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoScheduler`
- `INTConstant`
- `WanVideoSigmaToStep`
- `FloatConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Text Random Line`
- `TextInput_`
- `TextInput_`
- `LoadImage`
- `GetImageSizeAndCount`
- `TT_img_enc`
- `SaveImage`

## 知识

覆盖率 **98%**（40/41）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`easy cleanGpuUsed`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`TextInput_`、`TextCombinerTwo`、`ImageResizeKJ`、`WanVideoSampler`、`WanVideoLoraSelect`、`WanVideoScheduler`、`INTConstant`、`WanVideoSigmaToStep`、`FloatConstant`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`Text Random Line`、`LoadImage`、`GetImageSizeAndCount`、`TT_img_enc`、`SaveImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
