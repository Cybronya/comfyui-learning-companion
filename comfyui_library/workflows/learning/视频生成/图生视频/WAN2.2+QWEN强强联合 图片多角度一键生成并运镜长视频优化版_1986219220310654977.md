---
key: 视频生成/图生视频/WAN2.2+QWEN强强联合 图片多角度一键生成并运镜长视频优化版_1986219220310654977.json
name: WAN2.2+QWEN强强联合 图片多角度一键生成并运镜长视频优化版_1986219220310654977.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2+QWEN强强联合 图片多角度一键生成并运镜长视频优化版_1986219220310654977.json
hash: 012b9565aca3ff87
coverage: 0.484277
learned_at: 2026-10-15 22:32:54
nodes: [VAEDecode, ImageFromBatch, GetNode, ModelSamplingSD3, GetNode, CLIPTextEncode, CLIPTextEncode, SetNode, MathExpression|pysssss, GetNode, GetNode, DownloadAndLoadGIMMVFIModel, SetNode, GetImageSizeAndCount, GIMMVFI_interpolate, ImageBatch, GetNode, GetNode, UNETLoader, CLIPLoader, VAELoader, LayerUtility: PurgeVRAM, TextEncodeQwenImageEditPlus, SetNode, GetNode, GetNode, VAEDecode, LayerUtility: PurgeVRAM, KSampler, JjkText, JjkText, VAEDecode, SetNode, VAEEncode, GetNode, GetNode, LayerUtility: PurgeVRAM, ModelSamplingAuraFlow, CFGNorm, SetNode, SetNode, GetNode, SetNode, VAEDecode, LayerUtility: PurgeVRAM, TextEncodeQwenImageEditPlus, SetNode, VAEDecode, LayerUtility: PurgeVRAM, KSampler, GetNode, TextEncodeQwenImageEditPlus, SetNode, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, JjkText, SetNode, GetNode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, GetNode, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionEncode, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, GetNode, GetNode, GetNode, GetNode, WanFirstMiddleLastFrameToVideo, GetNode, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, GetNode, SaveImage, SaveImage, SaveImage, SaveImage, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, VAELoader, SetNode, CLIPLoader, wanBlockSwap, GetNode, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionEncode, SimpleMath+, SetNode, VHS_VideoCombine, GetNode, KSamplerAdvanced, WanFirstMiddleLastFrameToVideo, GetNode, GetNode, GetNode, SetNode, GetNode, CLIPVisionLoader, PathchSageAttentionKJ, wanBlockSwap, LayerUtility: PurgeVRAM, UNETLoader, LayerUtility: PurgeVRAM, UNETLoader, PathchSageAttentionKJ, SetNode, SetNode, GetNode, GetNode, PrimitiveInt, GetImageRangeFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, JjkText, KSampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, KSamplerAdvanced, ImageResizeKJv2, PrimitiveInt, SimpleMath+, LayerUtility: PurgeVRAM, GetNode, GetNode, LayerUtility: PurgeVRAM, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/WAN2.2+QWEN强强联合 图片多角度一键生成并运镜长视频优化版_1986219220310654977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986219220310654977.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（159 个）：
- `VAEDecode` ★核心
- `ImageFromBatch`
- `GetNode`
- `ModelSamplingSD3`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `DownloadAndLoadGIMMVFIModel`
- `SetNode`
- `GetImageSizeAndCount`
- `GIMMVFI_interpolate`
- `ImageBatch`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: PurgeVRAM`
- `TextEncodeQwenImageEditPlus`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `JjkText`
- `JjkText`
- `VAEDecode` ★核心
- `SetNode`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `TextEncodeQwenImageEditPlus`
- `SetNode`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `SetNode`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `JjkText`
- `SetNode`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `GetNode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanFirstMiddleLastFrameToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `SetNode`
- `CLIPLoader`
- `wanBlockSwap`
- `GetNode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `SimpleMath+`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `CLIPVisionLoader`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `JjkText`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `ImageResizeKJv2`
- `PrimitiveInt`
- `SimpleMath+`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **48%**（77/159）

**有卡**：`VAEDecode`、`ImageFromBatch`、`ModelSamplingSD3`、`CLIPTextEncode`、`MathExpression|pysssss`、`DownloadAndLoadGIMMVFIModel`、`GetImageSizeAndCount`、`GIMMVFI_interpolate`、`ImageBatch`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LayerUtility: PurgeVRAM`、`TextEncodeQwenImageEditPlus`、`KSampler`、`VAEEncode`、`ModelSamplingAuraFlow`、`CFGNorm`、`LoraLoaderModelOnly`、`CLIPVisionEncode`、`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`SaveImage`、`wanBlockSwap`、`SimpleMath+`、`VHS_VideoCombine`、`CLIPVisionLoader`、`PathchSageAttentionKJ`、`GetImageRangeFromBatch`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
