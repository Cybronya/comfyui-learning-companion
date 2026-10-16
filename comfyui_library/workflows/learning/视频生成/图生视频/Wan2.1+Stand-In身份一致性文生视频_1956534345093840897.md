---
key: 视频生成/图生视频/Wan2.1+Stand-In身份一致性文生视频_1956534345093840897.json
name: Wan2.1+Stand-In身份一致性文生视频_1956534345093840897.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956534345093840897.json
hash: 9e62fc4fb997c95c
coverage: 0.764706
learned_at: 2026-10-15 22:31:14
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoBlockSwap, WanVideoEmptyEmbeds, easy imageScaleDownToSize, Text Concatenate, WanVideoSampler, WanVideoTextEncode, ApplyFaceProcessor, PreviewImage, WanVideoAddStandInLatent, FaceProcessorLoader, MathExpression|pysssss, ShowText|pysssss, ImpactSwitch, Wan22PromptSelector, WanVideoEncode, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, PrimitiveInt, LoadImage, Reroute, WanVideoDecode, VHS_VideoCombine, ImageConcanate, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, RH_LLMAPI_NODE]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1+Stand-In身份一致性文生视频_1956534345093840897.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956534345093840897.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（34 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoEmptyEmbeds`
- `easy imageScaleDownToSize`
- `Text Concatenate`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `ApplyFaceProcessor`
- `PreviewImage`
- `WanVideoAddStandInLatent`
- `FaceProcessorLoader`
- `MathExpression|pysssss`
- `ShowText|pysssss`
- `ImpactSwitch`
- `Wan22PromptSelector`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `LoadImage`
- `Reroute`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageConcanate`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`

## 知识

覆盖率 **76%**（26/34）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoEmptyEmbeds`、`easy imageScaleDownToSize`、`Text Concatenate`、`WanVideoSampler`、`WanVideoTextEncode`、`ApplyFaceProcessor`、`WanVideoAddStandInLatent`、`FaceProcessorLoader`、`MathExpression|pysssss`、`Wan22PromptSelector`、`WanVideoEncode`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`LoadImage`、`WanVideoDecode`、`ImageConcanate`、`RH_LLMAPI_NODE`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoAddStandInLatent、WanVideoEncode
