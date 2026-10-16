---
key: 视频生成/图生视频/Wan2.1+Stand-In+MultiTalk 人脸一致性文生数字人_1956219463043612673.json
name: Wan2.1+Stand-In+MultiTalk 人脸一致性文生数字人_1956219463043612673.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956219463043612673.json
hash: 3e32130ef9040cb4
coverage: 0.82
learned_at: 2026-10-15 22:31:12
nodes: [Wan22PromptSelector, ImpactSwitch, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, GetNode, FaceProcessorLoader, JWInteger, Text Concatenate, GetNode, ApplyFaceProcessor, easy imageScaleDownToSize, RH_LLMAPI_NODE, AudioCrop, AudioSeparation, JWInteger, WanVideoDecode, ImageConcatMulti, JWInteger, JWInteger, WanVideoEmptyEmbeds, CR Text, LoadAudio, MultiTalkModelLoader, SetNode, SetNode, WanVideoVAELoader, easy showAnything, VHS_VideoCombine, WanVideoModelLoader, WanVideoTextEncode, GetNode, WanVideoSampler, WanVideoAddStandInLatent, WanVideoEncode, Audio Duration (mtb), RHHiddenNodes, VHS_VideoCombine, DownloadAndLoadWav2VecModel, easy cleanGpuUsed, MultiTalkWav2VecEmbeds, MathExpression|pysssss, ImageFromBatch+, PreviewImage, LoadImage, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1+Stand-In+MultiTalk 人脸一致性文生数字人_1956219463043612673.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956219463043612673.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（50 个）：
- `Wan22PromptSelector`
- `ImpactSwitch`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `FaceProcessorLoader`
- `JWInteger`
- `Text Concatenate`
- `GetNode`
- `ApplyFaceProcessor`
- `easy imageScaleDownToSize`
- `RH_LLMAPI_NODE`
- `AudioCrop`
- `AudioSeparation`
- `JWInteger`
- `WanVideoDecode`
- `ImageConcatMulti`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `CR Text`
- `LoadAudio`
- `MultiTalkModelLoader`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `easy showAnything`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoAddStandInLatent`
- `WanVideoEncode`
- `Audio Duration (mtb)`
- `RHHiddenNodes`
- `VHS_VideoCombine`
- `DownloadAndLoadWav2VecModel`
- `easy cleanGpuUsed`
- `MultiTalkWav2VecEmbeds`
- `MathExpression|pysssss`
- `ImageFromBatch+`
- `PreviewImage`
- `LoadImage`
- `WanVideoLoraSelect`

## 知识

覆盖率 **82%**（41/50）

**有卡**：`Wan22PromptSelector`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`FaceProcessorLoader`、`JWInteger`、`Text Concatenate`、`ApplyFaceProcessor`、`easy imageScaleDownToSize`、`RH_LLMAPI_NODE`、`AudioCrop`、`AudioSeparation`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoEmptyEmbeds`、`CR Text`、`LoadAudio`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoAddStandInLatent`、`WanVideoEncode`、`Audio Duration (mtb)`、`RHHiddenNodes`、`DownloadAndLoadWav2VecModel`、`easy cleanGpuUsed`、`MultiTalkWav2VecEmbeds`、`MathExpression|pysssss`、`ImageFromBatch+`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoAddStandInLatent、WanVideoEncode
