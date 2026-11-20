---
key: 平台全量/Qwen_edit_2511人物多视图v1.5+单独生成+_2074066349059563522.json
name: Qwen_edit_2511人物多视图v1.5+单独生成+_2074066349059563522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen_edit_2511人物多视图v1.5+单独生成+_2074066349059563522.json
hash: 1e23453069dfc567
coverage: 0.836735
learned_at: 2026-11-14 00:53:32
nodes: [CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text, CR Text, CR Text, CR Text, LoadImage, LoadImage, LoadImage, CR Text, CR Text, CR Text, CR Text, ModelSamplingAuraFlow, CFGNorm, Reroute, JWStringConcat, JWStringConcat, DWPreprocessor, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Reroute, Fast Groups Bypasser (rgthree), MarkdownNote, easy showAnything, Int, VAEDecode, Image Comparer (rgthree), Seed (rgthree), SaveImage, SDPoseOODLoader, FluxKontextMultiReferenceLatentMethod, MarkdownNote, SaveImage, UNETLoader, LoraLoaderModelOnly, VAELoader, Anything Everywhere, Reroute, Reroute, Reroute, JWStringConcat, easy textSwitch, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, ReferenceLatent, KSampler, Reroute, Reroute, CR Text, QwenEditConfigPreparer, QwenEditConfigPreparer, Int, CR Image Input Switch, Reroute, SDPoseOODProcessor, TextEncodeQwenImageEditPlusCustom_lrzjason, CR Text, CR Text, LoadImage, CR Text, CR Text, LoadImage, SaveImage, LoadImage, CR Text, CR Text, easy imageIndexSwitch, easy textIndexSwitch, CR Text, LoadImage, CR Text, CR Text, CR Text, Int, SimpleMathCondition+, Reroute, SimpleComparison+, SimpleComparison+, Int, SimpleMathCondition+, Int, SimpleComparison+, SimpleMathCondition+, easy imageIndexSwitch, easy textIndexSwitch, LoadImage, MarkdownNote, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 154253141201625, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen_edit_2511人物多视图v1.5+单独生成+_2074066349059563522.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen_edit_2511人物多视图v1.5+单独生成+_2074066349059563522.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（98 个）：
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `Reroute`
- `JWStringConcat`
- `JWStringConcat`
- `DWPreprocessor`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `easy showAnything`
- `Int`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `Seed (rgthree)`
- `SaveImage`
- `SDPoseOODLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `MarkdownNote`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `Anything Everywhere`
- `Reroute`
- `Reroute`
- `Reroute`
- `JWStringConcat`
- `easy textSwitch`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `ReferenceLatent`
- `KSampler` ★核心
- `Reroute`
- `Reroute`
- `CR Text`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `Int`
- `CR Image Input Switch`
- `Reroute`
- `SDPoseOODProcessor`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `CR Text`
- `CR Text`
- `LoadImage`
- `CR Text`
- `CR Text`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `CR Text`
- `CR Text`
- `easy imageIndexSwitch`
- `easy textIndexSwitch`
- `CR Text`
- `LoadImage`
- `CR Text`
- `CR Text`
- `CR Text`
- `Int`
- `SimpleMathCondition+`
- `Reroute`
- `SimpleComparison+`
- `SimpleComparison+`
- `Int`
- `SimpleMathCondition+`
- `Int`
- `SimpleComparison+`
- `SimpleMathCondition+`
- `easy imageIndexSwitch`
- `easy textIndexSwitch`
- `LoadImage`
- `MarkdownNote`
- `CR Text`

## 关键参数

- `seed` = `154253141201625`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（82/98）

**有卡**：`CLIPLoader`、`LoadImage`、`CR Text`、`ModelSamplingAuraFlow`、`CFGNorm`、`JWStringConcat`、`DWPreprocessor`、`Int`、`VAEDecode`、`Seed (rgthree)`、`SaveImage`、`SDPoseOODLoader`、`FluxKontextMultiReferenceLatentMethod`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`easy textSwitch`、`ConditioningZeroOut`、`ReferenceLatent`、`KSampler`、`QwenEditConfigPreparer`、`CR Image Input Switch`、`SDPoseOODProcessor`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`easy imageIndexSwitch`、`easy textIndexSwitch`、`SimpleMathCondition+`、`SimpleComparison+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
