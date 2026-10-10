---
key: 视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（KJ版）_1975846186269675522.json
name: （自用）Dyno+Remix 1.0新模型文生视频（KJ版）_1975846186269675522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（KJ版）_1975846186269675522.json
hash: f21bc678658a896f
coverage: 0.888889
learned_at: 2026-10-10 23:14:30
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoEmptyEmbeds, WanVideoSetLoRAs, WanVideoSampler, WanVideoSampler, Seed (rgthree), INTConstant, INTConstant, CreateCFGScheduleFloatList, PrimitiveFloat, TT_img_enc, SaveImage, WanVideoDecode, FastUnsharpSharpen, JWInteger, JWInteger, JWInteger, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncodeCached, CR Prompt Text, LoadImage, SaveImage]
patterns: []
missing: [CR Prompt Text, Seed (rgthree)]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（KJ版）_1975846186269675522.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（KJ版）_1975846186269675522.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（27 个）：
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoEmptyEmbeds`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Seed (rgthree)`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `PrimitiveFloat`
- `TT_img_enc`
- `SaveImage`
- `WanVideoDecode`
- `FastUnsharpSharpen`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `CR Prompt Text`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`INTConstant`、`CreateCFGScheduleFloatList`、`TT_img_enc`、`SaveImage`、`WanVideoDecode`、`FastUnsharpSharpen`、`JWInteger`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`LoadImage`

**缺卡**（2）：`CR Prompt Text`、`Seed (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoSetLoRAs、SaveImage

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
