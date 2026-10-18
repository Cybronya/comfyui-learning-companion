---
key: 视频生成/图生视频/wan2.2首尾帧优化版_1956153773183959042.json
name: wan2.2首尾帧优化版_1956153773183959042.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2首尾帧优化版_1956153773183959042.json
hash: 4bb939a47b50cdb2
coverage: 0.918919
learned_at: 2026-10-15 22:31:11
nodes: [CLIPLoader, VAELoader, VAEDecode, CreateVideo, LayerUtility: ImageMaskScaleAs, WanFirstLastFrameToVideo, RH_Translator, easy showAnything, easy ifElse, CLIPVisionEncode, CLIPVisionEncode, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, UNETLoader, PrimitiveBoolean, KSamplerAdvanced, ImageStitch, PathchSageAttentionKJ, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, SaveVideo, KSamplerAdvanced, easy showAnything, ModelSamplingSD3, WanVideoNAG, WanVideoNAG, RH_Captioner, Textbox, DF_Integer, SimpleMath+, CLIPTextEncode, CLIPVisionLoader, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2首尾帧优化版_1956153773183959042.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956153773183959042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CreateVideo`
- `LayerUtility: ImageMaskScaleAs`
- `WanFirstLastFrameToVideo`
- `RH_Translator`
- `easy showAnything`
- `easy ifElse`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `PrimitiveBoolean`
- `KSamplerAdvanced` ★核心
- `ImageStitch`
- `PathchSageAttentionKJ`
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
- `DF_Integer`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
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

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`CreateVideo`、`LayerUtility: ImageMaskScaleAs`、`WanFirstLastFrameToVideo`、`RH_Translator`、`CLIPVisionEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`PrimitiveBoolean`、`KSamplerAdvanced`、`ImageStitch`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveVideo`、`WanVideoNAG`、`RH_Captioner`、`Textbox`、`DF_Integer`、`SimpleMath+`、`CLIPVisionLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
