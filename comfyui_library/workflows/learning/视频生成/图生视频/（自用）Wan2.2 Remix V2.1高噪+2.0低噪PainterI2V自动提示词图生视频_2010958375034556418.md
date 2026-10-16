---
key: 视频生成/图生视频/（自用）Wan2.2 Remix V2.1高噪+2.0低噪PainterI2V自动提示词图生视频_2010958375034556418.json
name: （自用）Wan2.2 Remix V2.1高噪+2.0低噪PainterI2V自动提示词图生视频_2010958375034556418.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2010958375034556418.json
hash: ff7eb58c2eadf03b
coverage: 0.746479
learned_at: 2026-10-15 22:34:19
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Seed (rgthree), Note, Note, LayerUtility: ImageScaleByAspectRatio V2, Note, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, Pick From Batch (mtb), LayerUtility: PurgeVRAM, easy showAnything, Reroute, LayerUtility: PurgeVRAM, VHS_SelectFilename, easy showAnything, Any To Any, easy showAnything, Note, CR Prompt Text, AILab_QwenVL, Note, Note, CR Prompt Text, Note, JWInteger, SaveImage, TT_img_enc_v2, SaveImage, TT_img_enc, CR Prompt Text, Qwen3_VQA, Text Concatenate, VHS_VideoCombine, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, JWInteger, SaveImage, DuckHideNode, LoadImage, VAEDecode, UNETLoader, PainterI2V, VHS_VideoCombine, CR Prompt Text, RH_LLMAPI_NODE, CLIPLoader, CLIPTextEncode, easy showAnything, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/（自用）Wan2.2 Remix V2.1高噪+2.0低噪PainterI2V自动提示词图生视频_2010958375034556418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010958375034556418.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
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
- `Seed (rgthree)`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `VHS_SelectFilename`
- `easy showAnything`
- `Any To Any`
- `easy showAnything`
- `Note`
- `CR Prompt Text`
- `AILab_QwenVL`
- `Note`
- `Note`
- `CR Prompt Text`
- `Note`
- `JWInteger`
- `SaveImage`
- `TT_img_enc_v2`
- `SaveImage`
- `TT_img_enc`
- `CR Prompt Text`
- `Qwen3_VQA`
- `Text Concatenate`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `JWInteger`
- `SaveImage`
- `DuckHideNode`
- `LoadImage`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `PainterI2V`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `RH_LLMAPI_NODE`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（53/71）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`Seed (rgthree)`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`Pick From Batch (mtb)`、`LayerUtility: PurgeVRAM`、`VHS_SelectFilename`、`Any To Any`、`CR Prompt Text`、`AILab_QwenVL`、`JWInteger`、`TT_img_enc_v2`、`TT_img_enc`、`Qwen3_VQA`、`Text Concatenate`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UNETLoader`、`wanBlockSwap`、`DuckHideNode`、`LoadImage`、`VAEDecode`、`PainterI2V`、`RH_LLMAPI_NODE`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
