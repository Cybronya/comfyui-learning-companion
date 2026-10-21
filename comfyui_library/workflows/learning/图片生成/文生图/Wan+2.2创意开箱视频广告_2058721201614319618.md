---
key: 图片生成/文生图/Wan+2.2创意开箱视频广告_2058721201614319618.json
name: Wan+2.2创意开箱视频广告_2058721201614319618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan+2.2创意开箱视频广告_2058721201614319618.json
hash: 40d139ee1be44530
coverage: 0.72
learned_at: 2026-10-19 23:02:49
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoModelLoader, CreateCFGScheduleFloatList, easy cleanGpuUsed, DownloadAndLoadGIMMVFIModel, WanVideoDecode, GIMMVFI_interpolate, VHS_VideoCombine, MathExpression|pysssss, JjkText, WanVideoVAELoader, WanVideoSampler, WanVideoSampler, ImageFromBatch+, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoLoraSelect, Int, Int, Int, Int, Int, easy seed, WanVideoEmptyEmbeds, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoLoraSelect, JjkText, JsonToText, JjkText, JjkText, easy showAnything, Note, Note, Reroute, easy anythingIndexSwitch, Note, Wan22PromptSelector, Note, JWStringConcat, Note, RH_LLMAPI_NODE, easy anythingIndexSwitch, JjkText, Note, JjkText]
patterns: []
missing: []
---

# 图片生成/文生图/Wan+2.2创意开箱视频广告_2058721201614319618.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan+2.2创意开箱视频广告_2058721201614319618.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（50 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `easy cleanGpuUsed`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoDecode`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `JjkText`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `ImageFromBatch+`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `easy seed`
- `WanVideoEmptyEmbeds`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `JjkText`
- `JsonToText`
- `JjkText`
- `JjkText`
- `easy showAnything`
- `Note`
- `Note`
- `Reroute`
- `easy anythingIndexSwitch`
- `Note`
- `Wan22PromptSelector`
- `Note`
- `JWStringConcat`
- `Note`
- `RH_LLMAPI_NODE`
- `easy anythingIndexSwitch`
- `JjkText`
- `Note`
- `JjkText`

## 知识

覆盖率 **72%**（36/50）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`easy cleanGpuUsed`、`DownloadAndLoadGIMMVFIModel`、`WanVideoDecode`、`GIMMVFI_interpolate`、`VHS_VideoCombine`、`MathExpression|pysssss`、`WanVideoVAELoader`、`WanVideoSampler`、`ImageFromBatch+`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`Int`、`easy seed`、`WanVideoEmptyEmbeds`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`JsonToText`、`easy anythingIndexSwitch`、`Wan22PromptSelector`、`JWStringConcat`、`RH_LLMAPI_NODE`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
