---
key: 图片生成/文生图/ControlNet-Union-Pro-2.0最新Flux多合一CN控制_1913100134115409921.json
name: ControlNet-Union-Pro-2.0最新Flux多合一CN控制_1913100134115409921.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ControlNet-Union-Pro-2.0最新Flux多合一CN控制_1913100134115409921.json
hash: 1c926c8397285146
coverage: 0.810811
learned_at: 2026-10-07 19:46:13
nodes: [BasicGuider, RandomNoise, KSamplerSelect, BasicScheduler, easy cleanGpuUsed, ControlNetLoader, DualCLIPLoader, VAELoader, SaveImage, VAEDecode, SaveImage, PreviewImage, UNETLoader, CLIPTextEncode, CLIPTextEncode, FluxGuidance, SamplerCustomAdvanced, Text Concatenate, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, ImageConcanate, ImageConcanate, ShowText|pysssss, LoadImage, LoraLoaderModelOnly, AIO_Preprocessor, SetUnionControlNetType, Note, LoadImage, DownloadAndLoadFlorence2Model, Florence2Run, Text Multiline, RH_Captioner, ControlNetApplyAdvanced, ApplyFBCacheOnModel, VAEEncode, RepeatLatentBatch]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Concatenate, Text Multiline, easy cleanGpuUsed]
parameters: {"controlnet_strength": 0.8000000000000002}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/ControlNet-Union-Pro-2.0最新Flux多合一CN控制_1913100134115409921.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1913100134115409921.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `easy cleanGpuUsed`
- `ControlNetLoader`
- `DualCLIPLoader`
- `VAELoader`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `Text Concatenate`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcanate`
- `ImageConcanate`
- `ShowText|pysssss`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `Note`
- `LoadImage`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `Text Multiline`
- `RH_Captioner`
- `ControlNetApplyAdvanced` ★核心
- `ApplyFBCacheOnModel`
- `VAEEncode` ★核心
- `RepeatLatentBatch`

## 关键参数

- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **81%**（30/37）

**有卡**：`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`ControlNetLoader`、`DualCLIPLoader`、`VAELoader`、`SaveImage`、`VAEDecode`、`UNETLoader`、`CLIPTextEncode`、`FluxGuidance`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`ImageConcanate`、`LoadImage`、`AIO_Preprocessor`、`SetUnionControlNetType`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`RH_Captioner`、`ControlNetApplyAdvanced`、`ApplyFBCacheOnModel`、`VAEEncode`、`RepeatLatentBatch`

**缺卡**（4）：`LayerUtility: ImageScaleByAspectRatio V2`、`Text Concatenate`、`Text Multiline`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
