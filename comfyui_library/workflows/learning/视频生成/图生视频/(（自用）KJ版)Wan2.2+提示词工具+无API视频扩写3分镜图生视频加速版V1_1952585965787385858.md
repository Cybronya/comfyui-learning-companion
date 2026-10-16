---
key: 视频生成/图生视频/(（自用）KJ版)Wan2.2+提示词工具+无API视频扩写3分镜图生视频加速版V1_1952585965787385858.json
name: (（自用）KJ版)Wan2.2+提示词工具+无API视频扩写3分镜图生视频加速版V1_1952585965787385858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952585965787385858.json
hash: 15fe886abbe86ea5
coverage: 0.788462
learned_at: 2026-10-15 22:31:02
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, Note, Note, WanVideoModelLoader, WanVideoModelLoader, Note, JWInteger, WanVideoImageToVideoEncode, WanVideoVAELoader, WanVideoTextEncode, CR Prompt Text, Note, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, Note, WanVideoSampler, ShowText|pysssss, TextConcat, CR Prompt Text, easy showAnything, easy showAnything, JWStringConcat, WanVideoTorchCompileSettings, CR Prompt Text, Wan22PromptSelector, easy showAnything, RH_Captioner, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, JWInteger, RH_LLMAPI_NODE, CreateCFGScheduleFloatList, INTConstant, PrimitiveNode, WanVideoVAELoader, LoadLatent, VHS_VideoCombine, WanVideoDecode, SaveLatent, WanVideoSampler, LoadImage, SaveImage, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/(（自用）KJ版)Wan2.2+提示词工具+无API视频扩写3分镜图生视频加速版V1_1952585965787385858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952585965787385858.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（52 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Note`
- `JWInteger`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `CR Prompt Text`
- `Note`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `Note`
- `WanVideoSampler` ★核心
- `ShowText|pysssss`
- `TextConcat`
- `CR Prompt Text`
- `easy showAnything`
- `easy showAnything`
- `JWStringConcat`
- `WanVideoTorchCompileSettings`
- `CR Prompt Text`
- `Wan22PromptSelector`
- `easy showAnything`
- `RH_Captioner`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `JWInteger`
- `RH_LLMAPI_NODE`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `LoadLatent`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `SaveLatent`
- `WanVideoSampler` ★核心
- `LoadImage`
- `SaveImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `Note`

## 知识

覆盖率 **79%**（41/52）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`JWInteger`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`CR Prompt Text`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`TextConcat`、`JWStringConcat`、`WanVideoTorchCompileSettings`、`Wan22PromptSelector`、`RH_Captioner`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`RH_LLMAPI_NODE`、`CreateCFGScheduleFloatList`、`LoadLatent`、`VHS_VideoCombine`、`WanVideoDecode`、`SaveLatent`、`LoadImage`、`SaveImage`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、SaveLatent、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
