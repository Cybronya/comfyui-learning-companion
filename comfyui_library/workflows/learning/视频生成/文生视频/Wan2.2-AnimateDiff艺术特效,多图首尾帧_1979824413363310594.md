---
key: 视频生成/文生视频/Wan2.2-AnimateDiff艺术特效,多图首尾帧_1979824413363310594.json
name: Wan2.2-AnimateDiff艺术特效,多图首尾帧_1979824413363310594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-AnimateDiff艺术特效,多图首尾帧_1979824413363310594.json
hash: faea5f3ec8a7e7fb
coverage: 0.788889
learned_at: 2026-10-11 02:45:02
nodes: [Label (rgthree), Label (rgthree), FILM VFI, GetImageRangeFromBatch, GetImageRangeFromBatch, INTConstant, INTConstant, WanVideoSampler, WanVideoSampler, VRAM_Debug, VRAM_Debug, WanVideoModelLoader, VRAM_Debug, WanVideoApplyNAG, VRAM_Debug, WanVideoDecode, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), WanVideoSLG, WanVideoSLG, MathExpression|pysssss, INTConstant, WanVideoSLG, INTConstant, WanVideoSetBlockSwap, WanVideoDecode, GetImageSizeAndCount, GetImageSizeAndCount, easy showAnything, VRAM_Debug, VRAM_Debug, MathExpression|pysssss, WanVideoVAELoader, WanVideoSampler, VRAM_Debug, GetImageSizeAndCount, WanVideoTextEncodeCached, ImageBatch, ImageBatch, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoTextEncodeCached, easy showAnything, Note, ImageBatch, RH_Captioner, RH_Captioner, ImageBatch, WanVideoBlockSwap, LoadImage, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoLoraSelect, easy showAnything, easy showAnything, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoImageToVideoEncode, WanVideoApplyNAG, WanVideoTextEncodeCached, ImageBatch, ImageFromBatch+, WanVideoImageToVideoEncode, ImageResizeKJv2, ImageResizeKJv2, FILM VFI, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, VHS_VideoCombine, GetImageRangeFromBatch, GetImageRangeFromBatch, ImageBatch, ImageResizeKJv2, LoadImage, LoadImage, LoadImage, WanVideoSampler, ColorMatchToReference, FILM VFI, HDR Effects (SuperBeasts.AI), VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: [FILM VFI, FILM VFI, FILM VFI, HDR Effects (SuperBeasts.AI), ImageFromBatch+, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), MathExpression|pysssss, MathExpression|pysssss]
discoveries: [次要节点 `FILM VFI` 知识库中没有该节点类型的任何知识, 次要节点 `FILM VFI` 知识库中没有该节点类型的任何知识, 次要节点 `FILM VFI` 知识库中没有该节点类型的任何知识, 次要节点 `HDR Effects (SuperBeasts.AI)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2-AnimateDiff艺术特效,多图首尾帧_1979824413363310594.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-AnimateDiff艺术特效,多图首尾帧_1979824413363310594.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（90 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `FILM VFI`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `INTConstant`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VRAM_Debug`
- `VRAM_Debug`
- `WanVideoModelLoader`
- `VRAM_Debug`
- `WanVideoApplyNAG`
- `VRAM_Debug`
- `WanVideoDecode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanVideoSLG`
- `WanVideoSLG`
- `MathExpression|pysssss`
- `INTConstant`
- `WanVideoSLG`
- `INTConstant`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `easy showAnything`
- `VRAM_Debug`
- `VRAM_Debug`
- `MathExpression|pysssss`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `VRAM_Debug`
- `GetImageSizeAndCount`
- `WanVideoTextEncodeCached`
- `ImageBatch`
- `ImageBatch`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `easy showAnything`
- `Note`
- `ImageBatch`
- `RH_Captioner`
- `RH_Captioner`
- `ImageBatch`
- `WanVideoBlockSwap`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `easy showAnything`
- `easy showAnything`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoEncode`
- `WanVideoApplyNAG`
- `WanVideoTextEncodeCached`
- `ImageBatch`
- `ImageFromBatch+`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `FILM VFI`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `ImageBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanVideoSampler` ★核心
- `ColorMatchToReference`
- `FILM VFI`
- `HDR Effects (SuperBeasts.AI)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **79%**（71/90）

**有卡**：`GetImageRangeFromBatch`、`INTConstant`、`WanVideoSampler`、`VRAM_Debug`、`WanVideoModelLoader`、`WanVideoApplyNAG`、`WanVideoDecode`、`WanVideoSLG`、`WanVideoSetBlockSwap`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`ImageBatch`、`WanVideoSetLoRAs`、`RH_Captioner`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`VHS_VideoCombine`、`ColorMatchToReference`

**缺卡**（14）：`FILM VFI`、`FILM VFI`、`FILM VFI`、`HDR Effects (SuperBeasts.AI)`、`ImageFromBatch+`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`MathExpression|pysssss`、`MathExpression|pysssss`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `FILM VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `FILM VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `FILM VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `HDR Effects (SuperBeasts.AI)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
