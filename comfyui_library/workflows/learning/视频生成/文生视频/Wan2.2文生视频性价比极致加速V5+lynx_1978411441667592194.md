---
key: 视频生成/文生视频/Wan2.2文生视频性价比极致加速V5+lynx_1978411441667592194.json
name: Wan2.2文生视频性价比极致加速V5+lynx_1978411441667592194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速V5+lynx_1978411441667592194.json
hash: 753e53b91f898746
coverage: 0.684211
learned_at: 2026-10-10 23:08:02
nodes: [WanVideoTextEncodeCached, LynxEncodeFaceIP, RH_Captioner, LoadLynxResampler, LynxInsightFaceCrop, WanVideoVACEModelSelect, WanVideoExtraModelSelect, LoadImage, String Literal, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetRadialAttention, WanVideoSetRadialAttention, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, WanVideoEmptyEmbeds, WanVideoScheduler, PrimitiveNode, PrimitiveNode, easy seed, WanVideoScheduler, easy globalSeed, easy int, easy int, easy int, VHS_VideoCombine, Note, PrimitiveNode, easy float, easy float, WanVideoVACEEncode, WanVideoSigmaToStep, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVACEEncode, WanVideoExtraModelSelect, easy float, WanVideoAddLynxEmbeds, WanVideoVACEModelSelect, String Literal, WanVideoLoraSelect, WanVideoModelLoader]
patterns: []
missing: [String Literal, String Literal, easy float, easy float, easy float, easy int, easy int, easy int, easy globalSeed, easy seed]
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2文生视频性价比极致加速V5+lynx_1978411441667592194.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速V5+lynx_1978411441667592194.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（57 个）：
- `WanVideoTextEncodeCached`
- `LynxEncodeFaceIP`
- `RH_Captioner`
- `LoadLynxResampler` ★核心
- `LynxInsightFaceCrop`
- `WanVideoVACEModelSelect`
- `WanVideoExtraModelSelect`
- `LoadImage`
- `String Literal`
- `SetNode`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSetRadialAttention`
- `WanVideoSetRadialAttention`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoEmptyEmbeds`
- `WanVideoScheduler`
- `PrimitiveNode`
- `PrimitiveNode`
- `easy seed`
- `WanVideoScheduler`
- `easy globalSeed`
- `easy int`
- `easy int`
- `easy int`
- `VHS_VideoCombine`
- `Note`
- `PrimitiveNode`
- `easy float`
- `easy float`
- `WanVideoVACEEncode`
- `WanVideoSigmaToStep`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVACEEncode`
- `WanVideoExtraModelSelect`
- `easy float`
- `WanVideoAddLynxEmbeds`
- `WanVideoVACEModelSelect`
- `String Literal`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`

## 知识

覆盖率 **68%**（39/57）

**有卡**：`WanVideoTextEncodeCached`、`LynxEncodeFaceIP`、`RH_Captioner`、`LoadLynxResampler`、`LynxInsightFaceCrop`、`WanVideoVACEModelSelect`、`WanVideoExtraModelSelect`、`LoadImage`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoSetRadialAttention`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`WanVideoScheduler`、`VHS_VideoCombine`、`WanVideoVACEEncode`、`WanVideoSigmaToStep`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoAddLynxEmbeds`

**缺卡**（10）：`String Literal`、`String Literal`、`easy float`、`easy float`、`easy float`、`easy int`、`easy int`、`easy int`、`easy globalSeed`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
