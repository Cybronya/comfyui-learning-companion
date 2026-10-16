---
key: 视频生成/图生视频/wan2.2首尾帧视频-傲雪AIGC_1962136836984475650.json
name: wan2.2首尾帧视频-傲雪AIGC_1962136836984475650.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1962136836984475650.json
hash: 06097d9d510ea79f
coverage: 0.904762
learned_at: 2026-10-15 22:31:30
nodes: [LoraLoaderModelOnly, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, WanVideoNAG, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionLoader, CLIPLoader, VAELoader, LoadImage, LoadImage, easy ifElse, CLIPTextEncode, SimpleMath+, WanFirstLastFrameToVideo, WanVideoNAG, LayerUtility: ImageMaskScaleAs, VAEDecode, Textbox, PrimitiveBoolean, ImageStitch, RH_Captioner, easy showAnything, easy showAnything, RH_Translator, CLIPTextEncode, PlaySound|pysssss, KSamplerAdvanced, KSamplerAdvanced, DF_Integer, LayerUtility: ImageScaleByAspectRatio V2, CreateVideo, Int, MarkdownNote, LoadImage, SaveVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2首尾帧视频-傲雪AIGC_1962136836984475650.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962136836984475650.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `easy ifElse`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `WanFirstLastFrameToVideo`
- `WanVideoNAG`
- `LayerUtility: ImageMaskScaleAs`
- `VAEDecode` ★核心
- `Textbox`
- `PrimitiveBoolean`
- `ImageStitch`
- `RH_Captioner`
- `easy showAnything`
- `easy showAnything`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `PlaySound|pysssss`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `DF_Integer`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CreateVideo`
- `Int`
- `MarkdownNote`
- `LoadImage`
- `SaveVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（38/42）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ModelSamplingSD3`、`CLIPVisionEncode`、`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`CLIPTextEncode`、`SimpleMath+`、`WanFirstLastFrameToVideo`、`LayerUtility: ImageMaskScaleAs`、`VAEDecode`、`Textbox`、`PrimitiveBoolean`、`ImageStitch`、`RH_Captioner`、`RH_Translator`、`PlaySound|pysssss`、`KSamplerAdvanced`、`DF_Integer`、`LayerUtility: ImageScaleByAspectRatio V2`、`CreateVideo`、`Int`、`SaveVideo`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
