---
key: 视频生成/文生视频/图生视频 & 文生视频｜+ HDR + 工业级自动调色（避免死黑过曝）｜LTX2.3_2047750461792460802.json
name: 图生视频 & 文生视频｜+ HDR + 工业级自动调色（避免死黑过曝）｜LTX2.3_2047750461792460802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/图生视频 & 文生视频｜+ HDR + 工业级自动调色（避免死黑过曝）｜LTX2.3_2047750461792460802.json
hash: ca939741c285b896
coverage: 0.586207
learned_at: 2026-10-11 19:49:48
nodes: [LTXVPreprocess, ResizeImagesByLongerEdge, LTXVEmptyLatentAudio, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, LTXVCropGuides, LTXVImgToVideoInplace, CFGGuider, LTXVConcatAVLatent, Note, Note, PrimitiveFloat, Note, Note, Note, ComfyMathExpression, SimpleCalculatorKJ, Note, ComfyMathExpression, Note, easy showAnything, SimpleCalculatorKJ, easy cleanGpuUsed, LTX2SamplingPreviewOverride, Note, RandomNoise, easy showAnything, Note, Note, Qwen3_VQA, Note, Note, Note, Note, ttN concat, Note, ShowText|pysssss, MemoryCleaner, JoinStrings, Note, CreateVideo, easy cleanGpuUsed, easy cleanGpuUsed, LTXVConditioning, Note, CLIPTextEncode, LatentUpscaleModelLoader, ManualSigmas, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTX2_NAG, LTXVEnhanceAVideoKJ, KSamplerSelect, ResizeImageMaskNode, SamplerCustomAdvanced, SamplerCustomAdvanced, PrimitiveFloat, PrimitiveInt, PrimitiveInt, LoadImage, LTXVSeparateAVLatent, VAEDecodeTiled, easy cleanGpuUsed, LTXVAudioVAEDecode, SeedGenerator, SaveVideo, Note, Note, Note, PrimitiveBoolean, CR Text, easy cleanGpuUsed, CLIPTextEncode, ImageSharpen, Image Levels Adjustment, LTXVHDRDecodePostprocess, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, Note]
patterns: []
missing: [CR Text, Image Levels Adjustment, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, ttN concat]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Image Levels Adjustment` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/图生视频 & 文生视频｜+ HDR + 工业级自动调色（避免死黑过曝）｜LTX2.3_2047750461792460802.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/图生视频 & 文生视频｜+ HDR + 工业级自动调色（避免死黑过曝）｜LTX2.3_2047750461792460802.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `EmptyLTXVLatentVideo`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `Note`
- `Note`
- `PrimitiveFloat`
- `Note`
- `Note`
- `Note`
- `ComfyMathExpression`
- `SimpleCalculatorKJ`
- `Note`
- `ComfyMathExpression`
- `Note`
- `easy showAnything`
- `SimpleCalculatorKJ`
- `easy cleanGpuUsed`
- `LTX2SamplingPreviewOverride`
- `Note`
- `RandomNoise`
- `easy showAnything`
- `Note`
- `Note`
- `Qwen3_VQA`
- `Note`
- `Note`
- `Note`
- `Note`
- `ttN concat`
- `Note`
- `ShowText|pysssss`
- `MemoryCleaner`
- `JoinStrings`
- `Note`
- `CreateVideo`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LTXVConditioning`
- `Note`
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTX2_NAG`
- `LTXVEnhanceAVideoKJ`
- `KSamplerSelect` ★核心
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `LTXVAudioVAEDecode` ★核心
- `SeedGenerator`
- `SaveVideo`
- `Note`
- `Note`
- `Note`
- `PrimitiveBoolean`
- `CR Text`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `ImageSharpen`
- `Image Levels Adjustment`
- `LTXVHDRDecodePostprocess`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **59%**（51/87）

**有卡**：`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`LTXVEmptyLatentAudio`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`RandomNoise`、`EmptyLTXVLatentVideo`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`ComfyMathExpression`、`SimpleCalculatorKJ`、`LTX2SamplingPreviewOverride`、`Qwen3_VQA`、`MemoryCleaner`、`JoinStrings`、`CreateVideo`、`LTXVConditioning`、`CLIPTextEncode`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTX2_NAG`、`LTXVEnhanceAVideoKJ`、`ResizeImageMaskNode`、`SamplerCustomAdvanced`、`LoadImage`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SeedGenerator`、`SaveVideo`、`PrimitiveBoolean`、`ImageSharpen`、`LTXVHDRDecodePostprocess`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`

**缺卡**（8）：`CR Text`、`Image Levels Adjustment`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`ttN concat`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Image Levels Adjustment` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识
