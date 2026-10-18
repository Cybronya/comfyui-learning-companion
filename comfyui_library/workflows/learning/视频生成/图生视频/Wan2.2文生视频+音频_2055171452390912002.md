---
key: 视频生成/图生视频/Wan2.2文生视频+音频_2055171452390912002.json
name: Wan2.2文生视频+音频_2055171452390912002.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2文生视频+音频_2055171452390912002.json
hash: 7df938ed122ed721
coverage: 0.844444
learned_at: 2026-10-15 22:37:55
nodes: [VHS_VideoCombine, Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, WanVideoSampler, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncode, WanVideoLoraSelect, WanVideoBlockSwap, CreateCFGScheduleFloatList, PrimitiveNode, INTConstant, Float, WanVideoSampler, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, JWInteger, JWInteger, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, easy showAnything, VAELoader, SaveLatent, VAEEncode, GetImageSizeAndCount, WanVideoLoraSelect, text_mul_replace, HunyuanVideoFoley, VHS_VideoCombine, VHS_VideoCombine, JWInteger, CR Prompt Text, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2文生视频+音频_2055171452390912002.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055171452390912002.json`

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
- `WanVideoSampler` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
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
- `CR Prompt Text`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEmptyEmbeds`

## 知识

覆盖率 **84%**（38/45）

**有卡**：`VHS_VideoCombine`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`INTConstant`、`Float`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`JWInteger`、`WanVideoVAELoader`、`VAELoader`、`SaveLatent`、`VAEEncode`、`GetImageSizeAndCount`、`text_mul_replace`、`HunyuanVideoFoley`、`CR Prompt Text`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`

**用到的条目**：VAELoader、WanVideoSampler、CreateCFGScheduleFloatList、SaveLatent、VAEEncode、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
