---
key: 平台全量/LTX2.3 V2V CrossView Prompt  镜头切换视频生视频工作流_2077360035210027010.json
name: LTX2.3 V2V CrossView Prompt  镜头切换视频生视频工作流_2077360035210027010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3 V2V CrossView Prompt  镜头切换视频生视频工作流_2077360035210027010.json
hash: 24b6f993dc61ec80
coverage: 0.449275
learned_at: 2026-11-14 00:37:34
nodes: [CR Float To Integer, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, KSamplerSelect, SetNode, PathchSageAttentionKJ, GetNode, GetNode, SetNode, SetNode, PrimitiveFloat, PrimitiveInt, PrimitiveInt, SetNode, SetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVConditioning, GetNode, GetNode, SetNode, SamplerCustom, LTXVCropGuides, LTXVSeparateAVLatent, GetNode, VAEDecode, SetNode, GetNode, easy cleanGpuUsed, easy clearCacheAll, ManualSigmas, ImageConcatMulti, ConditioningZeroOut, GetNode, GetNode, LTXVEmptyLatentAudio, LTXAddVideoICLoRAGuide, LTXVConcatAVLatent, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, MathExpression|pysssss, VHS_VideoCombine, MarkdownNote, PrimitiveInt, CLIPTextEncode, SetNode, CM_FloatToInt, SetNode, UNETLoader, LoraLoaderModelOnly, Note, LTXICLoRALoaderModelOnly, VAELoader, VAELoader, DualCLIPLoader, VHS_LoadVideo, GetNode, GetNode, LTXVImgToVideoConditionOnly, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX2.3 V2V CrossView Prompt  镜头切换视频生视频工作流_2077360035210027010.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3 V2V CrossView Prompt  镜头切换视频生视频工作流_2077360035210027010.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（69 个）：
- `CR Float To Integer`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `PathchSageAttentionKJ`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `SetNode`
- `SamplerCustom` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `ManualSigmas`
- `ImageConcatMulti`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `MarkdownNote`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `SetNode`
- `CM_FloatToInt`
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LTXICLoRALoaderModelOnly` ★核心
- `VAELoader`
- `VAELoader`
- `DualCLIPLoader`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **45%**（31/69）

**有卡**：`CR Float To Integer`、`KSamplerSelect`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`SamplerCustom`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`VAEDecode`、`easy cleanGpuUsed`、`easy clearCacheAll`、`ManualSigmas`、`ImageConcatMulti`、`ConditioningZeroOut`、`LTXVEmptyLatentAudio`、`LTXAddVideoICLoRAGuide`、`LTXVConcatAVLatent`、`ImageResizeKJv2`、`MathExpression|pysssss`、`VHS_VideoCombine`、`CLIPTextEncode`、`CM_FloatToInt`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`VAELoader`、`DualCLIPLoader`、`VHS_LoadVideo`、`LTXVImgToVideoConditionOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、UNETLoader、KSamplerSelect、SamplerCustom
