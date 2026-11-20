---
key: 平台全量/DiffBIR Super Resolution_1889566742438469634.json
name: DiffBIR Super Resolution_1889566742438469634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/DiffBIR Super Resolution_1889566742438469634.json
hash: 039dd50055b61f9d
coverage: 0.612903
learned_at: 2026-11-14 00:23:17
nodes: [easy imageSize, ImageScaleBy, Simple_load, GetNode, easy imageSize, CR Text Replace, SetNode, CLIPTextEncode, GetNode, FluxGuidance, Anything Everywhere, Anything Everywhere3, Image Comparer (rgthree), Image Comparer (rgthree), PlaySound|pysssss, GetNode, ConditioningZeroOut, SetNode, GetNode, GetNode, PlaySound|pysssss, ModelSamplingFlux, easy imageSwitch, SetNode, SetNode, GetNode, CLIPTextEncode, ConditioningZeroOut, FaceDetailer, easy seed, easy seed, SaveImage, PlaySound|pysssss, LoadImage, easy float, Fast Groups Bypasser (rgthree), Florence2Run, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), CR Image Input Switch, UltimateSDUpscaleCustomSample, Fast Bypasser (rgthree), DetailDaemonSamplerNode, BasicScheduler, DiffBIR_sample, Fast Groups Bypasser (rgthree), easy imageSize, Note, easy showAnything, DownloadAndLoadFlorence2Model, Anything Everywhere3, LoraLoaderModelOnly, UltralyticsDetectorProvider, VAELoader, DualCLIPLoader, UnetLoaderGGUF, LoraLoaderModelOnly, UpscaleModelLoader, KSamplerSelect, GetNode, Image Comparer (rgthree)]
patterns: []
missing: []
---

# 平台全量/DiffBIR Super Resolution_1889566742438469634.json

> 来源文件 `comfyui_library/workflows/平台全量/DiffBIR Super Resolution_1889566742438469634.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（62 个）：
- `easy imageSize`
- `ImageScaleBy`
- `Simple_load`
- `GetNode`
- `easy imageSize`
- `CR Text Replace`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `FluxGuidance`
- `Anything Everywhere`
- `Anything Everywhere3`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `PlaySound|pysssss`
- `GetNode`
- `ConditioningZeroOut`
- `SetNode`
- `GetNode`
- `GetNode`
- `PlaySound|pysssss`
- `ModelSamplingFlux`
- `easy imageSwitch`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FaceDetailer`
- `easy seed`
- `easy seed`
- `SaveImage`
- `PlaySound|pysssss`
- `LoadImage`
- `easy float`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CR Image Input Switch`
- `UltimateSDUpscaleCustomSample`
- `Fast Bypasser (rgthree)`
- `DetailDaemonSamplerNode` ★核心
- `BasicScheduler`
- `DiffBIR_sample`
- `Fast Groups Bypasser (rgthree)`
- `easy imageSize`
- `Note`
- `easy showAnything`
- `DownloadAndLoadFlorence2Model`
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `UltralyticsDetectorProvider`
- `VAELoader`
- `DualCLIPLoader`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `KSamplerSelect` ★核心
- `GetNode`
- `Image Comparer (rgthree)`

## 知识

覆盖率 **61%**（38/62）

**有卡**：`easy imageSize`、`ImageScaleBy`、`Simple_load`、`CR Text Replace`、`CLIPTextEncode`、`FluxGuidance`、`PlaySound|pysssss`、`ConditioningZeroOut`、`ModelSamplingFlux`、`easy imageSwitch`、`FaceDetailer`、`easy seed`、`SaveImage`、`LoadImage`、`easy float`、`Florence2Run`、`CR Image Input Switch`、`UltimateSDUpscaleCustomSample`、`Fast Bypasser (rgthree)`、`DetailDaemonSamplerNode`、`BasicScheduler`、`DiffBIR_sample`、`DownloadAndLoadFlorence2Model`、`LoraLoaderModelOnly`、`UltralyticsDetectorProvider`、`VAELoader`、`DualCLIPLoader`、`UnetLoaderGGUF`、`UpscaleModelLoader`、`KSamplerSelect`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、DetailDaemonSamplerNode、easy seed、FluxGuidance
