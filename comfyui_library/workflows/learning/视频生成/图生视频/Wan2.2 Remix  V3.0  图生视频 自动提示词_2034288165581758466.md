---
key: 视频生成/图生视频/Wan2.2 Remix  V3.0  图生视频 自动提示词_2034288165581758466.json
name: Wan2.2 Remix  V3.0  图生视频 自动提示词_2034288165581758466.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2034288165581758466.json
hash: fca9d6ab5a11ee02
coverage: 0.452055
learned_at: 2026-10-15 22:35:44
nodes: [Note, KSamplerAdvanced, Note, LayerUtility: PurgeVRAM, GetNode, GetNode, VAELoader, CLIPLoader, SetNode, GetNode, SetNode, CLIPVisionEncode, CLIPVisionLoader, SetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LayerUtility: PurgeVRAM, VAEDecode, GetNode, SetNode, KSamplerAdvanced, JWInteger, SetNode, Note, Note, JWInteger, easy showAnything, CR Prompt Text, AILab_QwenVL, RH_LLMAPI_Pro_Node, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), Note, SetNode, GetNode, GetNode, GetNode, Note, easy anythingIndexSwitch, SetNode, Note, SetNode, PathchSageAttentionKJ, PathchSageAttentionKJ, SetNode, ModelSamplingSD3, ModelSamplingSD3, CR Prompt Text, UNETLoader, UNETLoader, LoadImage, GetNode, VHS_VideoCombine, GetNode, Note, TT_img_enc_v2, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Remix  V3.0  图生视频 自动提示词_2034288165581758466.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034288165581758466.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
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
- `SetNode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `Note`
- `TT_img_enc_v2`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **45%**（33/73）

**有卡**：`KSamplerAdvanced`、`LayerUtility: PurgeVRAM`、`VAELoader`、`CLIPLoader`、`CLIPVisionEncode`、`CLIPVisionLoader`、`CLIPTextEncode`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`JWInteger`、`CR Prompt Text`、`AILab_QwenVL`、`RH_LLMAPI_Pro_Node`、`easy anythingIndexSwitch`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`LoadImage`、`VHS_VideoCombine`、`TT_img_enc_v2`、`SaveImage`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
