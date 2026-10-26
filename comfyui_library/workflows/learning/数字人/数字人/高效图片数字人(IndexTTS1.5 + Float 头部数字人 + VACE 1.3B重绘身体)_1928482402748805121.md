---
key: 数字人/数字人/高效图片数字人(IndexTTS1.5 + Float 头部数字人 + VACE 1.3B重绘身体)_1928482402748805121.json
name: 高效图片数字人(IndexTTS1.5 + Float 头部数字人 + VACE 1.3B重绘身体)_1928482402748805121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/高效图片数字人(IndexTTS1.5 + Float 头部数字人 + VACE 1.3B重绘身体)_1928482402748805121.json
hash: 1a92c125bebbe494
coverage: 0.73
learned_at: 2026-10-26 02:06:05
nodes: [Uncrop (mtb), GetImageSize+, ImageResize+, WanVideoExperimentalArgs, GetNode, GetNode, ImageComposite+, Reroute, APersonMaskGenerator, LayerUtility: ColorImage V2, LayerUtility: ColorImage V2, Split Bbox (mtb), ImageCompositeMaskedWithSwitch, PreviewImage, Reroute, APersonMaskGenerator, MaskBoundingBox+, easy imageSize, PrimitiveFloat, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, Crop (mtb), ImageResize+, DisplayAny, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, TextInput_, DisplayAny, VHS_GetImageCount, Reroute, LayerUtility: ColorImage V2, VHS_GetImageCount, DisplayAny, ImageBatchGet, PreviewImage, VHS_VideoCombine, WanVideoVACEModelSelect, WanVideoModelLoader, SetNode, WanVideoVAELoader, SetNode, LoadWanVideoT5TextEncoder, SetNode, SetNode, WanVideoVACEEncode, GetNode, easy cleanGpuUsed, GetNode, GetNode, IndexTTSRun, JWImageResizeByLongerSide, PreviewImage, SetNode, WanVideoTextEncode, WanVideoDecode, RH_Captioner, WanVideoSLG, RepeatImageBatch, ImageConcatMulti, GetNode, LoadAudio, easy anythingIndexSwitch, INTConstant, LoadFloatModels, PrimitiveFloat, SetNode, FirstFrameSelector, PreviewImage, AudioCrop, FloatProcess, VHS_VideoCombine, DisplayAny, Reroute, INTConstant, DF_Logic_node, WanVideoContextOptions, GetImageSizeAndCount, WanVideoSampler, Reroute, Reroute, Reroute, SaveAudio, AudioCrop, SaveAudio, Display Any (rgthree), VHS_VideoCombine, WanVideoTeaCache, VHS_VideoCombine, VHS_VideoCombine, INTConstant, LoadAudio, MarkdownNote, MaskFastGrow, InvertMask, JWImageResizeByLongerSide, LoadImage, Reroute, Note Plus (mtb)]
patterns: []
missing: []
---

# 数字人/数字人/高效图片数字人(IndexTTS1.5 + Float 头部数字人 + VACE 1.3B重绘身体)_1928482402748805121.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/高效图片数字人(IndexTTS1.5 + Float 头部数字人 + VACE 1.3B重绘身体)_1928482402748805121.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（100 个）：
- `Uncrop (mtb)`
- `GetImageSize+`
- `ImageResize+`
- `WanVideoExperimentalArgs`
- `GetNode`
- `GetNode`
- `ImageComposite+`
- `Reroute`
- `APersonMaskGenerator`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ColorImage V2`
- `Split Bbox (mtb)`
- `ImageCompositeMaskedWithSwitch`
- `PreviewImage`
- `Reroute`
- `APersonMaskGenerator`
- `MaskBoundingBox+`
- `easy imageSize`
- `PrimitiveFloat`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Crop (mtb)`
- `ImageResize+`
- `DisplayAny`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `TextInput_`
- `DisplayAny`
- `VHS_GetImageCount`
- `Reroute`
- `LayerUtility: ColorImage V2`
- `VHS_GetImageCount`
- `DisplayAny`
- `ImageBatchGet`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `WanVideoVACEEncode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `IndexTTSRun`
- `JWImageResizeByLongerSide`
- `PreviewImage`
- `SetNode`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `RH_Captioner`
- `WanVideoSLG`
- `RepeatImageBatch`
- `ImageConcatMulti`
- `GetNode`
- `LoadAudio`
- `easy anythingIndexSwitch`
- `INTConstant`
- `LoadFloatModels`
- `PrimitiveFloat`
- `SetNode`
- `FirstFrameSelector`
- `PreviewImage`
- `AudioCrop`
- `FloatProcess`
- `VHS_VideoCombine`
- `DisplayAny`
- `Reroute`
- `INTConstant`
- `DF_Logic_node`
- `WanVideoContextOptions`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `SaveAudio`
- `AudioCrop`
- `SaveAudio`
- `Display Any (rgthree)`
- `VHS_VideoCombine`
- `WanVideoTeaCache`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `INTConstant`
- `LoadAudio`
- `MarkdownNote`
- `MaskFastGrow`
- `InvertMask`
- `JWImageResizeByLongerSide`
- `LoadImage`
- `Reroute`
- `Note Plus (mtb)`

## 知识

覆盖率 **73%**（73/100）

**有卡**：`Uncrop (mtb)`、`GetImageSize+`、`ImageResize+`、`WanVideoExperimentalArgs`、`ImageComposite+`、`APersonMaskGenerator`、`LayerUtility: ColorImage V2`、`Split Bbox (mtb)`、`ImageCompositeMaskedWithSwitch`、`MaskBoundingBox+`、`easy imageSize`、`MathExpression|pysssss`、`Crop (mtb)`、`DisplayAny`、`TextInput_`、`VHS_GetImageCount`、`ImageBatchGet`、`VHS_VideoCombine`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVACEEncode`、`easy cleanGpuUsed`、`IndexTTSRun`、`JWImageResizeByLongerSide`、`WanVideoTextEncode`、`WanVideoDecode`、`RH_Captioner`、`WanVideoSLG`、`RepeatImageBatch`、`ImageConcatMulti`、`LoadAudio`、`easy anythingIndexSwitch`、`INTConstant`、`LoadFloatModels`、`FirstFrameSelector`、`AudioCrop`、`FloatProcess`、`DF_Logic_node`、`WanVideoContextOptions`、`GetImageSizeAndCount`、`WanVideoSampler`、`SaveAudio`、`Display Any (rgthree)`、`WanVideoTeaCache`、`MaskFastGrow`、`InvertMask`、`LoadImage`、`Note Plus (mtb)`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、GetImageSizeAndCount
