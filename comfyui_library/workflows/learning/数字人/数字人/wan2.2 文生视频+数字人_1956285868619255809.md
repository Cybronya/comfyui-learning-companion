---
key: 数字人/数字人/wan2.2 文生视频+数字人_1956285868619255809.json
name: wan2.2 文生视频+数字人_1956285868619255809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan2.2 文生视频+数字人_1956285868619255809.json
hash: 40dc590e2a17cba6
coverage: 0.96875
learned_at: 2026-10-26 01:59:26
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetBlockSwap, CreateCFGScheduleFloatList, WanVideoSampler, DownloadAndLoadWav2VecModel, WanVideoDecode, INTConstant, INTConstant, easy int, easy int, WanVideoBlockSwap, Note, AudioSeparation, Audio Duration (mtb), VHS_VideoCombine, FloatConstant, MathExpression|pysssss, WanVideoEmptyEmbeds, MultiTalkWav2VecEmbeds, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, MultiTalkModelLoader, LoadAudio]
patterns: []
missing: []
---

# 数字人/数字人/wan2.2 文生视频+数字人_1956285868619255809.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan2.2 文生视频+数字人_1956285868619255809.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（32 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `DownloadAndLoadWav2VecModel`
- `WanVideoDecode`
- `INTConstant`
- `INTConstant`
- `easy int`
- `easy int`
- `WanVideoBlockSwap`
- `Note`
- `AudioSeparation`
- `Audio Duration (mtb)`
- `VHS_VideoCombine`
- `FloatConstant`
- `MathExpression|pysssss`
- `WanVideoEmptyEmbeds`
- `MultiTalkWav2VecEmbeds`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `MultiTalkModelLoader`
- `LoadAudio`

## 知识

覆盖率 **97%**（31/32）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`DownloadAndLoadWav2VecModel`、`WanVideoDecode`、`INTConstant`、`easy int`、`WanVideoBlockSwap`、`AudioSeparation`、`Audio Duration (mtb)`、`VHS_VideoCombine`、`FloatConstant`、`MathExpression|pysssss`、`WanVideoEmptyEmbeds`、`MultiTalkWav2VecEmbeds`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`MultiTalkModelLoader`、`LoadAudio`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
