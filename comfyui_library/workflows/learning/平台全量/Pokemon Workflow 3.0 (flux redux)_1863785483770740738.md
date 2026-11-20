---
key: 平台全量/Pokemon Workflow 3.0 (flux redux)_1863785483770740738.json
name: Pokemon Workflow 3.0 (flux redux)_1863785483770740738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Pokemon Workflow 3.0 (flux redux)_1863785483770740738.json
hash: 873ba765a6cc58b7
coverage: 0.825
learned_at: 2026-11-14 00:48:27
nodes: [ShowText|pysssss, ShowText|pysssss, CR Text, CR Text, CR Text, Florence2Run, DownloadAndLoadFlorence2Model, Florence2Run, LayerUtility: TextJoin, LayerUtility: TextJoin, LayerUtility: TextJoin, CLIPVisionLoader, CLIPTextEncode, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, EmptySD3LatentImage, ModelSamplingFlux, SDXLAspectRatioSelector, Note, Note, Note, Replace Text _O, LoadImage, CLIPVisionEncode, StyleModelLoader, CLIPVisionEncode, StyleModelApply, FluxGuidance, StyleModelApply, LoadImage, LayerUtility: TextJoin, ShowText|pysssss, OllamaGenerate, CheckpointLoaderSimple, VAEDecode, SaveImage, PreviewImage]
patterns: []
missing: []
parameters: {"checkpoint": "flux.1_dev_8x8_e4m3fn-marduk191.safetensors"}
---

# 平台全量/Pokemon Workflow 3.0 (flux redux)_1863785483770740738.json

> 来源文件 `comfyui_library/workflows/平台全量/Pokemon Workflow 3.0 (flux redux)_1863785483770740738.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `ShowText|pysssss`
- `ShowText|pysssss`
- `CR Text`
- `CR Text`
- `CR Text`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `LayerUtility: TextJoin`
- `LayerUtility: TextJoin`
- `LayerUtility: TextJoin`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `EmptySD3LatentImage`
- `ModelSamplingFlux`
- `SDXLAspectRatioSelector`
- `Note`
- `Note`
- `Note`
- `Replace Text _O`
- `LoadImage`
- `CLIPVisionEncode`
- `StyleModelLoader`
- `CLIPVisionEncode`
- `StyleModelApply`
- `FluxGuidance`
- `StyleModelApply`
- `LoadImage`
- `LayerUtility: TextJoin`
- `ShowText|pysssss`
- `OllamaGenerate`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`

## 关键参数

- `checkpoint` = `flux.1_dev_8x8_e4m3fn-marduk191.safetensors`

## 知识

覆盖率 **82%**（33/40）

**有卡**：`CR Text`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`LayerUtility: TextJoin`、`CLIPVisionLoader`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`SDXLAspectRatioSelector`、`Replace Text _O`、`LoadImage`、`CLIPVisionEncode`、`StyleModelLoader`、`StyleModelApply`、`FluxGuidance`、`OllamaGenerate`、`CheckpointLoaderSimple`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、CLIPVisionEncode
