---
key: 视频生成/文生视频/双采样高质量图生视频 LTX2.3-单镜头可扩写提示词 高度遵从 运镜+动作+自动扩写 -高质量1K_2057269109406126081.json
name: 双采样高质量图生视频 LTX2.3-单镜头可扩写提示词 高度遵从 运镜+动作+自动扩写 -高质量1K_2057269109406126081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/双采样高质量图生视频 LTX2.3-单镜头可扩写提示词 高度遵从 运镜+动作+自动扩写 -高质量1K_2057269109406126081.json
hash: 2272dbe53838ed71
coverage: 0.686275
learned_at: 2026-10-11 19:49:47
nodes: [LTXVAudioVAELoader, EmptyImage, ImageScaleBy, KSamplerSelect, LTXVConcatAVLatent, KSampler, GetImageSize, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConditioning, VAEDecode, LTXVAudioVAEDecode, CreateVideo, LTXVSeparateAVLatent, LTXVLatentUpsampler, LatentUpscaleModelLoader, RandomNoise, easy int, easy float, PrimitiveInt, MathExpression|pysssss, CFGGuider, LoraLoaderModelOnly, CheckpointLoaderSimple, RH_LLMAPI_Pro_Node, LTXVImgToVideoInplace, LayerUtility: ImageScaleByAspectRatio V2, Int, CR Prompt Text, LTXAVTextEncoderLoader, GetImageSize, MathExpression|pysssss, easy showAnything, easy float, CR Prompt Text, easy int, LTXVScheduler, CLIPTextEncode, CLIPTextEncode, LoadImage, SaveVideo, Note, Note, Note, CR Prompt Text, Fast Groups Bypasser (rgthree)]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, MathExpression|pysssss, easy float, easy float, easy int, easy int, CR Prompt Text, CR Prompt Text, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 715038988026475, "steps": 4, "width": 97}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/双采样高质量图生视频 LTX2.3-单镜头可扩写提示词 高度遵从 运镜+动作+自动扩写 -高质量1K_2057269109406126081.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/双采样高质量图生视频 LTX2.3-单镜头可扩写提示词 高度遵从 运镜+动作+自动扩写 -高质量1K_2057269109406126081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `LTXVAudioVAELoader`
- `EmptyImage`
- `ImageScaleBy`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConditioning`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `easy int`
- `easy float`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `RH_LLMAPI_Pro_Node`
- `LTXVImgToVideoInplace`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `CR Prompt Text`
- `LTXAVTextEncoderLoader`
- `GetImageSize`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy float`
- `CR Prompt Text`
- `easy int`
- `LTXVScheduler`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `SaveVideo`
- `Note`
- `Note`
- `Note`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `715038988026475`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **69%**（35/51）

**有卡**：`LTXVAudioVAELoader`、`EmptyImage`、`ImageScaleBy`、`KSamplerSelect`、`LTXVConcatAVLatent`、`KSampler`、`GetImageSize`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`VAEDecode`、`LTXVAudioVAEDecode`、`CreateVideo`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`RandomNoise`、`CFGGuider`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`RH_LLMAPI_Pro_Node`、`Int`、`LTXAVTextEncoderLoader`、`LTXVScheduler`、`CLIPTextEncode`、`LoadImage`、`SaveVideo`

**缺卡**（10）：`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`MathExpression|pysssss`、`easy float`、`easy float`、`easy int`、`easy int`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
