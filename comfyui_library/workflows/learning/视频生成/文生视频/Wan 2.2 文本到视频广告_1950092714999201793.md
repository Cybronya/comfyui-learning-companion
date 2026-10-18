---
key: 视频生成/文生视频/Wan 2.2 文本到视频广告_1950092714999201793.json
name: Wan 2.2 文本到视频广告_1950092714999201793.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2 文本到视频广告_1950092714999201793.json
hash: b70a9e41eeab12c5
coverage: 0.552239
learned_at: 2026-10-15 22:43:34
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoModelLoader, CreateCFGScheduleFloatList, easy cleanGpuUsed, WanVideoDecode, WanVideoVAELoader, WanVideoSampler, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, easy showAnything, Note, easy anythingIndexSwitch, Wan22PromptSelector, Note, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, WanVideoEmptyEmbeds, Note, LoadImage, LoadImage, JjkText, JjkText, Note, Note, easy anythingIndexSwitch, WanVideoLoraSelect, WanVideoTextEncode, WanVideoLoraSelect, MathExpression|pysssss, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JWStringConcat, RH_LLMAPI_NODE, Int, Int, Note, MathExpression|pysssss, Int, Int, easy seed, Note, VHS_VideoCombine, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageFromBatch+, Note]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan 2.2 文本到视频广告_1950092714999201793.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950092714999201793.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（67 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `easy showAnything`
- `Note`
- `easy anythingIndexSwitch`
- `Wan22PromptSelector`
- `Note`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `WanVideoEmptyEmbeds`
- `Note`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `JjkText`
- `Note`
- `Note`
- `easy anythingIndexSwitch`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `MathExpression|pysssss`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JWStringConcat`
- `RH_LLMAPI_NODE`
- `Int`
- `Int`
- `Note`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `easy seed`
- `Note`
- `VHS_VideoCombine`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageFromBatch+`
- `Note`

## 知识

覆盖率 **55%**（37/67）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`easy anythingIndexSwitch`、`Wan22PromptSelector`、`WanVideoEmptyEmbeds`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`MathExpression|pysssss`、`JWStringConcat`、`RH_LLMAPI_NODE`、`Int`、`easy seed`、`VHS_VideoCombine`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`ImageFromBatch+`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
