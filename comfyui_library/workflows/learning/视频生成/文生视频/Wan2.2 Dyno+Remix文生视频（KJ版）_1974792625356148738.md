---
key: 视频生成/文生视频/Wan2.2 Dyno+Remix文生视频（KJ版）_1974792625356148738.json
name: Wan2.2 Dyno+Remix文生视频（KJ版）_1974792625356148738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Dyno+Remix文生视频（KJ版）_1974792625356148738.json
hash: 973d076a887cdec4
coverage: 0.892857
learned_at: 2026-10-10 23:06:49
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoEmptyEmbeds, WanVideoSampler, INTConstant, INTConstant, CreateCFGScheduleFloatList, PrimitiveFloat, SaveImage, WanVideoDecode, FastUnsharpSharpen, JWInteger, JWInteger, JWInteger, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, VHS_VideoCombine, TT_img_enc, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSampler, Seed (rgthree), WanVideoTextEncodeCached, CR Prompt Text, WanVideoModelLoader, WanVideoLoraSelect]
patterns: []
missing: [CR Prompt Text, Seed (rgthree)]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2 Dyno+Remix文生视频（KJ版）_1974792625356148738.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Dyno+Remix文生视频（KJ版）_1974792625356148738.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（28 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `PrimitiveFloat`
- `SaveImage`
- `WanVideoDecode`
- `FastUnsharpSharpen`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`
- `TT_img_enc`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `Seed (rgthree)`
- `WanVideoTextEncodeCached`
- `CR Prompt Text`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`INTConstant`、`CreateCFGScheduleFloatList`、`SaveImage`、`WanVideoDecode`、`FastUnsharpSharpen`、`JWInteger`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`TT_img_enc`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoTextEncodeCached`、`WanVideoLoraSelect`

**缺卡**（2）：`CR Prompt Text`、`Seed (rgthree)`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs、SaveImage

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
