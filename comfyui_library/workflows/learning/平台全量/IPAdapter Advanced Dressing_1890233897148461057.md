---
key: 平台全量/IPAdapter Advanced Dressing_1890233897148461057.json
name: IPAdapter Advanced Dressing_1890233897148461057
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/IPAdapter Advanced Dressing_1890233897148461057.json
hash: 9e582a36b4816859
coverage: 0.891304
learned_at: 2026-11-14 00:32:27
nodes: [IPAdapterUnifiedLoaderFaceID, VAEDecode, DWPreprocessor, UltralyticsDetectorProvider, IPAdapterEncoder, ShowText|pysssss, DiffControlNetLoader, CLIPTextEncode, WD14Tagger|pysssss, StringFunction|pysssss, PreviewImage, ControlNetApply, EmptyLatentImage, CLIPTextEncode, WD14Tagger|pysssss, LoadImage, CLIPTextEncode, Text List, Text List to Text, LoadImage, ShowText|pysssss, StringFunction|pysssss, String Literal, JWImageResizeByLongerSide, GetImageSize+, IPAdapterUnifiedLoader, CLIPSetLastLayer, WD14Tagger|pysssss, IPAdapterEncoder, IPAdapter, IPAdapterCombineEmbeds, IPAdapterEmbeds, KSampler //Inspire, CheckpointLoaderSimple, CheckpointLoaderSimple, Anything Everywhere3, LoadImage, IPAdapterEncoder, FreeU_V2, IPAdapterNoise, IPAdapterEncoder, LoadImage, LoadImage, SaveImage, FaceDetailer, PreviewImage]
patterns: [controlnet]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "checkpoint": "magmix_v10.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 512, "sampler_name": "dpmpp_sde", "scheduler": "AYS SD1", "seed": 887054014123268, "steps": 25, "width": 512}
---

# 平台全量/IPAdapter Advanced Dressing_1890233897148461057.json

> 来源文件 `comfyui_library/workflows/平台全量/IPAdapter Advanced Dressing_1890233897148461057.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `IPAdapterUnifiedLoaderFaceID`
- `VAEDecode` ★核心
- `DWPreprocessor`
- `UltralyticsDetectorProvider`
- `IPAdapterEncoder`
- `ShowText|pysssss`
- `DiffControlNetLoader`
- `CLIPTextEncode` ★核心
- `WD14Tagger|pysssss`
- `StringFunction|pysssss`
- `PreviewImage`
- `ControlNetApply` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `WD14Tagger|pysssss`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Text List`
- `Text List to Text`
- `LoadImage`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `String Literal`
- `JWImageResizeByLongerSide`
- `GetImageSize+`
- `IPAdapterUnifiedLoader`
- `CLIPSetLastLayer`
- `WD14Tagger|pysssss`
- `IPAdapterEncoder`
- `IPAdapter`
- `IPAdapterCombineEmbeds`
- `IPAdapterEmbeds`
- `KSampler //Inspire` ★核心
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `Anything Everywhere3`
- `LoadImage`
- `IPAdapterEncoder`
- `FreeU_V2`
- `IPAdapterNoise`
- `IPAdapterEncoder`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `FaceDetailer`
- `PreviewImage`

**识别到的模式**：controlnet

## 关键参数

- `controlnet_strength` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `887054014123268`
- `steps` = `25`
- `cfg` = `4`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `AYS SD1`
- `denoise` = `1`
- `checkpoint` = `magmix_v10.safetensors`

## 知识

覆盖率 **89%**（41/46）

**有卡**：`IPAdapterUnifiedLoaderFaceID`、`VAEDecode`、`DWPreprocessor`、`UltralyticsDetectorProvider`、`IPAdapterEncoder`、`DiffControlNetLoader`、`CLIPTextEncode`、`WD14Tagger|pysssss`、`StringFunction|pysssss`、`ControlNetApply`、`EmptyLatentImage`、`LoadImage`、`Text List`、`Text List to Text`、`String Literal`、`JWImageResizeByLongerSide`、`GetImageSize+`、`IPAdapterUnifiedLoader`、`CLIPSetLastLayer`、`IPAdapter`、`IPAdapterCombineEmbeds`、`IPAdapterEmbeds`、`KSampler //Inspire`、`CheckpointLoaderSimple`、`FreeU_V2`、`IPAdapterNoise`、`SaveImage`、`FaceDetailer`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApply、DiffControlNetLoader、KSampler //Inspire
