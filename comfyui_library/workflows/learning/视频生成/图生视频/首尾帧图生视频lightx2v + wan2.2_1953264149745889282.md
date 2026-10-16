---
key: 视频生成/图生视频/首尾帧图生视频lightx2v + wan2.2_1953264149745889282.json
name: 首尾帧图生视频lightx2v + wan2.2_1953264149745889282.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1953264149745889282.json
hash: 47d7469c7aca513b
coverage: 0.918919
learned_at: 2026-10-15 22:31:04
nodes: [easy ifElse, RH_Captioner, ImageStitch, easy showAnything, Textbox, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPLoader, RH_Translator, LoadImage, LoadImage, CLIPVisionLoader, LayerUtility: ImageMaskScaleAs, CLIPVisionEncode, CLIPVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, WanVideoNAG, ModelSamplingSD3, PathchSageAttentionKJ, WanVideoNAG, ModelSamplingSD3, WanFirstLastFrameToVideo, SimpleMath+, DF_Integer, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CreateVideo, SaveVideo, PrimitiveBoolean, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/首尾帧图生视频lightx2v + wan2.2_1953264149745889282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953264149745889282.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `easy ifElse`
- `RH_Captioner`
- `ImageStitch`
- `easy showAnything`
- `Textbox`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `RH_Translator`
- `LoadImage`
- `LoadImage`
- `CLIPVisionLoader`
- `LayerUtility: ImageMaskScaleAs`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `WanFirstLastFrameToVideo`
- `SimpleMath+`
- `DF_Integer`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `PrimitiveBoolean`
- `easy showAnything`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`RH_Captioner`、`ImageStitch`、`Textbox`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`RH_Translator`、`LoadImage`、`CLIPVisionLoader`、`LayerUtility: ImageMaskScaleAs`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ModelSamplingSD3`、`WanFirstLastFrameToVideo`、`SimpleMath+`、`DF_Integer`、`KSamplerAdvanced`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`PrimitiveBoolean`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
