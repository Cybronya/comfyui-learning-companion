---
key: 平台全量/PosterCraft海报封面生成+自动修改文字为中文-Calligrapher_1948677558505209857.json
name: PosterCraft海报封面生成+自动修改文字为中文-Calligrapher_1948677558505209857
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/PosterCraft海报封面生成+自动修改文字为中文-Calligrapher_1948677558505209857.json
hash: e8d78c1e19303062
coverage: 0.927711
learned_at: 2026-11-14 00:48:32
nodes: [SaveImage, LayerUtility: PurgeVRAM V2, CR Text Concatenate, LayerUtility: PurgeVRAM V2, LoadImage, CR Prompt Text, CalligrapherBlockSwap, ImageResizeKJ, PreviewImage, MaskToImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, ImageConcanate, SaveImage, SaveImage, VAELoader, ReferenceLatent, CR Prompt Text, SaveImage, SaveImage, JWInteger, GroupExecutorSingle, PreviewImage, PMRF, SaveImage, PreviewImage, LayerUtility: PurgeVRAM, ImageResizeKJ, CalligrapherImageProcesssor, Reroute, easy showAnything, RH_Translator, CR Prompt Text, ttN concat, GroupExecutorSingle, CalligrapherSampler, LayerUtility: PurgeVRAM, GrowMaskWithBlur, RunningHub PosterCraft Pipeline, RH_Prompter, JWInteger, JWInteger, GroupExecutorSender, GroupExecutorSingle, RH_Translator, PDIMAGE_LongerSize, TeaCache, ConditioningZeroOut, LoraLoaderModelOnly, FluxKontextImageScale, DualCLIPLoader, CLIPTextEncode, KSampler, FluxGuidance, VAEDecode, LayerUtility: PurgeVRAM V2, RHHiddenNodes, UnetLoaderGGUF, CalligrapherModelLoader, CalligrapherLora, LayerUtility: PurgeVRAM V2, FluxGuidance, ReferenceLatent, FluxKontextImageScale, ConditioningZeroOut, VAEEncode, KSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, VAEDecode, RunningHub PosterCraft Sampler, Reroute, DualCLIPLoader, VAELoader, ImageConcanate, CR Prompt Text, VAEEncode, LayerUtility: PurgeVRAM, PMRF, PDIMAGE_LongerSize, RHHiddenNodes]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 62891064435085, "steps": 20}
---

# 平台全量/PosterCraft海报封面生成+自动修改文字为中文-Calligrapher_1948677558505209857.json

> 来源文件 `comfyui_library/workflows/平台全量/PosterCraft海报封面生成+自动修改文字为中文-Calligrapher_1948677558505209857.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `SaveImage`
- `LayerUtility: PurgeVRAM V2`
- `CR Text Concatenate`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `CR Prompt Text`
- `CalligrapherBlockSwap`
- `ImageResizeKJ`
- `PreviewImage`
- `MaskToImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `ImageConcanate`
- `SaveImage`
- `SaveImage`
- `VAELoader`
- `ReferenceLatent`
- `CR Prompt Text`
- `SaveImage`
- `SaveImage`
- `JWInteger`
- `GroupExecutorSingle`
- `PreviewImage`
- `PMRF`
- `SaveImage`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `ImageResizeKJ`
- `CalligrapherImageProcesssor`
- `Reroute`
- `easy showAnything`
- `RH_Translator`
- `CR Prompt Text`
- `ttN concat`
- `GroupExecutorSingle`
- `CalligrapherSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `GrowMaskWithBlur`
- `RunningHub PosterCraft Pipeline`
- `RH_Prompter`
- `JWInteger`
- `JWInteger`
- `GroupExecutorSender`
- `GroupExecutorSingle`
- `RH_Translator`
- `PDIMAGE_LongerSize`
- `TeaCache`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `FluxKontextImageScale`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `FluxGuidance`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `RHHiddenNodes`
- `UnetLoaderGGUF` ★核心
- `CalligrapherModelLoader`
- `CalligrapherLora`
- `LayerUtility: PurgeVRAM V2`
- `FluxGuidance`
- `ReferenceLatent`
- `FluxKontextImageScale`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `VAEDecode` ★核心
- `RunningHub PosterCraft Sampler` ★核心
- `Reroute`
- `DualCLIPLoader`
- `VAELoader`
- `ImageConcanate`
- `CR Prompt Text`
- `VAEEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `PMRF`
- `PDIMAGE_LongerSize`
- `RHHiddenNodes`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `62891064435085`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（77/83）

**有卡**：`SaveImage`、`LayerUtility: PurgeVRAM V2`、`CR Text Concatenate`、`LoadImage`、`CR Prompt Text`、`CalligrapherBlockSwap`、`ImageResizeKJ`、`MaskToImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`VAELoader`、`ReferenceLatent`、`JWInteger`、`GroupExecutorSingle`、`PMRF`、`LayerUtility: PurgeVRAM`、`CalligrapherImageProcesssor`、`RH_Translator`、`ttN concat`、`CalligrapherSampler`、`GrowMaskWithBlur`、`RunningHub PosterCraft Pipeline`、`RH_Prompter`、`GroupExecutorSender`、`PDIMAGE_LongerSize`、`TeaCache`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`FluxKontextImageScale`、`DualCLIPLoader`、`CLIPTextEncode`、`KSampler`、`FluxGuidance`、`VAEDecode`、`RHHiddenNodes`、`UnetLoaderGGUF`、`CalligrapherModelLoader`、`CalligrapherLora`、`VAEEncode`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`RunningHub PosterCraft Sampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LayerUtility: ImageScaleByAspectRatio V2、LoadImage
