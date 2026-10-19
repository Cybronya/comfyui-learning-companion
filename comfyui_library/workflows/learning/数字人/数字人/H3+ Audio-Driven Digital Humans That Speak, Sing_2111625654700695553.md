---
key: 数字人/数字人/H3+ Audio-Driven Digital Humans That Speak, Sing_2111625654700695553.json
name: H3+ Audio-Driven Digital Humans That Speak, Sing_2111625654700695553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/H3+ Audio-Driven Digital Humans That Speak, Sing_2111625654700695553.json
hash: 01f2f586738ed427
coverage: 0.658537
learned_at: 2026-10-19 00:40:59
nodes: [VAELoader, GetNode, SetNode, ComfyMathExpression, Any To String (mtb), SetNode, GetNode, PrimitiveInt, AILab_QwenVL, VAELoader, PreviewImage, VRGDG_MiniMaxH3AudioDrive, ImageResizeKJv2, SetNode, AudioCrop, AudioSeparation, JoinStrings, JjkText, PrimitiveFloat, RandomNoise, BasicGuider, SoundFlow_GetLength, GetNode, VAEDecode, ComfyMathExpression, SetNode, UNETLoader, SamplerCustomAdvanced, Any To String (mtb), LoraLoaderModelOnly, CLIPLoader, MiniMaxH3ReferenceToVideo, KSamplerSelect, BasicScheduler, PrimitiveStringMultiline, LoadImage, LoadAudio, PreviewAudio, PrimitiveInt, PrimitiveInt, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/H3+ Audio-Driven Digital Humans That Speak, Sing_2111625654700695553.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/H3+ Audio-Driven Digital Humans That Speak, Sing_2111625654700695553.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `VAELoader`
- `GetNode`
- `SetNode`
- `ComfyMathExpression`
- `Any To String (mtb)`
- `SetNode`
- `GetNode`
- `PrimitiveInt`
- `AILab_QwenVL`
- `VAELoader`
- `PreviewImage`
- `VRGDG_MiniMaxH3AudioDrive`
- `ImageResizeKJv2`
- `SetNode`
- `AudioCrop`
- `AudioSeparation`
- `JoinStrings`
- `JjkText`
- `PrimitiveFloat`
- `RandomNoise`
- `BasicGuider`
- `SoundFlow_GetLength`
- `GetNode`
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `SetNode`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `Any To String (mtb)`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `MiniMaxH3ReferenceToVideo`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadAudio`
- `PreviewAudio`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`

## 知识

覆盖率 **66%**（27/41）

**有卡**：`VAELoader`、`ComfyMathExpression`、`Any To String (mtb)`、`AILab_QwenVL`、`VRGDG_MiniMaxH3AudioDrive`、`ImageResizeKJv2`、`AudioCrop`、`AudioSeparation`、`JoinStrings`、`RandomNoise`、`BasicGuider`、`SoundFlow_GetLength`、`VAEDecode`、`UNETLoader`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`CLIPLoader`、`MiniMaxH3ReferenceToVideo`、`KSamplerSelect`、`BasicScheduler`、`LoadImage`、`LoadAudio`、`PreviewAudio`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
