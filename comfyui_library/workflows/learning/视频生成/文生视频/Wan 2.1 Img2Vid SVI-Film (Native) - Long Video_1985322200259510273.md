---
key: 视频生成/文生视频/Wan 2.1 Img2Vid SVI-Film (Native) - Long Video_1985322200259510273.json
name: Wan 2.1 Img2Vid SVI-Film (Native) - Long Video_1985322200259510273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.1 Img2Vid SVI-Film (Native) - Long Video_1985322200259510273.json
hash: 6c5b03f06b549bc9
coverage: 0.304348
learned_at: 2026-10-10 23:06:08
nodes: [ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveInt, SetNode, SetNode, GetNode, GetNode, ImageResizeKJv2, GetImageSizeAndCount, MathExpression|pysssss, GetNode, VAEDecode, GetImageRangeFromBatch, GetNode, MathExpression|pysssss, GetNode, GetNode, VHS_VideoCombine, easy showAnything, CLIPTextEncode, GetNode, SetNode, PrimitiveInt, SetNode, SetNode, LayerColor: Brightness & Contrast, GetNode, GetNode, UnetLoaderGGUF, PreviewImage, GetNode, ImageBatchMulti, CLIPVisionEncode, SetNode, GetNode, SetNode, easy forLoopStart, CLIPTextEncode, SetNode, Display Any (rgthree), ImageResizeKJv2, GetNode, GetNode, PreviewImage, SetNode, LoadImage, UNETLoader, TorchCompileModel, Note, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPVisionLoader, VAELoader, CLIPLoader, Note, PrimitiveInt, SetNode, Note, Note, GetNode, GetNode, SetNode, Note, WanImageToVideo, CR Prompt List, GetNode, SetNode, PrimitiveInt, SetNode, PrimitiveFloat, SimpleMath+, MathExpression|pysssss, GetNode, MathExpression|pysssss, GetNode, PrimitiveStringMultiline, easy showAnything, RIFE VFI, Note, KSampler, ImageColorMatch+, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, wanBlockSwap, ImageFromBatch, ImageBatchMulti, easy forLoopEnd, Note, PrimitiveStringMultiline, VHS_VideoCombine, PrimitiveInt]
patterns: []
missing: [Display Any (rgthree), ImageColorMatch+, LayerColor: Brightness & Contrast, LayerUtility: PurgeVRAM, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, RIFE VFI, SimpleMath+, easy forLoopEnd, easy forLoopStart, CR Prompt List]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 307993194522586, "steps": 8}
discoveries: [次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageColorMatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerColor: Brightness & Contrast` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan 2.1 Img2Vid SVI-Film (Native) - Long Video_1985322200259510273.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.1 Img2Vid SVI-Film (Native) - Long Video_1985322200259510273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `MathExpression|pysssss`
- `GetNode`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `LayerColor: Brightness & Contrast`
- `GetNode`
- `GetNode`
- `UnetLoaderGGUF` ★核心
- `PreviewImage`
- `GetNode`
- `ImageBatchMulti`
- `CLIPVisionEncode`
- `SetNode`
- `GetNode`
- `SetNode`
- `easy forLoopStart`
- `CLIPTextEncode` ★核心
- `SetNode`
- `Display Any (rgthree)`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `LoadImage`
- `UNETLoader` ★核心
- `TorchCompileModel`
- `Note`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPLoader`
- `Note`
- `PrimitiveInt`
- `SetNode`
- `Note`
- `Note`
- `GetNode`
- `GetNode`
- `SetNode`
- `Note`
- `WanImageToVideo`
- `CR Prompt List`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `PrimitiveFloat`
- `SimpleMath+`
- `MathExpression|pysssss`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `RIFE VFI`
- `Note`
- `KSampler` ★核心
- `ImageColorMatch+`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `wanBlockSwap`
- `ImageFromBatch`
- `ImageBatchMulti`
- `easy forLoopEnd`
- `Note`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `PrimitiveInt`

## 关键参数

- `seed` = `307993194522586`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **30%**（28/92）

**有卡**：`ModelSamplingSD3`、`PathchSageAttentionKJ`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`VAEDecode`、`GetImageRangeFromBatch`、`VHS_VideoCombine`、`CLIPTextEncode`、`UnetLoaderGGUF`、`ImageBatchMulti`、`CLIPVisionEncode`、`LoadImage`、`UNETLoader`、`TorchCompileModel`、`LoraLoaderModelOnly`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`WanImageToVideo`、`KSampler`、`wanBlockSwap`、`ImageFromBatch`

**缺卡**（13）：`Display Any (rgthree)`、`ImageColorMatch+`、`LayerColor: Brightness & Contrast`、`LayerUtility: PurgeVRAM`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`RIFE VFI`、`SimpleMath+`、`easy forLoopEnd`、`easy forLoopStart`、`CR Prompt List`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageColorMatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerColor: Brightness & Contrast` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
