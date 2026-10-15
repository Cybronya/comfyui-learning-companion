---
key: 视频生成/文生视频/Smooth Mix 2.0 VS LightX2V T2V_2073238743884062721.json
name: Smooth Mix 2.0 VS LightX2V T2V_2073238743884062721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth Mix 2.0 VS LightX2V T2V_2073238743884062721.json
hash: 67d10a6dae383965
coverage: 0.957447
learned_at: 2026-10-15 22:47:00
nodes: [CreateCFGScheduleFloatList, WanVideoSampler, INTConstant, WanVideoScheduler, WanVideoBlockSwap, LayerUtility: PurgeVRAM, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, WanVideoVAELoader, CLIPLoader, Note, WanVideoDecode, VHS_VideoCombine, CR Prompt Text, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, UNETLoader, UNETLoader, KSamplerAdvanced, WanVideoSampler, CLIPTextEncode, CLIPTextEncode, VAELoader, JWInteger, JWInteger, JWInteger, WanImageToVideo, WanVideoEmptyEmbeds, PrimitiveNode, WanVideoScheduler, Float, WanVideoSigmaToStep]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/Smooth Mix 2.0 VS LightX2V T2V_2073238743884062721.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Smooth Mix 2.0 VS LightX2V T2V_2073238743884062721.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（47 个）：
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoScheduler`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `WanVideoVAELoader`
- `CLIPLoader`
- `Note`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `WanVideoSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `WanImageToVideo`
- `WanVideoEmptyEmbeds`
- `PrimitiveNode`
- `WanVideoScheduler`
- `Float`
- `WanVideoSigmaToStep`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（45/47）

**有卡**：`CreateCFGScheduleFloatList`、`WanVideoSampler`、`INTConstant`、`WanVideoScheduler`、`WanVideoBlockSwap`、`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAEDecode`、`WanVideoVAELoader`、`CLIPLoader`、`WanVideoDecode`、`CR Prompt Text`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoTextEncode`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`JWInteger`、`WanImageToVideo`、`WanVideoEmptyEmbeds`、`Float`、`WanVideoSigmaToStep`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、WanVideoSampler、CreateCFGScheduleFloatList
