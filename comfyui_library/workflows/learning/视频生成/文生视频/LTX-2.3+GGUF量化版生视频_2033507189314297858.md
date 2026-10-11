---
key: 视频生成/文生视频/LTX-2.3+GGUF量化版生视频_2033507189314297858.json
name: LTX-2.3+GGUF量化版生视频_2033507189314297858
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3+GGUF量化版生视频_2033507189314297858.json
hash: c8d9a927d5c65a4b
coverage: 0.765957
learned_at: 2026-10-11 03:48:34
nodes: [KSamplerSelect, RandomNoise, CFGGuider, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, CR Text, LTXVPreprocess, LTXVImgToVideoConditionOnly, VAELoader, Fast Groups Bypasser (rgthree), CR Text, LTXVScheduler, LTXVConcatAVLatent, easy cleanGpuUsed, LTXVLatentUpsampler, easy cleanGpuUsed, INTConstant, PrimitiveInt, VAELoaderKJ, PrimitiveInt, LTXVSeparateAVLatent, easy cleanGpuUsed, LatentUpscaleModelLoader, LTXVConcatAVLatent, easy cleanGpuUsed, SamplerCustomAdvanced, ManualSigmas, KSamplerSelect, CFGGuider, RandomNoise, LTXVAudioVAEDecode, LTXVConditioning, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, INTConstant, INTConstant, CR Prompt Text, PrimitiveBoolean, CLIPTextEncode, CLIPTextEncode, UnetLoaderGGUF, DualCLIPLoaderGGUF, SamplerCustomAdvanced, LTXVSeparateAVLatent, VHS_VideoCombine, VAEDecodeTiled]
patterns: []
missing: [CR Text, CR Text, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX-2.3+GGUF量化版生视频_2033507189314297858.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3+GGUF量化版生视频_2033507189314297858.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（47 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `CR Text`
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `LTXVScheduler`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `LTXVLatentUpsampler` ★核心
- `easy cleanGpuUsed`
- `INTConstant`
- `PrimitiveInt`
- `VAELoaderKJ`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `CR Prompt Text`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoaderGGUF`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（36/47）

**有卡**：`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`VAELoader`、`LTXVScheduler`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`INTConstant`、`VAELoaderKJ`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LoadImage`、`PrimitiveBoolean`、`CLIPTextEncode`、`UnetLoaderGGUF`、`DualCLIPLoaderGGUF`、`VHS_VideoCombine`、`VAEDecodeTiled`

**缺卡**（8）：`CR Text`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
