---
key: 图片生成/文生图/ControlNet-Union-Pro-2.0最新Flux多合一CN控制_1913100134115409921.json
name: ControlNet-Union-Pro-2.0最新Flux多合一CN控制_1913100134115409921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ControlNet-Union-Pro-2.0最新Flux多合一CN控制_1913100134115409921.json
hash: 1c926c8397285146
coverage: 0.810811
learned_at: 2026-10-10 21:27:02
nodes: [BasicGuider, RandomNoise, KSamplerSelect, BasicScheduler, easy cleanGpuUsed, ControlNetLoader, DualCLIPLoader, VAELoader, SaveImage, VAEDecode, SaveImage, PreviewImage, UNETLoader, CLIPTextEncode, CLIPTextEncode, FluxGuidance, SamplerCustomAdvanced, Text Concatenate, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, ImageConcanate, ImageConcanate, ShowText|pysssss, LoadImage, LoraLoaderModelOnly, AIO_Preprocessor, SetUnionControlNetType, Note, LoadImage, DownloadAndLoadFlorence2Model, Florence2Run, Text Multiline, RH_Captioner, ControlNetApplyAdvanced, ApplyFBCacheOnModel, VAEEncode, RepeatLatentBatch]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Concatenate, Text Multiline, easy cleanGpuUsed]
parameters: {"controlnet_strength": 0.8000000000000002}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/ControlNet-Union-Pro-2.0最新Flux多合一CN控制_1913100134115409921.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ControlNet-Union-Pro-2.0最新Flux多合一CN控制_1913100134115409921.json`

## 结构

**节点**（37 个）：
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect`
- `BasicScheduler`
- `easy cleanGpuUsed`
- `ControlNetLoader`
- `DualCLIPLoader`
- `VAELoader`
- `SaveImage`
- `VAEDecode`
- `SaveImage`
- `PreviewImage`
- `UNETLoader`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `FluxGuidance`
- `SamplerCustomAdvanced`
- `Text Concatenate`
- `LoraLoaderModelOnly`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcanate`
- `ImageConcanate`
- `ShowText|pysssss`
- `LoadImage`
- `LoraLoaderModelOnly`
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `Note`
- `LoadImage`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `Text Multiline`
- `RH_Captioner`
- `ControlNetApplyAdvanced`
- `ApplyFBCacheOnModel`
- `VAEEncode`
- `RepeatLatentBatch`

## 关键参数

- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **81%**（30/37）

**有卡**：`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`easy cleanGpuUsed`、`ControlNetLoader`、`DualCLIPLoader`、`VAELoader`、`SaveImage`、`VAEDecode`、`PreviewImage`、`UNETLoader`、`CLIPTextEncode`、`FluxGuidance`、`SamplerCustomAdvanced`、`Text Concatenate`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`ShowText|pysssss`、`LoadImage`、`AIO_Preprocessor`、`SetUnionControlNetType`、`Note`、`DownloadAndLoadFlorence2Model`

**缺卡**（4）：`LayerUtility: ImageScaleByAspectRatio V2`、`Text Concatenate`、`Text Multiline`、`easy cleanGpuUsed`

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
