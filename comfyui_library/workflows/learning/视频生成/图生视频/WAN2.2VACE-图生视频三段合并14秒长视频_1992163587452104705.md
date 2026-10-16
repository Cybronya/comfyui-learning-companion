---
key: 视频生成/图生视频/WAN2.2VACE-图生视频三段合并14秒长视频_1992163587452104705.json
name: WAN2.2VACE-图生视频三段合并14秒长视频_1992163587452104705.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1992163587452104705.json
hash: cf4988681dc28b8f
coverage: 0.41844
learned_at: 2026-10-15 22:33:15
nodes: [GetNode, GetNode, VAELoader, SetNode, SetNode, SetNode, CLIPLoader, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanMoeKSampler, DiffusionModelSelector, ModelSamplingSD3, ModelSamplingSD3, GetNode, GetNode, GetNode, WanVideoVACEStartToEndFrame, GetNode, WanVaceToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, WanMoeKSampler, MathExpression|pysssss, GetNode, GetImageSizeAndCount, GetNode, GetImageRangeFromBatch, GetNode, GetNode, GetNode, GetNode, WanVideoVACEStartToEndFrame, GetNode, WanVaceToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, WanMoeKSampler, MathExpression|pysssss, GetNode, GetImageSizeAndCount, GetImageRangeFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetImageRangeFromBatch, GetImageRangeFromBatch, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, VAEDecode, ImageBatchMulti, ImageFromBatch+, SetNode, SetNode, SetNode, GetNode, ImageFromBatch+, VAEDecode, SetNode, SetNode, CreateVideo, SetNode, GetNode, ImageFromBatch+, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, CreateVideo, SetNode, GetNode, CreateVideo, VAEDecode, LoadImage, WanVaceToVideo, WanVideoVACEStartToEndFrame, ImageResizeKJv2, Text Multiline, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, DiffusionModelSelector, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, INTConstant, INTConstant, INTConstant, INTConstant, SetNode, INTConstant, SaveVideo, SaveVideo, SaveVideo, SaveVideo, SaveImage, SaveImage, SaveImage, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, CreateVideo, SetNode, MarkdownNote, Text Multiline, Text Multiline]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2VACE-图生视频三段合并14秒长视频_1992163587452104705.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992163587452104705.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（141 个）：
- `GetNode`
- `GetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanMoeKSampler` ★核心
- `DiffusionModelSelector`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `WanVaceToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanMoeKSampler` ★核心
- `MathExpression|pysssss`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `WanVaceToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanMoeKSampler` ★核心
- `MathExpression|pysssss`
- `GetNode`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `ImageBatchMulti`
- `ImageFromBatch+`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageFromBatch+`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `CreateVideo`
- `SetNode`
- `GetNode`
- `ImageFromBatch+`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `CreateVideo`
- `SetNode`
- `GetNode`
- `CreateVideo`
- `VAEDecode` ★核心
- `LoadImage`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `ImageResizeKJv2`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `DiffusionModelSelector`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SaveVideo`
- `SaveVideo`
- `SaveVideo`
- `SaveVideo`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CreateVideo`
- `SetNode`
- `MarkdownNote`
- `Text Multiline`
- `Text Multiline`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **42%**（59/141）

**有卡**：`VAELoader`、`CLIPLoader`、`WanMoeKSampler`、`DiffusionModelSelector`、`ModelSamplingSD3`、`WanVideoVACEStartToEndFrame`、`WanVaceToVideo`、`MathExpression|pysssss`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`LoraLoaderModelOnly`、`VAEDecode`、`ImageBatchMulti`、`ImageFromBatch+`、`CreateVideo`、`LoadImage`、`ImageResizeKJv2`、`Text Multiline`、`CLIPTextEncode`、`DiffusionModelLoaderKJ`、`INTConstant`、`SaveVideo`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、WanMoeKSampler、GetImageSizeAndCount
