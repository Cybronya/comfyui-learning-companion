---
key: 图片生成/图生图/qwenedit最新双节棍QwenEdit人物姿态控制支持controlnet_nunchaku_1967805080453918722.json
name: qwenedit最新双节棍QwenEdit人物姿态控制支持controlnet_nunchaku_1967805080453918722
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwenedit最新双节棍QwenEdit人物姿态控制支持controlnet_nunchaku_1967805080453918722.json
hash: c232a8ec51b0ac73
coverage: 0.928571
learned_at: 2026-10-23 11:44:20
nodes: [PreviewImage, easy cleanGpuUsed, ControlNetApplySD3, easy cleanGpuUsed, LayerUtility: PurgeVRAM, TextEncodeQwenImageEdit, easy positive, VAELoader, ModelSamplingAuraFlow, VAEEncode, FluxKontextImageScale, PreviewImage, LoadImage, FluxKontextImageScale, CR Simple Image Compare, CLIPLoader, CFGNorm, LoadImage, VAEDecode, ReferenceLatent, ConditioningAverage, ControlNetLoader, SetUnionControlNetType, AIO_Preprocessor, SaveImage, NunchakuQwenImageDiTLoader, KSampler, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 0.98, "controlnet_strength": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 397565246979641, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwenedit最新双节棍QwenEdit人物姿态控制支持controlnet_nunchaku_1967805080453918722.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwenedit最新双节棍QwenEdit人物姿态控制支持controlnet_nunchaku_1967805080453918722.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `PreviewImage`
- `easy cleanGpuUsed`
- `ControlNetApplySD3` ★核心
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `TextEncodeQwenImageEdit`
- `easy positive`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `PreviewImage`
- `LoadImage`
- `FluxKontextImageScale`
- `CR Simple Image Compare`
- `CLIPLoader`
- `CFGNorm`
- `LoadImage`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `ConditioningAverage`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `SaveImage`
- `NunchakuQwenImageDiTLoader`
- `KSampler` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `397565246979641`
- `steps` = `6`
- `cfg` = `0.98`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`easy cleanGpuUsed`、`ControlNetApplySD3`、`LayerUtility: PurgeVRAM`、`TextEncodeQwenImageEdit`、`easy positive`、`VAELoader`、`ModelSamplingAuraFlow`、`VAEEncode`、`FluxKontextImageScale`、`LoadImage`、`CR Simple Image Compare`、`CLIPLoader`、`CFGNorm`、`VAEDecode`、`ReferenceLatent`、`ConditioningAverage`、`ControlNetLoader`、`SetUnionControlNetType`、`AIO_Preprocessor`、`SaveImage`、`NunchakuQwenImageDiTLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、ControlNetLoader、SetUnionControlNetType、ControlNetApplySD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
