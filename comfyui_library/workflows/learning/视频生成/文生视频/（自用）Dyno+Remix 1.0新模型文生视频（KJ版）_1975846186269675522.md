---
key: 视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（KJ版）_1975846186269675522.json
name: （自用）Dyno+Remix 1.0新模型文生视频（KJ版）_1975846186269675522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（KJ版）_1975846186269675522.json
hash: f21bc678658a896f
coverage: 0.962963
learned_at: 2026-10-15 22:49:12
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoEmptyEmbeds, WanVideoSetLoRAs, WanVideoSampler, WanVideoSampler, Seed (rgthree), INTConstant, INTConstant, CreateCFGScheduleFloatList, PrimitiveFloat, TT_img_enc, SaveImage, WanVideoDecode, FastUnsharpSharpen, JWInteger, JWInteger, JWInteger, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncodeCached, CR Prompt Text, LoadImage, SaveImage]
patterns: []
missing: []
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

覆盖率 **96%**（26/27）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`Seed (rgthree)`、`INTConstant`、`CreateCFGScheduleFloatList`、`TT_img_enc`、`SaveImage`、`WanVideoDecode`、`FastUnsharpSharpen`、`JWInteger`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`CR Prompt Text`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed (rgthree)、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoSetLoRAs
