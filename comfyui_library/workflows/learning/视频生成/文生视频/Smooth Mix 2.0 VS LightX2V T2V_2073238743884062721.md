---
key: 视频生成/文生视频/Smooth Mix 2.0 VS LightX2V T2V_2073238743884062721.json
name: Smooth Mix 2.0 VS LightX2V T2V_2073238743884062721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth Mix 2.0 VS LightX2V T2V_2073238743884062721.json
hash: 67d10a6dae383965
coverage: 0.893617
learned_at: 2026-10-11 20:38:42
nodes: [CreateCFGScheduleFloatList, WanVideoSampler, INTConstant, WanVideoScheduler, WanVideoBlockSwap, LayerUtility: PurgeVRAM, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, WanVideoVAELoader, CLIPLoader, Note, WanVideoDecode, VHS_VideoCombine, CR Prompt Text, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, UNETLoader, UNETLoader, KSamplerAdvanced, WanVideoSampler, CLIPTextEncode, CLIPTextEncode, VAELoader, JWInteger, JWInteger, JWInteger, WanImageToVideo, WanVideoEmptyEmbeds, PrimitiveNode, WanVideoScheduler, Float, WanVideoSigmaToStep]
patterns: []
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CR Prompt Text]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
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

覆盖率 **89%**（42/47）

**有卡**：`CreateCFGScheduleFloatList`、`WanVideoSampler`、`INTConstant`、`WanVideoScheduler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAEDecode`、`WanVideoVAELoader`、`CLIPLoader`、`WanVideoDecode`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoTextEncode`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`JWInteger`、`WanImageToVideo`、`WanVideoEmptyEmbeds`、`Float`、`WanVideoSigmaToStep`

**缺卡**（3）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、WanVideoSampler、CreateCFGScheduleFloatList

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
