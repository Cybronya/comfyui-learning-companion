---
key: 图片生成/文生图/lora训练工具之四：一张图生成人像lora数据集工作流V1.1_1954537986593583106.json
name: lora训练工具之四：一张图生成人像lora数据集工作流V1.1_1954537986593583106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/lora训练工具之四：一张图生成人像lora数据集工作流V1.1_1954537986593583106.json
hash: ac984d1c055b83a3
coverage: 0.666667
learned_at: 2026-10-15 22:27:51
nodes: [MatAnyoneVideoMatting, GroundingDinoSAMSegment (segment anything), SAMModelLoader (segment anything), GroundingDinoModelLoader (segment anything), MaskPreview+, Reroute, MaskToImage, GetImagesFromBatchIndexed, TransparentBGSession+, ImageRemoveBackground+, LayerUtility: PurgeVRAM, CLIPVisionLoader, WanImageToVideo, PrimitiveNode, Reroute (rgthree), Reroute (rgthree), PathchSageAttentionKJ, Reroute (rgthree), EmptyHunyuanLatentVideo, KSamplerSelect, BasicScheduler, CFGGuider, VAEDecodeTiled, Reroute (rgthree), VAEDecodeTiled, Reroute (rgthree), Reroute (rgthree), MathExpression|pysssss, SplitSigmas, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, ImageScale, Reroute (rgthree), Reroute (rgthree), Reroute (rgthree), Reroute (rgthree), Reroute (rgthree), Reroute (rgthree), Reroute (rgthree), Reroute (rgthree), GetLatentRangeFromBatch, Reroute (rgthree), ScheduledCFGGuidance, Reroute (rgthree), MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, Reroute, Reroute, ImageUpscaleWithModel, UpscaleModelLoader, SamplerCustomAdvanced, SamplerCustomAdvanced, VHS_VideoCombine, RandomNoise, CLIPLoader, VAELoader, VHS_VideoCombine, MaskPreview+, PreviewImage, LoraLoaderModelOnly, VHS_VideoCombine, RHHiddenNodes, UnetLoaderGGUF, VHS_VideoCombine, PreviewImage, Image Crop Face, LoadImage, PrimitiveNode, Note]
patterns: []
missing: []
---

# 图片生成/文生图/lora训练工具之四：一张图生成人像lora数据集工作流V1.1_1954537986593583106.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/lora训练工具之四：一张图生成人像lora数据集工作流V1.1_1954537986593583106.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `MatAnyoneVideoMatting`
- `GroundingDinoSAMSegment (segment anything)`
- `SAMModelLoader (segment anything)`
- `GroundingDinoModelLoader (segment anything)`
- `MaskPreview+`
- `Reroute`
- `MaskToImage`
- `GetImagesFromBatchIndexed`
- `TransparentBGSession+`
- `ImageRemoveBackground+`
- `LayerUtility: PurgeVRAM`
- `CLIPVisionLoader`
- `WanImageToVideo`
- `PrimitiveNode`
- `Reroute (rgthree)`
- `Reroute (rgthree)`
- `PathchSageAttentionKJ`
- `Reroute (rgthree)`
- `EmptyHunyuanLatentVideo`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `Reroute (rgthree)`
- `VAEDecodeTiled` ★核心
- `Reroute (rgthree)`
- `Reroute (rgthree)`
- `MathExpression|pysssss`
- `SplitSigmas`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `ImageScale`
- `Reroute (rgthree)`
- `Reroute (rgthree)`
- `Reroute (rgthree)`
- `Reroute (rgthree)`
- `Reroute (rgthree)`
- `Reroute (rgthree)`
- `Reroute (rgthree)`
- `Reroute (rgthree)`
- `GetLatentRangeFromBatch`
- `Reroute (rgthree)`
- `ScheduledCFGGuidance`
- `Reroute (rgthree)`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Reroute`
- `Reroute`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `RandomNoise`
- `CLIPLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `MaskPreview+`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `UnetLoaderGGUF` ★核心
- `VHS_VideoCombine`
- `PreviewImage`
- `Image Crop Face`
- `LoadImage`
- `PrimitiveNode`
- `Note`

## 知识

覆盖率 **67%**（48/72）

**有卡**：`MatAnyoneVideoMatting`、`GroundingDinoSAMSegment (segment anything)`、`SAMModelLoader (segment anything)`、`GroundingDinoModelLoader (segment anything)`、`MaskPreview+`、`MaskToImage`、`GetImagesFromBatchIndexed`、`TransparentBGSession+`、`ImageRemoveBackground+`、`LayerUtility: PurgeVRAM`、`CLIPVisionLoader`、`WanImageToVideo`、`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`KSamplerSelect`、`BasicScheduler`、`CFGGuider`、`VAEDecodeTiled`、`MathExpression|pysssss`、`SplitSigmas`、`CLIPTextEncode`、`CLIPVisionEncode`、`ImageScale`、`GetLatentRangeFromBatch`、`ScheduledCFGGuidance`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`RHHiddenNodes`、`UnetLoaderGGUF`、`Image Crop Face`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
