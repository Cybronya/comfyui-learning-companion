---
key: 图片生成/图生图/image_krea2_optimizer_workflow_2073588797480198146.json
name: image_krea2_optimizer_workflow_2073588797480198146
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image_krea2_optimizer_workflow_2073588797480198146.json
hash: 82c1e87e63a46bfa
coverage: 0.740741
learned_at: 2026-10-23 11:37:51
nodes: [MarkdownNote, MarkdownNote, StringConcatenate, TextGenerate, ComfySwitchNode, MarkdownNote, PreviewAny, PrimitiveStringMultiline, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, VAEDecode, SaveImage, SaveImage, UltralyticsDetectorProvider, SAMLoader, PrimitiveBoolean, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, LoraLoaderModelOnly, VAELoader, KSampler, KSampler, FaceDetailer, RTXVideoSuperResolution]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.20000000000000004, "height": 2048, "sampler_name": "deis", "scheduler": "bong_tangent", "seed": 982721285543792, "steps": 2, "width": 2048}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/image_krea2_optimizer_workflow_2073588797480198146.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image_krea2_optimizer_workflow_2073588797480198146.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（27 个）：
- `MarkdownNote`
- `MarkdownNote`
- `StringConcatenate`
- `TextGenerate`
- `ComfySwitchNode`
- `MarkdownNote`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `KSampler` ★核心
- `KSampler` ★核心
- `FaceDetailer`
- `RTXVideoSuperResolution`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `2048`
- `height` = `2048`
- `batch_size` = `1`
- `seed` = `982721285543792`
- `steps` = `2`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `bong_tangent`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`StringConcatenate`、`TextGenerate`、`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`UltralyticsDetectorProvider`、`SAMLoader`、`PrimitiveBoolean`、`ResolutionSelector`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`KSampler`、`FaceDetailer`、`RTXVideoSuperResolution`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
