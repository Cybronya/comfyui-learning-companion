---
key: 视频生成/图生视频/【全能图片V1双图分镜】Wan2.2-Smooth Mix图像生视频（一键成片）_1979720358234329089.json
name: 【全能图片V1双图分镜】Wan2.2-Smooth Mix图像生视频（一键成片）_1979720358234329089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【全能图片V1双图分镜】Wan2.2-Smooth Mix图像生视频（一键成片）_1979720358234329089.json
hash: 483a257440b4d979
coverage: 0.727273
learned_at: 2026-10-15 22:32:25
nodes: [Note, SetNode, easy batchAnything, ImageCASharpening+, RHHiddenNodes, CR Text, MathExpression|pysssss, VHS_LoadAudioUpload, Float, Float, Note, RHHiddenNodes, LoadImage, Note, PreviewImage, VHS_Unbatch, easy forLoopStart, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ImageConcanate, Text Load Line From File, QwenLoader, RHHiddenNodes, LayerUtility: PurgeVRAM V2, LoadImage, Note, CR Text Concatenate, BatchCount+, WanVideoPromptExtender, CR Text, PrimitiveBoolean, JWInteger, RHHiddenNodes, CR Text Concatenate, easy showAnything, CR Text, VHS_VideoCombine, JjkText, PreviewAudio, Int, wanBlockSwap, UNETLoader, PathchSageAttentionKJ, easy cleanGpuUsed, easy ifElse, UNETLoader, LoraLoaderModelOnly, easy cleanGpuUsed, PathchSageAttentionKJ, wanBlockSwap, ModelSamplingSD3, ImageResize+, ModelSamplingSD3, easy forLoopEnd, ColorCorrectOfUtils, KSamplerAdvanced, KSamplerAdvanced, ImpactSwitch, easy showAnything, Int, Note, VAEDecode, CLIPVisionLoader, SetNode, ImageResize+, RH_Captioner, GetNode, SetNode, PreviewImage, GetNode, easy imageListToImageBatch, GetNode, PreviewImage, CLIPVisionEncode, ImageResize+, SetNode, RH_Nano_Banana_Image2Image, GetNode, Note, Note, Note, WanImageToVideo, VAELoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, HunyuanVideoFoley, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/【全能图片V1双图分镜】Wan2.2-Smooth Mix图像生视频（一键成片）_1979720358234329089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979720358234329089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `Note`
- `SetNode`
- `easy batchAnything`
- `ImageCASharpening+`
- `RHHiddenNodes`
- `CR Text`
- `MathExpression|pysssss`
- `VHS_LoadAudioUpload`
- `Float`
- `Float`
- `Note`
- `RHHiddenNodes`
- `LoadImage`
- `Note`
- `PreviewImage`
- `VHS_Unbatch`
- `easy forLoopStart`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `ImageConcanate`
- `Text Load Line From File`
- `QwenLoader`
- `RHHiddenNodes`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `Note`
- `CR Text Concatenate`
- `BatchCount+`
- `WanVideoPromptExtender`
- `CR Text`
- `PrimitiveBoolean`
- `JWInteger`
- `RHHiddenNodes`
- `CR Text Concatenate`
- `easy showAnything`
- `CR Text`
- `VHS_VideoCombine`
- `JjkText`
- `PreviewAudio`
- `Int`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `easy cleanGpuUsed`
- `easy ifElse`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `ImageResize+`
- `ModelSamplingSD3`
- `easy forLoopEnd`
- `ColorCorrectOfUtils`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImpactSwitch`
- `easy showAnything`
- `Int`
- `Note`
- `VAEDecode` ★核心
- `CLIPVisionLoader`
- `SetNode`
- `ImageResize+`
- `RH_Captioner`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `easy imageListToImageBatch`
- `GetNode`
- `PreviewImage`
- `CLIPVisionEncode`
- `ImageResize+`
- `SetNode`
- `RH_Nano_Banana_Image2Image`
- `GetNode`
- `Note`
- `Note`
- `Note`
- `WanImageToVideo`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `HunyuanVideoFoley`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **73%**（64/88）

**有卡**：`easy batchAnything`、`ImageCASharpening+`、`RHHiddenNodes`、`CR Text`、`MathExpression|pysssss`、`VHS_LoadAudioUpload`、`Float`、`LoadImage`、`VHS_Unbatch`、`easy forLoopStart`、`LayerUtility: PurgeVRAM V2`、`ImageConcanate`、`Text Load Line From File`、`QwenLoader`、`CR Text Concatenate`、`BatchCount+`、`WanVideoPromptExtender`、`PrimitiveBoolean`、`JWInteger`、`VHS_VideoCombine`、`PreviewAudio`、`Int`、`wanBlockSwap`、`UNETLoader`、`PathchSageAttentionKJ`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`ImageResize+`、`easy forLoopEnd`、`ColorCorrectOfUtils`、`KSamplerAdvanced`、`VAEDecode`、`CLIPVisionLoader`、`RH_Captioner`、`easy imageListToImageBatch`、`CLIPVisionEncode`、`RH_Nano_Banana_Image2Image`、`WanImageToVideo`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`HunyuanVideoFoley`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
