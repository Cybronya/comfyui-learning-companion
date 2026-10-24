---
key: 图片生成/图生图/Nunchaku-Qwen-image +Controlnet-union加速工作流_2073060605287821314.json
name: Nunchaku-Qwen-image +Controlnet-union加速工作流_2073060605287821314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku-Qwen-image +Controlnet-union加速工作流_2073060605287821314.json
hash: 7b27f5887a4e62aa
coverage: 0.818182
learned_at: 2026-10-23 11:10:02
nodes: [NunchakuQwenImageDiTLoader, ShowText, AILab_MiniCPM_4_V, ControlNetApplyAdvanced, ControlNetLoader, SetUnionControlNetType, AIO_Preprocessor, PreviewImage, Switch, JjkText, Note, Note, ModelSamplingAuraFlow, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptySD3LatentImage, VAEDecode, KSampler, SaveImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1821260513354, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Nunchaku-Qwen-image +Controlnet-union加速工作流_2073060605287821314.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku-Qwen-image +Controlnet-union加速工作流_2073060605287821314.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `NunchakuQwenImageDiTLoader`
- `ShowText`
- `AILab_MiniCPM_4_V`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `PreviewImage`
- `Switch`
- `JjkText`
- `Note`
- `Note`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `1821260513354`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`NunchakuQwenImageDiTLoader`、`ShowText`、`AILab_MiniCPM_4_V`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`SetUnionControlNetType`、`AIO_Preprocessor`、`Switch`、`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`EmptySD3LatentImage`、`VAEDecode`、`KSampler`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、ControlNetApplyAdvanced、ControlNetLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
