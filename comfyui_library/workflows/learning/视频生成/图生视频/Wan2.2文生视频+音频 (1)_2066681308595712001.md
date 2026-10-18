---
key: 视频生成/图生视频/Wan2.2文生视频+音频 (1)_2066681308595712001.json
name: Wan2.2文生视频+音频 (1)_2066681308595712001.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2文生视频+音频 (1)_2066681308595712001.json
hash: 07e5ce2791e075e0
coverage: 0.844444
learned_at: 2026-10-15 22:39:51
nodes: [VHS_VideoCombine, Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoSampler, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoBlockSwap, CreateCFGScheduleFloatList, PrimitiveNode, INTConstant, Float, WanVideoSampler, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, JWInteger, JWInteger, WanVideoEmptyEmbeds, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, easy showAnything, VAELoader, SaveLatent, VAEEncode, GetImageSizeAndCount, WanVideoLoraSelect, text_mul_replace, HunyuanVideoFoley, VHS_VideoCombine, VHS_VideoCombine, JWInteger, WanVideoTextEncode, WanVideoModelLoader, WanVideoModelLoader, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2文生视频+音频 (1)_2066681308595712001.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066681308595712001.json`

## 结构

**生成流程**：Model → Encode → Sampling → Process → Output → Other

**节点**（45 个）：
- `VHS_VideoCombine`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `INTConstant`
- `Float`
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `easy showAnything`
- `VAELoader`
- `SaveLatent`
- `VAEEncode` ★核心
- `GetImageSizeAndCount`
- `WanVideoLoraSelect`
- `text_mul_replace`
- `HunyuanVideoFoley`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `CR Prompt Text`

## 知识

覆盖率 **84%**（38/45）

**有卡**：`VHS_VideoCombine`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`INTConstant`、`Float`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`JWInteger`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`VAELoader`、`SaveLatent`、`VAEEncode`、`GetImageSizeAndCount`、`text_mul_replace`、`HunyuanVideoFoley`、`WanVideoTextEncode`、`WanVideoModelLoader`、`CR Prompt Text`

**用到的条目**：VAELoader、WanVideoSampler、CreateCFGScheduleFloatList、SaveLatent、VAEEncode、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
