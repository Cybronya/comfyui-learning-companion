---
key: 视频生成/文生视频/LTX2.5- 图生+文生视频_2034499552383868929.json
name: LTX2.5- 图生+文生视频_2034499552383868929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5- 图生+文生视频_2034499552383868929.json
hash: fbd5cb5f85412cbc
coverage: 0.893617
learned_at: 2026-10-15 22:45:16
nodes: [llama_cpp_model_loader, Note, LoadImage, PrimitiveBoolean, PrimitiveFloat, Note, KSamplerSelect, CFGGuider, RandomNoise, ManualSigmas, SamplerCustomAdvanced, KSamplerSelect, LTXVImgToVideoConditionOnly, CFGGuider, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine, CLIPTextEncode, ManualSigmas, RandomNoise, LTXVConcatAVLatent, INTConstant, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CR Text, llama_cpp_instruct_adv, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, CLIPTextEncode, LTXVLatentUpsampler, ShowText|pysssss, easy cleanGpuUsed, CR Text, PrimitiveInt, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, VAELoaderKJ, VAELoaderKJ, UnetLoaderGGUF, LTXVConditioning, DualCLIPLoaderGGUF, LatentUpscaleModelLoader, LTXVPreprocess, EmptyLTXVLatentVideo, CM_FloatToInt, LTXVConcatAVLatent]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5- 图生+文生视频_2034499552383868929.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5- 图生+文生视频_2034499552383868929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（47 个）：
- `llama_cpp_model_loader`
- `Note`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `Note`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `LTXVImgToVideoConditionOnly`
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `INTConstant`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CR Text`
- `llama_cpp_instruct_adv`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LTXVLatentUpsampler` ★核心
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `CR Text`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoConditionOnly`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UnetLoaderGGUF` ★核心
- `LTXVConditioning`
- `DualCLIPLoaderGGUF`
- `LatentUpscaleModelLoader`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `CM_FloatToInt`
- `LTXVConcatAVLatent`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（42/47）

**有卡**：`llama_cpp_model_loader`、`LoadImage`、`PrimitiveBoolean`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVImgToVideoConditionOnly`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`INTConstant`、`LTXVSeparateAVLatent`、`CR Text`、`llama_cpp_instruct_adv`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVLatentUpsampler`、`easy cleanGpuUsed`、`LTXVEmptyLatentAudio`、`VAELoaderKJ`、`UnetLoaderGGUF`、`LTXVConditioning`、`DualCLIPLoaderGGUF`、`LatentUpscaleModelLoader`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`CM_FloatToInt`

**用到的条目**：CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent、LTXVSeparateAVLatent
