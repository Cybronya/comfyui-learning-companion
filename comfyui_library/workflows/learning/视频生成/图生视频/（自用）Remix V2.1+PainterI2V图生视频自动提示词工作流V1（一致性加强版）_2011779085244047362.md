---
key: 视频生成/图生视频/（自用）Remix V2.1+PainterI2V图生视频自动提示词工作流V1（一致性加强版）_2011779085244047362.json
name: （自用）Remix V2.1+PainterI2V图生视频自动提示词工作流V1（一致性加强版）_2011779085244047362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（自用）Remix V2.1+PainterI2V图生视频自动提示词工作流V1（一致性加强版）_2011779085244047362.json
hash: 9bca41a8eb586bca
coverage: 0.746269
learned_at: 2026-10-15 22:34:25
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, Pick From Batch (mtb), VAEDecode, PainterI2V, KSamplerAdvanced, PathchSageAttentionKJ, PathchSageAttentionKJ, LayerUtility: PurgeVRAM, RH_LLMAPI_NODE, AILab_QwenVL, CLIPTextEncode, UNETLoader, UNETLoader, Reroute, Note, Note, Note, easy anythingIndexSwitch, Note, Seed (rgthree), Reroute, ImageFromBatch+, LayerUtility: PurgeVRAM, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, Float, UNETLoader, UNETLoader, JWInteger, JWInteger, easy showAnything, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, LoadImage, easy showAnything, CR Prompt Text, VHS_VideoCombine, VHS_VideoCombine, SaveImage, TT_img_enc_v2, SaveImage, TT_img_enc, DuckHideNode, SaveImage, RunningHub Deepcleaner, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/（自用）Remix V2.1+PainterI2V图生视频自动提示词工作流V1（一致性加强版）_2011779085244047362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011779085244047362.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `Note`
- `Note`
- `ImageScaleBy`
- `Note`
- `ImageResizeKJv2`
- `SaveImage`
- `ColorMatch`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `Note`
- `CLIPVisionLoader`
- `VAELoader`
- `Note`
- `Note`
- `Note`
- `CLIPLoader`
- `Note`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `VAEDecode` ★核心
- `PainterI2V`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LayerUtility: PurgeVRAM`
- `RH_LLMAPI_NODE`
- `AILab_QwenVL`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Reroute`
- `Note`
- `Note`
- `Note`
- `easy anythingIndexSwitch`
- `Note`
- `Seed (rgthree)`
- `Reroute`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Float`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `JWInteger`
- `JWInteger`
- `easy showAnything`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `LoadImage`
- `easy showAnything`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SaveImage`
- `TT_img_enc_v2`
- `SaveImage`
- `TT_img_enc`
- `DuckHideNode`
- `SaveImage`
- `RunningHub Deepcleaner`
- `CR Prompt Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（50/67）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`Pick From Batch (mtb)`、`VAEDecode`、`PainterI2V`、`PathchSageAttentionKJ`、`LayerUtility: PurgeVRAM`、`RH_LLMAPI_NODE`、`AILab_QwenVL`、`UNETLoader`、`easy anythingIndexSwitch`、`Seed (rgthree)`、`ImageFromBatch+`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`Float`、`JWInteger`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`LoadImage`、`CR Prompt Text`、`VHS_VideoCombine`、`TT_img_enc_v2`、`TT_img_enc`、`DuckHideNode`、`RunningHub Deepcleaner`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
