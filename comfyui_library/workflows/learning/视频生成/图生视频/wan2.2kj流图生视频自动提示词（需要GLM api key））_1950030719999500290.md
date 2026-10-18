---
key: 视频生成/图生视频/wan2.2kj流图生视频自动提示词（需要GLM api key））_1950030719999500290.json
name: wan2.2kj流图生视频自动提示词（需要GLM api key））_1950030719999500290.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2kj流图生视频自动提示词（需要GLM api key））_1950030719999500290.json
hash: 91b78ff76a125824
coverage: 0.945946
learned_at: 2026-10-15 22:30:51
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoModelLoader, PreviewImage, WanVideoTorchCompileSettings, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoDecode, ImageResizeKJv2, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoVAELoader, GetImageSizeAndCount, VHS_VideoCombine, INTConstant, QwenLoader, ShowText, ShowText, CR Text Concatenate, LoadImage, LoadImage, GLM_Vision_ImageToPrompt, INTConstant, WanVideoTextEncode, WanVideoPromptExtender, ShowText, Wan22PromptSelector, CR Text, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2kj流图生视频自动提示词（需要GLM api key））_1950030719999500290.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950030719999500290.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `PreviewImage`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `INTConstant`
- `QwenLoader`
- `ShowText`
- `ShowText`
- `CR Text Concatenate`
- `LoadImage`
- `LoadImage`
- `GLM_Vision_ImageToPrompt`
- `INTConstant`
- `WanVideoTextEncode`
- `WanVideoPromptExtender`
- `ShowText`
- `Wan22PromptSelector`
- `CR Text`
- `CR Text`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelect`、`WanVideoDecode`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`INTConstant`、`QwenLoader`、`ShowText`、`CR Text Concatenate`、`LoadImage`、`GLM_Vision_ImageToPrompt`、`WanVideoTextEncode`、`WanVideoPromptExtender`、`Wan22PromptSelector`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
