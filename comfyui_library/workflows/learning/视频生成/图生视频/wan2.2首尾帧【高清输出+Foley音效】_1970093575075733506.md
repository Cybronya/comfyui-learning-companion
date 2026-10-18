---
key: 视频生成/图生视频/wan2.2首尾帧【高清输出+Foley音效】_1970093575075733506.json
name: wan2.2首尾帧【高清输出+Foley音效】_1970093575075733506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2首尾帧【高清输出+Foley音效】_1970093575075733506.json
hash: 5aa6ddf8dde3ea24
coverage: 0.87234
learned_at: 2026-10-15 22:31:52
nodes: [CLIPLoader, VAELoader, CLIPVisionLoader, WanFirstLastFrameToVideo, LoadImage, CLIPVisionEncode, CLIPVisionEncode, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, UNETLoader, LoadImage, KSamplerAdvanced, ImageStitch, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, KSamplerAdvanced, easy showAnything, ModelSamplingSD3, WanVideoNAG, WanVideoNAG, LayerUtility: ImageMaskScaleAs, PrimitiveBoolean, LayerUtility: ImageScaleByAspectRatio V2, UpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, VAEDecode, DF_Integer, SimpleMath+, SetNode, Float, ImageUpscaleWithModel, LayerUtility: PurgeVRAM V2, GetNode, HunyuanVideoFoley, NormalizeAudioLoudness, RH_Translator, Textbox, SetNode, easy ifElse, GetNode, RH_Captioner, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2首尾帧【高清输出+Foley音效】_1970093575075733506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1970093575075733506.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `LoadImage`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `ImageStitch`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `ModelSamplingSD3`
- `WanVideoNAG`
- `WanVideoNAG`
- `LayerUtility: ImageMaskScaleAs`
- `PrimitiveBoolean`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `DF_Integer`
- `SimpleMath+`
- `SetNode`
- `Float`
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `HunyuanVideoFoley`
- `NormalizeAudioLoudness`
- `RH_Translator`
- `Textbox`
- `SetNode`
- `easy ifElse`
- `GetNode`
- `RH_Captioner`
- `CR Prompt Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **87%**（41/47）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`LoadImage`、`CLIPVisionEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`ImageStitch`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`WanVideoNAG`、`LayerUtility: ImageMaskScaleAs`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`UpscaleModelLoader`、`VHS_VideoCombine`、`VAEDecode`、`DF_Integer`、`SimpleMath+`、`Float`、`ImageUpscaleWithModel`、`LayerUtility: PurgeVRAM V2`、`HunyuanVideoFoley`、`NormalizeAudioLoudness`、`RH_Translator`、`Textbox`、`RH_Captioner`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
