---
key: 平台全量/Sketch coloring workflow_1864944402526588930.json
name: Sketch coloring workflow_1864944402526588930
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Sketch coloring workflow_1864944402526588930.json
hash: 8691560cf01b7515
coverage: 0.944444
learned_at: 2026-11-14 01:00:42
nodes: [ConditioningConcat, VAEEncode, ACN_ReferencePreprocessor, ACN_AdvancedControlNetApply, ACN_ReferenceControlNet, ACN_AdvancedControlNetApply, ControlNetLoaderAdvanced, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, KSampler, VAEDecode, SaveImage, PreviewImage, HintImageEnchance, SDXLEmptyLatentSizePicker+, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 0, "cfg": 7, "checkpoint": "aaaautismPonyFinetune_aaaaReStart.safetensors", "controlnet_strength": 0.9500000000000001, "denoise": 1, "height": 1, "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 1025880851511530, "steps": 30, "width": "832x1216 (0.68)"}
---

# 平台全量/Sketch coloring workflow_1864944402526588930.json

> 来源文件 `comfyui_library/workflows/平台全量/Sketch coloring workflow_1864944402526588930.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ConditioningConcat`
- `VAEEncode` ★核心
- `ACN_ReferencePreprocessor`
- `ACN_AdvancedControlNetApply` ★核心
- `ACN_ReferenceControlNet`
- `ACN_AdvancedControlNetApply` ★核心
- `ControlNetLoaderAdvanced`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `HintImageEnchance`
- `SDXLEmptyLatentSizePicker+` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `0.9500000000000001`
- `checkpoint` = `aaaautismPonyFinetune_aaaaReStart.safetensors`
- `seed` = `1025880851511530`
- `steps` = `30`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `832x1216 (0.68)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`ConditioningConcat`、`VAEEncode`、`ACN_ReferencePreprocessor`、`ACN_AdvancedControlNetApply`、`ACN_ReferenceControlNet`、`ControlNetLoaderAdvanced`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`KSampler`、`VAEDecode`、`SaveImage`、`HintImageEnchance`、`SDXLEmptyLatentSizePicker+`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ACN_AdvancedControlNetApply、ControlNetLoaderAdvanced、ACN_ReferenceControlNet
