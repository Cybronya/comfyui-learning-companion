---
key: 图片生成/图生图/flux kontext dev 单图 双图 三图 三合一 nunchaku加速版_1937433957573279745.json
name: flux kontext dev 单图 双图 三图 三合一 nunchaku加速版_1937433957573279745
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux kontext dev 单图 双图 三图 三合一 nunchaku加速版_1937433957573279745.json
hash: 9638c62c3bf65a40
coverage: 0.766667
learned_at: 2026-10-23 11:35:06
nodes: [VAELoader, FluxGuidance, ReferenceLatent, ImageStitch, VAEEncode, EmptyLatentImage, ImageStitch, ConditioningZeroOut, FluxResolutionNode, Int Literal, VAEDecode, MarkdownNote, MarkdownNote, MarkdownNote, LayerUtility: BooleanOperatorV2, FluxKontextImageScale, ImpactSwitch, DualCLIPLoader, CLIPTextEncode, ShowText|pysssss, easy ifElse, RH_Translator, LoadImage, SaveImage, LoadImage, LoadImage, easy ifElse, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, KSampler]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 141178004739053, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/flux kontext dev 单图 双图 三图 三合一 nunchaku加速版_1937433957573279745.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux kontext dev 单图 双图 三图 三合一 nunchaku加速版_1937433957573279745.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `VAELoader`
- `FluxGuidance`
- `ReferenceLatent`
- `ImageStitch`
- `VAEEncode` ★核心
- `EmptyLatentImage` ★核心
- `ImageStitch`
- `ConditioningZeroOut`
- `FluxResolutionNode`
- `Int Literal`
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LayerUtility: BooleanOperatorV2`
- `FluxKontextImageScale`
- `ImpactSwitch`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `easy ifElse`
- `RH_Translator`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `easy ifElse`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `KSampler` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `141178004739053`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（23/30）

**有卡**：`VAELoader`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`VAEEncode`、`EmptyLatentImage`、`ConditioningZeroOut`、`FluxResolutionNode`、`Int Literal`、`VAEDecode`、`LayerUtility: BooleanOperatorV2`、`FluxKontextImageScale`、`DualCLIPLoader`、`CLIPTextEncode`、`RH_Translator`、`LoadImage`、`SaveImage`、`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage、FluxGuidance

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
