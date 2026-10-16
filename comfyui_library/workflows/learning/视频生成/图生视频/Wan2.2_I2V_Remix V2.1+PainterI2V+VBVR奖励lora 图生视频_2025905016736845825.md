---
key: 视频生成/图生视频/Wan2.2_I2V_Remix V2.1+PainterI2V+VBVR奖励lora 图生视频_2025905016736845825.json
name: Wan2.2_I2V_Remix V2.1+PainterI2V+VBVR奖励lora 图生视频_2025905016736845825.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2025905016736845825.json
hash: 7ae7de86e0d98957
coverage: 0.455882
learned_at: 2026-10-15 22:35:13
nodes: [Note, KSamplerAdvanced, Note, LayerUtility: PurgeVRAM, GetNode, GetNode, VAELoader, CLIPLoader, SetNode, GetNode, SetNode, CLIPVisionEncode, CLIPVisionLoader, SetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, GetNode, LayerUtility: PurgeVRAM, VAEDecode, GetNode, SetNode, KSamplerAdvanced, JWInteger, SetNode, Note, Note, JWInteger, easy showAnything, CR Prompt Text, AILab_QwenVL, RH_LLMAPI_Pro_Node, LoadImage, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), Note, SetNode, GetNode, GetNode, GetNode, Note, easy anythingIndexSwitch, SetNode, Note, VHS_VideoCombine, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, SetNode, ModelSamplingSD3, ModelSamplingSD3, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2_I2V_Remix V2.1+PainterI2V+VBVR奖励lora 图生视频_2025905016736845825.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2025905016736845825.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（68 个）：
- `Note`
- `KSamplerAdvanced` ★核心
- `Note`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `SetNode`
- `Note`
- `Note`
- `JWInteger`
- `easy showAnything`
- `CR Prompt Text`
- `AILab_QwenVL`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `easy anythingIndexSwitch`
- `SetNode`
- `Note`
- `VHS_VideoCombine`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CR Prompt Text`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **46%**（31/68）

**有卡**：`KSamplerAdvanced`、`LayerUtility: PurgeVRAM`、`VAELoader`、`CLIPLoader`、`CLIPVisionEncode`、`CLIPVisionLoader`、`CLIPTextEncode`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`JWInteger`、`CR Prompt Text`、`AILab_QwenVL`、`RH_LLMAPI_Pro_Node`、`LoadImage`、`easy anythingIndexSwitch`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
