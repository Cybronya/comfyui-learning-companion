---
key: 视频生成/图生视频/wan2.2 图生视频 (加速版) + 自动提示词 + 润色扩写_1952550373196279809.json
name: wan2.2 图生视频 (加速版) + 自动提示词 + 润色扩写_1952550373196279809.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 图生视频 (加速版) + 自动提示词 + 润色扩写_1952550373196279809.json
hash: bc3450594ab3daf8
coverage: 0.777778
learned_at: 2026-10-15 22:31:02
nodes: [VAELoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionLoader, SimpleMath+, CLIPVisionEncode, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, WanImageToVideo, VAEDecode, RH_Translator, Text Multiline, RH_Translator, LayerUtility: ImageScaleByAspectRatio V2, easy ifElse, PrimitiveBoolean, Note, PrimitiveBoolean, Note, DF_Integer, KSamplerAdvanced, Note, Note, Text Multiline, RH_Captioner, easy ifElse, ShowText|pysssss, ShowText|pysssss, string_util_StrReplace, RH_LLMAPI_NODE, ShowText|pysssss, INTConstant, INTConstant, easy int, KSamplerAdvanced, ShowText|pysssss, UNETLoader, UNETLoader, LoraLoaderModelOnly, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2 图生视频 (加速版) + 自动提示词 + 润色扩写_1952550373196279809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952550373196279809.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（45 个）：
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `SimpleMath+`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `RH_Translator`
- `Text Multiline`
- `RH_Translator`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy ifElse`
- `PrimitiveBoolean`
- `Note`
- `PrimitiveBoolean`
- `Note`
- `DF_Integer`
- `KSamplerAdvanced` ★核心
- `Note`
- `Note`
- `Text Multiline`
- `RH_Captioner`
- `easy ifElse`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `string_util_StrReplace`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `INTConstant`
- `INTConstant`
- `easy int`
- `KSamplerAdvanced` ★核心
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **78%**（35/45）

**有卡**：`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionLoader`、`SimpleMath+`、`CLIPVisionEncode`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`WanImageToVideo`、`VAEDecode`、`RH_Translator`、`Text Multiline`、`LayerUtility: ImageScaleByAspectRatio V2`、`PrimitiveBoolean`、`DF_Integer`、`KSamplerAdvanced`、`RH_Captioner`、`string_util_StrReplace`、`RH_LLMAPI_NODE`、`INTConstant`、`easy int`、`UNETLoader`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
