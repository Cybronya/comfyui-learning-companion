---
key: 视频生成/文生视频/wan2.2 首尾帧视频_1957693851249078273.json
name: wan2.2 首尾帧视频_1957693851249078273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 首尾帧视频_1957693851249078273.json
hash: 380bd58a74242bc0
coverage: 0.837838
learned_at: 2026-10-10 23:09:37
nodes: [CLIPLoader, VAELoader, VAEDecode, CreateVideo, CLIPVisionLoader, LayerUtility: ImageMaskScaleAs, WanFirstLastFrameToVideo, RH_Translator, easy showAnything, easy ifElse, CLIPVisionEncode, CLIPVisionEncode, DF_Integer, SimpleMath+, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, UNETLoader, PrimitiveBoolean, KSamplerAdvanced, ImageStitch, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, SaveVideo, KSamplerAdvanced, easy showAnything, ModelSamplingSD3, WanVideoNAG, WanVideoNAG, RH_Captioner, Textbox, LoadImage, LoadImage]
patterns: []
missing: [LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `LayerUtility: ImageMaskScaleAs` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2 首尾帧视频_1957693851249078273.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2 首尾帧视频_1957693851249078273.json`

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
- `PathchSageAttentionKJ`
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

覆盖率 **84%**（31/37）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`CreateVideo`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`RH_Translator`、`CLIPVisionEncode`、`DF_Integer`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`PrimitiveBoolean`、`KSamplerAdvanced`、`ImageStitch`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`SaveVideo`、`WanVideoNAG`、`RH_Captioner`、`Textbox`、`LoadImage`

**缺卡**（3）：`LayerUtility: ImageMaskScaleAs`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `LayerUtility: ImageMaskScaleAs` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
