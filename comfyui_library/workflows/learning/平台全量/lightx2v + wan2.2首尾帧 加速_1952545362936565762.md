---
key: 平台全量/lightx2v + wan2.2首尾帧 加速_1952545362936565762.json
name: lightx2v + wan2.2首尾帧 加速_1952545362936565762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/lightx2v + wan2.2首尾帧 加速_1952545362936565762.json
hash: 37200a8fbf39bb4f
coverage: 0.918919
learned_at: 2026-11-14 01:14:25
nodes: [CLIPLoader, VAELoader, VAEDecode, CreateVideo, CLIPVisionLoader, LayerUtility: ImageMaskScaleAs, WanFirstLastFrameToVideo, RH_Translator, easy showAnything, easy ifElse, CLIPVisionEncode, CLIPVisionEncode, DF_Integer, SimpleMath+, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, UNETLoader, PrimitiveBoolean, KSamplerAdvanced, ImageStitch, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, SaveVideo, KSamplerAdvanced, easy showAnything, ModelSamplingSD3, WanVideoNAG, WanVideoNAG, RH_Captioner, Textbox, PathchSageAttentionKJ, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 平台全量/lightx2v + wan2.2首尾帧 加速_1952545362936565762.json

> 来源文件 `comfyui_library/workflows/平台全量/lightx2v + wan2.2首尾帧 加速_1952545362936565762.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CreateVideo`
- `CLIPVisionLoader`
- `LayerUtility: ImageMaskScaleAs`
- `WanFirstLastFrameToVideo`
- `RH_Translator`
- `easy showAnything`
- `easy ifElse`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `DF_Integer`
- `SimpleMath+`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `PrimitiveBoolean`
- `KSamplerAdvanced` ★核心
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `ModelSamplingSD3`
- `WanVideoNAG`
- `WanVideoNAG`
- `RH_Captioner`
- `Textbox`
- `PathchSageAttentionKJ`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`CreateVideo`、`CLIPVisionLoader`、`LayerUtility: ImageMaskScaleAs`、`WanFirstLastFrameToVideo`、`RH_Translator`、`CLIPVisionEncode`、`DF_Integer`、`SimpleMath+`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`PrimitiveBoolean`、`KSamplerAdvanced`、`ImageStitch`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveVideo`、`WanVideoNAG`、`RH_Captioner`、`Textbox`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerAdvanced
