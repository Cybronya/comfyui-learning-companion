---
key: 视频生成/文生视频/Wan+2.2+文本到视频广告_1951940652722540546.json
name: Wan+2.2+文本到视频广告_1951940652722540546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan+2.2+文本到视频广告_1951940652722540546.json
hash: 367168696868f39d
coverage: 0.6
learned_at: 2026-10-10 23:06:21
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoModelLoader, CreateCFGScheduleFloatList, easy cleanGpuUsed, DownloadAndLoadGIMMVFIModel, WanVideoDecode, GIMMVFI_interpolate, VHS_VideoCombine, MathExpression|pysssss, JjkText, WanVideoVAELoader, WanVideoSampler, WanVideoSampler, ImageFromBatch+, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoLoraSelect, Int, Int, Int, Int, Int, easy seed, WanVideoEmptyEmbeds, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoLoraSelect, JsonToText, JjkText, JjkText, easy showAnything, Note, Note, Reroute, easy anythingIndexSwitch, Note, Wan22PromptSelector, Note, JWStringConcat, Note, RH_LLMAPI_NODE, easy anythingIndexSwitch, Note, JjkText, JjkText, JjkText]
patterns: []
missing: [ImageFromBatch+, MathExpression|pysssss, easy anythingIndexSwitch, easy anythingIndexSwitch, easy cleanGpuUsed, easy seed]
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan+2.2+文本到视频广告_1951940652722540546.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan+2.2+文本到视频广告_1951940652722540546.json`

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
- `Note`
- `JjkText`
- `JjkText`
- `JjkText`

## 知识

覆盖率 **60%**（30/50）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`DownloadAndLoadGIMMVFIModel`、`WanVideoDecode`、`GIMMVFI_interpolate`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`Int`、`WanVideoEmptyEmbeds`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`JsonToText`、`Wan22PromptSelector`、`JWStringConcat`、`RH_LLMAPI_NODE`

**缺卡**（6）：`ImageFromBatch+`、`MathExpression|pysssss`、`easy anythingIndexSwitch`、`easy anythingIndexSwitch`、`easy cleanGpuUsed`、`easy seed`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
