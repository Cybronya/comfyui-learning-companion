---
key: 视频生成/文生视频/Wan2.2文生视频性价比极致加速V5+lynx_1978411441667592194.json
name: Wan2.2文生视频性价比极致加速V5+lynx_1978411441667592194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频性价比极致加速V5+lynx_1978411441667592194.json
hash: 753e53b91f898746
coverage: 0.859649
learned_at: 2026-10-15 22:47:16
nodes: [WanVideoTextEncodeCached, LynxEncodeFaceIP, RH_Captioner, LoadLynxResampler, LynxInsightFaceCrop, WanVideoVACEModelSelect, WanVideoExtraModelSelect, LoadImage, String Literal, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetRadialAttention, WanVideoSetRadialAttention, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, WanVideoEmptyEmbeds, WanVideoScheduler, PrimitiveNode, PrimitiveNode, easy seed, WanVideoScheduler, easy globalSeed, easy int, easy int, easy int, VHS_VideoCombine, Note, PrimitiveNode, easy float, easy float, WanVideoVACEEncode, WanVideoSigmaToStep, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVACEEncode, WanVideoExtraModelSelect, easy float, WanVideoAddLynxEmbeds, WanVideoVACEModelSelect, String Literal, WanVideoLoraSelect, WanVideoModelLoader]
patterns: []
missing: []
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

覆盖率 **86%**（49/57）

**有卡**：`WanVideoTextEncodeCached`、`LynxEncodeFaceIP`、`RH_Captioner`、`LoadLynxResampler`、`LynxInsightFaceCrop`、`WanVideoVACEModelSelect`、`WanVideoExtraModelSelect`、`LoadImage`、`String Literal`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoSetRadialAttention`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`WanVideoScheduler`、`easy seed`、`easy globalSeed`、`easy int`、`VHS_VideoCombine`、`easy float`、`WanVideoVACEEncode`、`WanVideoSigmaToStep`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoAddLynxEmbeds`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
