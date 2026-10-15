---
key: 视频生成/文生视频/qwen3-vl反推+Wan2.2文生视频性价比极致加速V5_1981321615827001346.json
name: qwen3-vl反推+Wan2.2文生视频性价比极致加速V5_1981321615827001346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/qwen3-vl反推+Wan2.2文生视频性价比极致加速V5_1981321615827001346.json
hash: 5985858d6bee280f
coverage: 0.823529
learned_at: 2026-10-15 22:47:30
nodes: [SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetRadialAttention, WanVideoSetRadialAttention, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, WanVideoEmptyEmbeds, WanVideoScheduler, PrimitiveNode, PrimitiveNode, easy seed, WanVideoScheduler, easy globalSeed, WanVideoVACEEncode, easy int, VHS_VideoCombine, PrimitiveNode, easy float, easy float, easy float, WanVideoSigmaToStep, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoVACEEncode, easy int, easy int, WanVideoModelLoader, String Literal, LayerUtility: PurgeVRAM V2, VHS_LoadVideo, easy showAnything, AILab_QwenVL, Note]
patterns: []
missing: []
---

# 视频生成/文生视频/qwen3-vl反推+Wan2.2文生视频性价比极致加速V5_1981321615827001346.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/qwen3-vl反推+Wan2.2文生视频性价比极致加速V5_1981321615827001346.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（51 个）：
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
- `WanVideoVACEEncode`
- `easy int`
- `VHS_VideoCombine`
- `PrimitiveNode`
- `easy float`
- `easy float`
- `easy float`
- `WanVideoSigmaToStep`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEEncode`
- `easy int`
- `easy int`
- `WanVideoModelLoader`
- `String Literal`
- `LayerUtility: PurgeVRAM V2`
- `VHS_LoadVideo`
- `easy showAnything`
- `AILab_QwenVL`
- `Note`

## 知识

覆盖率 **82%**（42/51）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoSetRadialAttention`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`WanVideoScheduler`、`easy seed`、`easy globalSeed`、`WanVideoVACEEncode`、`easy int`、`VHS_VideoCombine`、`easy float`、`WanVideoSigmaToStep`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`String Literal`、`LayerUtility: PurgeVRAM V2`、`VHS_LoadVideo`、`AILab_QwenVL`

**用到的条目**：WanVideoSampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
