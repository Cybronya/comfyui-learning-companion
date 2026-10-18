---
key: 视频生成/图生视频/六图丝滑循环变身wan2.2+vace+FlashVSR+变身LORA_1997299541873475585.json
name: 六图丝滑循环变身wan2.2+vace+FlashVSR+变身LORA_1997299541873475585.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/六图丝滑循环变身wan2.2+vace+FlashVSR+变身LORA_1997299541873475585.json
hash: 6961c6c303a48cc8
coverage: 0.912281
learned_at: 2026-10-15 22:33:29
nodes: [CLIPTextEncode, easy showAnything, ImageResizeKJ, ImageResizeKJ, easy forLoopStart, ImageBatchMulti, JWImageExtractFromBatch, PreviewImage, ImageResizeKJ, ImageResizeKJ, ImageResizeKJ, ImageResizeKJ, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, Int, Int, Int, CLIPLoader, TrimVideoLatent, VAEDecode, WanVaceToVideo, easy batchAnything, easy forLoopEnd, MathExpression|pysssss, MathExpression|pysssss, PreviewImage, JWImageExtractFromBatch, PreviewImage, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, Int, CLIPTextEncode, String Literal, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, VAELoader, KSampler, VHS_VideoCombine, Lora Loader Stack (rgthree), WanVideoEnhanceAVideoKJ, CFGNorm, PathchSageAttentionKJ, ModelSamplingSD3, UnetLoaderGGUF, RHHiddenNodes, Fast Groups Bypasser (rgthree), VHS_VideoCombine, LoraLoaderModelOnly, FlashVSRNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 772712932423515, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/六图丝滑循环变身wan2.2+vace+FlashVSR+变身LORA_1997299541873475585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1997299541873475585.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `easy forLoopStart`
- `ImageBatchMulti`
- `JWImageExtractFromBatch`
- `PreviewImage`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `Int`
- `Int`
- `Int`
- `CLIPLoader`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `WanVaceToVideo`
- `easy batchAnything`
- `easy forLoopEnd`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `PreviewImage`
- `JWImageExtractFromBatch`
- `PreviewImage`
- `WanVideoVACEStartToEndFrame`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Int`
- `CLIPTextEncode` ★核心
- `String Literal`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `VAELoader`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `Lora Loader Stack (rgthree)`
- `WanVideoEnhanceAVideoKJ`
- `CFGNorm`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UnetLoaderGGUF` ★核心
- `RHHiddenNodes`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `FlashVSRNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `772712932423515`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（52/57）

**有卡**：`CLIPTextEncode`、`ImageResizeKJ`、`easy forLoopStart`、`ImageBatchMulti`、`JWImageExtractFromBatch`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`Int`、`CLIPLoader`、`TrimVideoLatent`、`VAEDecode`、`WanVaceToVideo`、`easy batchAnything`、`easy forLoopEnd`、`MathExpression|pysssss`、`WanVideoVACEStartToEndFrame`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`String Literal`、`LayerUtility: PurgeVRAM V2`、`VAELoader`、`KSampler`、`Lora Loader Stack (rgthree)`、`WanVideoEnhanceAVideoKJ`、`CFGNorm`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UnetLoaderGGUF`、`RHHiddenNodes`、`LoraLoaderModelOnly`、`FlashVSRNode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
