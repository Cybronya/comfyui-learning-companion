---
key: 图片生成/文生图/Nunchaku加速_FLUX_Kontext_lora_1911961603980623874.json
name: Nunchaku加速_FLUX_Kontext_lora_1911961603980623874.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Nunchaku加速_FLUX_Kontext_lora_1911961603980623874.json
hash: 3285a9dc0b045609
coverage: 0.807692
learned_at: 2026-10-07 19:46:00
nodes: [VAELoader, DualCLIPLoader, NunchakuFluxDiTLoader, Anything Everywhere3, CLIPTextEncode, SetNode, NunchakuFluxLoraLoader, SetNode, FluxGuidance, DifferentialDiffusion, ConditioningZeroOut, EmptyLatentImage, GetNode, GetNode, VAEDecode, KSampler, ConditioningZeroOut, CLIPTextEncode, VAEEncode, FluxKontextImageScale, ReferenceLatent, FluxGuidance, KSampler, VAEDecode, SaveImage, NunchakuFluxDiTLoader, VAELoader, DualCLIPLoader, Anything Everywhere3, SaveImage, CLIPTextEncode, ConditioningZeroOut, NunchakuFluxDiTLoader, VAELoader, DualCLIPLoader, Anything Everywhere3, RH_Translator, NunchakuFluxLoraLoader, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, VAEDecode, KSampler, VAEEncode, DifferentialDiffusion, FluxGuidance, RH_Translator, NunchakuFluxLoraLoader, LoadImage, Image Comparer (rgthree), LoadImage, RH_Translator, Fast Groups Bypasser (rgthree)]
patterns: [text_to_image, image_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.30000000000000004, "height": 1536, "sampler_name": "euler", "scheduler": "normal", "seed": 981053385176214, "steps": 20, "width": 1024}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Nunchaku加速_FLUX_Kontext_lora_1911961603980623874.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1911961603980623874.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `VAELoader`
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `Anything Everywhere3`
- `CLIPTextEncode` ★核心
- `SetNode`
- `NunchakuFluxLoraLoader` ★核心
- `SetNode`
- `FluxGuidance`
- `DifferentialDiffusion`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `ReferenceLatent`
- `FluxGuidance`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `NunchakuFluxDiTLoader`
- `VAELoader`
- `DualCLIPLoader`
- `Anything Everywhere3`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `NunchakuFluxDiTLoader`
- `VAELoader`
- `DualCLIPLoader`
- `Anything Everywhere3`
- `RH_Translator`
- `NunchakuFluxLoraLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `DifferentialDiffusion`
- `FluxGuidance`
- `RH_Translator`
- `NunchakuFluxLoraLoader` ★核心
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `RH_Translator`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `981053385176214`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **81%**（42/52）

**有卡**：`VAELoader`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`CLIPTextEncode`、`NunchakuFluxLoraLoader`、`FluxGuidance`、`DifferentialDiffusion`、`ConditioningZeroOut`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`VAEEncode`、`FluxKontextImageScale`、`ReferenceLatent`、`SaveImage`、`RH_Translator`、`LoadImage`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage、FluxGuidance

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
