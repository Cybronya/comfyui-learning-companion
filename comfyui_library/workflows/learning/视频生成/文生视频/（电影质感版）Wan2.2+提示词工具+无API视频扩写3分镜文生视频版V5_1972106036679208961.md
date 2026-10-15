---
key: 视频生成/文生视频/（电影质感版）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V5_1972106036679208961.json
name: （电影质感版）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V5_1972106036679208961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（电影质感版）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V5_1972106036679208961.json
hash: 5761c3ca58d38bc4
coverage: 0.795918
learned_at: 2026-10-15 22:49:11
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, INTConstant, INTConstant, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoTextEncode, Note, CR Prompt Text, easy showAnything, TextConcat, easy showAnything, ShowText|pysssss, JWStringConcat, easy showAnything, JWInteger, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, JWInteger, JWInteger, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoSampler, WanVideoVAELoader, GetImageSizeAndCount, VHS_VideoCombine, CR Prompt Text, Note, Wan22PromptSelector, CR Prompt Text, RH_LLMAPI_NODE, PrimitiveNode, WanVideoModelLoader, WanVideoModelLoader, VHS_VideoCombine, VHS_VideoCombine, ImageFromBatch+, WanVideoDecode]
patterns: []
missing: []
---

# 视频生成/文生视频/（电影质感版）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V5_1972106036679208961.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（电影质感版）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V5_1972106036679208961.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（49 个）：
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `Note`
- `CR Prompt Text`
- `easy showAnything`
- `TextConcat`
- `easy showAnything`
- `ShowText|pysssss`
- `JWStringConcat`
- `easy showAnything`
- `JWInteger`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `Note`
- `Wan22PromptSelector`
- `CR Prompt Text`
- `RH_LLMAPI_NODE`
- `PrimitiveNode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `WanVideoDecode`

## 知识

覆盖率 **80%**（39/49）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`CR Prompt Text`、`TextConcat`、`JWStringConcat`、`JWInteger`、`WanVideoSetLoRAs`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`Wan22PromptSelector`、`RH_LLMAPI_NODE`、`WanVideoModelLoader`、`ImageFromBatch+`、`WanVideoDecode`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
