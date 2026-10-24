---
key: 图片生成/图生图/Flux.2-Kelin服装材质花纹替换_2060199934435094530.json
name: Flux.2-Kelin服装材质花纹替换_2060199934435094530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2-Kelin服装材质花纹替换_2060199934435094530.json
hash: 155f6a43fb209ff6
coverage: 0.866667
learned_at: 2026-10-23 10:58:50
nodes: [LayerUtility: PurgeVRAM V2, UNETLoader, easy imageSizeByLongerSide, ZML_ArithmeticComparison, Image Input Switch, UpscaleModelLoader, ImageUpscaleWithModel, UpscaleModelLoader, Image Input Switch, ImageUpscaleWithModel, SetNode, easy int, LayerUtility: ImageScaleByAspectRatio V2, ImageUpscaleWithModel, UpscaleModelLoader, SetNode, Flux2KleinModelConfig_EditUtils, Flux2KleinConfigPreparer_EditUtils, GetNode, CLIPLoader, VAELoader, GetNode, Flux2KleinConfigPreparer_EditUtils, CLIPTextEncode, VAEDecode, ReferenceLatent, Flux2KleinOutputExtractor_EditUtils, LoraLoaderModelOnly, CFGNorm, ModelSamplingAuraFlow, KSampler, CropWithPadInfo_EditUtils, Image Comparer (rgthree), LoadImage, SaveImage, ZML_ArithmeticComparison, easy int, easy imageSizeByLongerSide, LayerUtility: ImageScaleByAspectRatio V2, Int, LoadImage, Note, CR Prompt Text, EditTextEncode_EditUtils, ttN concat]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 462406021376063, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux.2-Kelin服装材质花纹替换_2060199934435094530.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2-Kelin服装材质花纹替换_2060199934435094530.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `LayerUtility: PurgeVRAM V2`
- `UNETLoader` ★核心
- `easy imageSizeByLongerSide`
- `ZML_ArithmeticComparison`
- `Image Input Switch`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `Image Input Switch`
- `ImageUpscaleWithModel`
- `SetNode`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `SetNode`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `GetNode`
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `Flux2KleinConfigPreparer_EditUtils`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `Flux2KleinOutputExtractor_EditUtils`
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `CropWithPadInfo_EditUtils`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `ZML_ArithmeticComparison`
- `easy int`
- `easy imageSizeByLongerSide`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `LoadImage`
- `Note`
- `CR Prompt Text`
- `EditTextEncode_EditUtils`
- `ttN concat`

## 关键参数

- `seed` = `462406021376063`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **87%**（39/45）

**有卡**：`LayerUtility: PurgeVRAM V2`、`UNETLoader`、`easy imageSizeByLongerSide`、`ZML_ArithmeticComparison`、`Image Input Switch`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`Flux2KleinModelConfig_EditUtils`、`Flux2KleinConfigPreparer_EditUtils`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`ReferenceLatent`、`Flux2KleinOutputExtractor_EditUtils`、`LoraLoaderModelOnly`、`CFGNorm`、`ModelSamplingAuraFlow`、`KSampler`、`CropWithPadInfo_EditUtils`、`LoadImage`、`SaveImage`、`Int`、`CR Prompt Text`、`EditTextEncode_EditUtils`、`ttN concat`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
