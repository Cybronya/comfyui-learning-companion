---
key: 平台全量/Nunchaku3.0-Controlnet+lora工作流_1929912735440736257.json
name: Nunchaku3.0-Controlnet+lora工作流_1929912735440736257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Nunchaku3.0-Controlnet+lora工作流_1929912735440736257.json
hash: 2208762e48a1ea98
coverage: 0.903226
learned_at: 2026-11-14 00:47:12
nodes: [ConditioningZeroOut, SetUnionControlNetType, ControlNetApplyAdvanced, MarkdownNote, AIO_Preprocessor, PreviewImage, ModelSamplingFlux, CFGZeroStarAndInit, KSamplerSelect, RandomNoise, GetImageSize+, FluxGuidance, GetImageSize+, BasicGuider, EmptySD3LatentImage, SamplerCustomAdvanced, BasicScheduler, VAEDecode, AddLabel, ImageResize+, AddLabel, PreviewImage, CLIPTextEncode, DualCLIPLoader, ControlNetLoader, NunchakuFluxLoraLoader, VAELoader, NunchakuFluxDiTLoader, ImageConcatMulti, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.6500000000000001}
---

# 平台全量/Nunchaku3.0-Controlnet+lora工作流_1929912735440736257.json

> 来源文件 `comfyui_library/workflows/平台全量/Nunchaku3.0-Controlnet+lora工作流_1929912735440736257.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `ConditioningZeroOut`
- `SetUnionControlNetType`
- `ControlNetApplyAdvanced` ★核心
- `MarkdownNote`
- `AIO_Preprocessor`
- `PreviewImage`
- `ModelSamplingFlux`
- `CFGZeroStarAndInit`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `GetImageSize+`
- `FluxGuidance`
- `GetImageSize+`
- `BasicGuider`
- `EmptySD3LatentImage`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `AddLabel`
- `ImageResize+`
- `AddLabel`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `ControlNetLoader`
- `NunchakuFluxLoraLoader` ★核心
- `VAELoader`
- `NunchakuFluxDiTLoader`
- `ImageConcatMulti`
- `SaveImage`
- `LoadImage`

## 关键参数

- `controlnet_strength` = `0.6500000000000001`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`ConditioningZeroOut`、`SetUnionControlNetType`、`ControlNetApplyAdvanced`、`AIO_Preprocessor`、`ModelSamplingFlux`、`CFGZeroStarAndInit`、`KSamplerSelect`、`RandomNoise`、`GetImageSize+`、`FluxGuidance`、`BasicGuider`、`EmptySD3LatentImage`、`SamplerCustomAdvanced`、`BasicScheduler`、`VAEDecode`、`AddLabel`、`ImageResize+`、`CLIPTextEncode`、`DualCLIPLoader`、`ControlNetLoader`、`NunchakuFluxLoraLoader`、`VAELoader`、`NunchakuFluxDiTLoader`、`ImageConcatMulti`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、SetUnionControlNetType
