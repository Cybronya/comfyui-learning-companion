---
key: 视频生成/文生视频/（灰度本地N版）Wan2.2 Smooth Mix V2高低噪模型高动态文生视频V1（KJ版）_1979878092309172225.json
name: （灰度本地N版）Wan2.2 Smooth Mix V2高低噪模型高动态文生视频V1（KJ版）_1979878092309172225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（灰度本地N版）Wan2.2 Smooth Mix V2高低噪模型高动态文生视频V1（KJ版）_1979878092309172225.json
hash: 1519ba8a004a7ea9
coverage: 0.820513
learned_at: 2026-10-11 02:45:05
nodes: [WanVideoSetBlockSwap, Note, Note, Note, WanVideoTorchCompileSettings, JWInteger, JWInteger, JWInteger, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoVAELoader, Note, WanVideoDecode, WanVideoSampler, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoBlockSwap, PrimitiveNode, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoTextEncode, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, INTConstant, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, CR Prompt Text, SaveImage, TT_img_enc_v2, SaveImage, TT_img_enc, GetImageSizeAndCount, CR Prompt Text]
patterns: []
missing: [CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（灰度本地N版）Wan2.2 Smooth Mix V2高低噪模型高动态文生视频V1（KJ版）_1979878092309172225.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（灰度本地N版）Wan2.2 Smooth Mix V2高低噪模型高动态文生视频V1（KJ版）_1979878092309172225.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `WanVideoSetBlockSwap`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `Note`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `PrimitiveNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `INTConstant`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `CR Prompt Text`
- `SaveImage`
- `TT_img_enc_v2`
- `SaveImage`
- `TT_img_enc`
- `GetImageSizeAndCount`
- `CR Prompt Text`

## 知识

覆盖率 **82%**（32/39）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`JWInteger`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`INTConstant`、`WanVideoModelLoader`、`SaveImage`、`TT_img_enc_v2`、`TT_img_enc`、`GetImageSizeAndCount`

**缺卡**（2）：`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
