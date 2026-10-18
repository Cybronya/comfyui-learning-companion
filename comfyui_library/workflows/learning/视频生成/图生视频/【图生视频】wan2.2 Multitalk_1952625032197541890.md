---
key: 视频生成/图生视频/【图生视频】wan2.2 Multitalk_1952625032197541890.json
name: 【图生视频】wan2.2 Multitalk_1952625032197541890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【图生视频】wan2.2 Multitalk_1952625032197541890.json
hash: a84666fde7786c3a
coverage: 0.866667
learned_at: 2026-10-15 22:31:03
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, RH_GetAudioDuration, WanVideoSetLoRAs, WanVideoSetLoRAs, Int, INTConstant, WanVideoSampler, WanVideoModelLoader, WanVideoSampler, VHS_VideoCombine, Float to Int, ImageResizeKJv2, MultiTalkWav2VecEmbeds, INTConstant, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTorchCompileSettings, MultiTalkModelLoader, WanVideoBlockSwap, WanVideoVAELoader, WanVideoImageToVideoEncode, CreateCFGScheduleFloatList, WanVideoDecode, GetImageSizeAndCount, DownloadAndLoadWav2VecModel, LoadImage, WanVideoTextEncode, easy showAnything, TextBox, Note, easy ifElse, PrimitiveBoolean, RH_Captioner, TextBox, TextBox, CR Text Replace, easy showAnything, Reroute, LoadImage, Note, WanVideoModelLoader, LoadAudio, SimpleMath+]
patterns: []
missing: []
---

# 视频生成/图生视频/【图生视频】wan2.2 Multitalk_1952625032197541890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952625032197541890.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `RH_GetAudioDuration`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `Int`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `Float to Int`
- `ImageResizeKJv2`
- `MultiTalkWav2VecEmbeds`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `MultiTalkModelLoader`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `DownloadAndLoadWav2VecModel`
- `LoadImage`
- `WanVideoTextEncode`
- `easy showAnything`
- `TextBox`
- `Note`
- `easy ifElse`
- `PrimitiveBoolean`
- `RH_Captioner`
- `TextBox`
- `TextBox`
- `CR Text Replace`
- `easy showAnything`
- `Reroute`
- `LoadImage`
- `Note`
- `WanVideoModelLoader`
- `LoadAudio`
- `SimpleMath+`

## 知识

覆盖率 **87%**（39/45）

**有卡**：`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`RH_GetAudioDuration`、`WanVideoSetLoRAs`、`Int`、`INTConstant`、`WanVideoSampler`、`WanVideoModelLoader`、`VHS_VideoCombine`、`Float to Int`、`ImageResizeKJv2`、`MultiTalkWav2VecEmbeds`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`MultiTalkModelLoader`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`GetImageSizeAndCount`、`DownloadAndLoadWav2VecModel`、`LoadImage`、`WanVideoTextEncode`、`TextBox`、`PrimitiveBoolean`、`RH_Captioner`、`CR Text Replace`、`LoadAudio`、`SimpleMath+`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
