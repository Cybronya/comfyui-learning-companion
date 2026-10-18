---
key: 视频生成/图生视频/BlueNan-WAN2.2 SMOOTH I2V自动首尾帧无限长度视频生成v1.0_1994048504089739265.json
name: BlueNan-WAN2.2 SMOOTH I2V自动首尾帧无限长度视频生成v1.0_1994048504089739265.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/BlueNan-WAN2.2 SMOOTH I2V自动首尾帧无限长度视频生成v1.0_1994048504089739265.json
hash: d181a49db94c6c4b
coverage: 0.441379
learned_at: 2026-10-15 22:33:20
nodes: [Int, SetNode, SetNode, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, wanBlockSwap, GetNode, GetNode, GetNode, GetNode, CLIPVisionEncode, GetNode, MathExpression|pysssss, WanMoeKSampler, GetNode, easy forLoopEnd, GetNode, GetNode, SetNode, PreviewImage, GetImageRangeFromBatch, PathchSageAttentionKJ, ImageScaleBy, VAEDecode, GetImageSizeAndCount, GetNode, MathExpression|pysssss, ImageScaleBy, VAEDecode, RIFE VFI, RIFE VFI, easy cleanGpuUsed, easy promptLine, CLIPTextEncode, SetNode, CR Text Concatenate, GetNode, easy showAnything, GetNode, GetNode, GetNode, CR Text Concatenate, SetNode, CLIPTextEncode, SetNode, SetNode, SetNode, GetNode, easy showAnything, Int, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, ImageFromBatch, SetNode, easy showAnything, ImageBatchMulti, INTConstant, GetNode, GetNode, GetNode, INTConstant, GetNode, GetNode, MathExpression|pysssss, Int, Int, CLIPTextEncode, LoraLoaderModelOnly, Int, PreviewImage, Fast Groups Bypasser (rgthree), SetNode, GetNode, WanImageToVideo, ImageResizeKJv2, GetNode, SetNode, easy showAnything, GetNode, CLIPVisionLoader, Fast Groups Muter (rgthree), VAELoader, CLIPLoader, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, easy forLoopEnd, Note, Note, LoadImageListFromDir //Inspire, easy forLoopStart, WanImageToVideo, WanMoeKSampler, SetNode, GetNode, GetNode, PreviewImage, ImageResizeKJv2, MathExpression|pysssss, LoadImage, SetNode, GetNode, easy forLoopStart, LoraLoaderModelOnly, wanBlockSwap, CR Seed, UNETLoader, UNETLoader, MathExpression|pysssss, VHS_VideoCombine, SetNode, VRAM_Debug, SetNode, GetNode, easy cleanGpuUsed, ImageScaleBy, VHS_VideoCombine, VHS_VideoCombine, ProductInfoBuilder, SoraPromptFromProduct]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "uni_pc", "sampler_name": 1, "scheduler": 1, "seed": 1, "steps": "fixed"}
---

# 视频生成/图生视频/BlueNan-WAN2.2 SMOOTH I2V自动首尾帧无限长度视频生成v1.0_1994048504089739265.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1994048504089739265.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（145 个）：
- `Int`
- `SetNode`
- `SetNode`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SetNode`
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
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `wanBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `MathExpression|pysssss`
- `WanMoeKSampler` ★核心
- `GetNode`
- `easy forLoopEnd`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `GetImageRangeFromBatch`
- `PathchSageAttentionKJ`
- `ImageScaleBy`
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `GetNode`
- `MathExpression|pysssss`
- `ImageScaleBy`
- `VAEDecode` ★核心
- `RIFE VFI`
- `RIFE VFI`
- `easy cleanGpuUsed`
- `easy promptLine`
- `CLIPTextEncode` ★核心
- `SetNode`
- `CR Text Concatenate`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Text Concatenate`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageFromBatch`
- `SetNode`
- `easy showAnything`
- `ImageBatchMulti`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Int`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `GetNode`
- `WanImageToVideo`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `easy showAnything`
- `GetNode`
- `CLIPVisionLoader`
- `Fast Groups Muter (rgthree)`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `easy forLoopEnd`
- `Note`
- `Note`
- `LoadImageListFromDir //Inspire`
- `easy forLoopStart`
- `WanImageToVideo`
- `WanMoeKSampler` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `ImageResizeKJv2`
- `MathExpression|pysssss`
- `LoadImage`
- `SetNode`
- `GetNode`
- `easy forLoopStart`
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `CR Seed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `SetNode`
- `VRAM_Debug`
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ProductInfoBuilder`
- `SoraPromptFromProduct`

## 关键参数

- `seed` = `1`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `uni_pc`

## 知识

覆盖率 **44%**（64/145）

**有卡**：`Int`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`wanBlockSwap`、`CLIPVisionEncode`、`MathExpression|pysssss`、`WanMoeKSampler`、`easy forLoopEnd`、`GetImageRangeFromBatch`、`ImageScaleBy`、`VAEDecode`、`GetImageSizeAndCount`、`RIFE VFI`、`easy cleanGpuUsed`、`easy promptLine`、`CLIPTextEncode`、`CR Text Concatenate`、`ImageFromBatch`、`ImageBatchMulti`、`INTConstant`、`LoraLoaderModelOnly`、`WanImageToVideo`、`ImageResizeKJv2`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`LoadImageListFromDir //Inspire`、`easy forLoopStart`、`LoadImage`、`CR Seed`、`UNETLoader`、`VHS_VideoCombine`、`VRAM_Debug`、`ProductInfoBuilder`、`SoraPromptFromProduct`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
