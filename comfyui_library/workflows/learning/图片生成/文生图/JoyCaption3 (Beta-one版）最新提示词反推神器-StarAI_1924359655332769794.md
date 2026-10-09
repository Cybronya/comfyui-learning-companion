---
key: 图片生成/文生图/JoyCaption3 (Beta-one版）最新提示词反推神器-StarAI_1924359655332769794.json
name: JoyCaption3 (Beta-one版）最新提示词反推神器-StarAI_1924359655332769794.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/JoyCaption3 (Beta-one版）最新提示词反推神器-StarAI_1924359655332769794.json
hash: de9a33005d60706f
coverage: 0.555556
learned_at: 2026-10-07 22:22:48
nodes: [Note Plus (mtb), easy showAnything, easy cleanGpuUsed, Reroute, Note, Fast Groups Bypasser (rgthree), VAELoader, EmptyLatentImage, FluxGuidance, ConditioningZeroOut, CLIPTextEncode, VAEDecode, easy cleanGpuUsed, RH_Translator, ShowText|pysssss, KSampler, UNETLoader, DualCLIPLoader, SaveImage, Reroute, LayerUtility: ImageScaleByAspectRatio V2, RH_Translator, ShowText|pysssss, easy cleanGpuUsed, JJC_JoyCaption_Custom, JJC_JoyCaption, TextCombinerTwo, JjkText, easy showAnything, RH_Captioner, LoadImage, JjkText, TextCombinerTwo, ShowText|pysssss, RH_Translator, RH_Prompter]
patterns: [text_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2, Note Plus (mtb), easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 1063019573550015, "steps": 20, "width": 768}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/JoyCaption3 (Beta-one版）最新提示词反推神器-StarAI_1924359655332769794.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1924359655332769794.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `Note Plus (mtb)`
- `easy showAnything`
- `easy cleanGpuUsed`
- `Reroute`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `RH_Translator`
- `ShowText|pysssss`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `SaveImage`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_Translator`
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `JJC_JoyCaption_Custom`
- `JJC_JoyCaption`
- `TextCombinerTwo`
- `JjkText`
- `easy showAnything`
- `RH_Captioner`
- `LoadImage`
- `JjkText`
- `TextCombinerTwo`
- `ShowText|pysssss`
- `RH_Translator`
- `RH_Prompter`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1063019573550015`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **56%**（20/36）

**有卡**：`VAELoader`、`EmptyLatentImage`、`FluxGuidance`、`ConditioningZeroOut`、`CLIPTextEncode`、`VAEDecode`、`RH_Translator`、`KSampler`、`UNETLoader`、`DualCLIPLoader`、`SaveImage`、`JJC_JoyCaption_Custom`、`JJC_JoyCaption`、`TextCombinerTwo`、`RH_Captioner`、`LoadImage`、`RH_Prompter`

**缺卡**（5）：`LayerUtility: ImageScaleByAspectRatio V2`、`Note Plus (mtb)`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
