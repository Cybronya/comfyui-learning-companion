---
key: 平台全量/DW+LineArt+IPAdapterFaceID+面部细化-真人转日漫_1930881537016049666.json
name: DW+LineArt+IPAdapterFaceID+面部细化-真人转日漫_1930881537016049666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/DW+LineArt+IPAdapterFaceID+面部细化-真人转日漫_1930881537016049666.json
hash: 2f33bc44e96aa165
coverage: 0.884615
learned_at: 2026-11-14 00:23:12
nodes: [SaveImage, WD14Tagger|pysssss, Control Net Stacker, ControlNetLoader, AIO_Preprocessor, PreviewImage, Control Net Stacker, PreviewImage, AIO_Preprocessor, ControlNetLoader, LayerUtility: ImageScaleByAspectRatio V2, ImageConcanate, MaskToImage, FaceDetailer, VAEEncode, PreviewImage, UltralyticsDetectorProvider, SAMLoader, CLIPVisionLoader, IPAdapterInsightFaceLoader, LoadImage, LoadImage, IPAdapterModelLoader, KSampler (Efficient), Efficient Loader, IPAdapterFaceID]
patterns: []
missing: []
parameters: {"cfg": 7, "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 478129594458028, "steps": 25}
---

# 平台全量/DW+LineArt+IPAdapterFaceID+面部细化-真人转日漫_1930881537016049666.json

> 来源文件 `comfyui_library/workflows/平台全量/DW+LineArt+IPAdapterFaceID+面部细化-真人转日漫_1930881537016049666.json`

## 结构

**生成流程**：Model → Encode → Control → Sampling → Process → Output → Other

**节点**（26 个）：
- `SaveImage`
- `WD14Tagger|pysssss`
- `Control Net Stacker`
- `ControlNetLoader`
- `AIO_Preprocessor`
- `PreviewImage`
- `Control Net Stacker`
- `PreviewImage`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcanate`
- `MaskToImage`
- `FaceDetailer`
- `VAEEncode` ★核心
- `PreviewImage`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `CLIPVisionLoader`
- `IPAdapterInsightFaceLoader`
- `LoadImage`
- `LoadImage`
- `IPAdapterModelLoader`
- `KSampler (Efficient)` ★核心
- `Efficient Loader`
- `IPAdapterFaceID`

## 关键参数

- `seed` = `478129594458028`
- `steps` = `25`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`SaveImage`、`WD14Tagger|pysssss`、`Control Net Stacker`、`ControlNetLoader`、`AIO_Preprocessor`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`MaskToImage`、`FaceDetailer`、`VAEEncode`、`UltralyticsDetectorProvider`、`SAMLoader`、`CLIPVisionLoader`、`IPAdapterInsightFaceLoader`、`LoadImage`、`IPAdapterModelLoader`、`KSampler (Efficient)`、`Efficient Loader`、`IPAdapterFaceID`

**用到的条目**：LoadImage、Control Net Stacker、ControlNetLoader、KSampler (Efficient)、VAEEncode、IPAdapterFaceID、IPAdapterInsightFaceLoader、IPAdapterModelLoader
