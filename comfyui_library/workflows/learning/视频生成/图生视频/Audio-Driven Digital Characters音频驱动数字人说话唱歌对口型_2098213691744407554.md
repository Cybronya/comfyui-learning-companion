---
key: 视频生成/图生视频/Audio-Driven Digital Characters音频驱动数字人说话唱歌对口型_2098213691744407554.json
name: Audio-Driven Digital Characters音频驱动数字人说话唱歌对口型_2098213691744407554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Audio-Driven Digital Characters音频驱动数字人说话唱歌对口型_2098213691744407554.json
hash: 3299a166692715c1
coverage: 0.658537
learned_at: 2026-10-17 01:44:21
nodes: [VAELoader, GetNode, SetNode, ComfyMathExpression, Any To String (mtb), SetNode, PrimitiveInt, GetNode, PrimitiveInt, AILab_QwenVL, VAELoader, PreviewImage, VRGDG_MiniMaxH3AudioDrive, ImageResizeKJv2, PrimitiveInt, SetNode, AudioCrop, AudioSeparation, JoinStrings, JjkText, PrimitiveFloat, LoadAudio, PreviewAudio, RandomNoise, BasicGuider, SoundFlow_GetLength, GetNode, VAEDecode, ComfyMathExpression, SetNode, PrimitiveStringMultiline, UNETLoader, SamplerCustomAdvanced, Any To String (mtb), LoraLoaderModelOnly, CLIPLoader, MiniMaxH3ReferenceToVideo, KSamplerSelect, BasicScheduler, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Audio-Driven Digital Characters音频驱动数字人说话唱歌对口型_2098213691744407554.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Audio-Driven Digital Characters音频驱动数字人说话唱歌对口型_2098213691744407554.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `VAELoader`
- `GetNode`
- `SetNode`
- `ComfyMathExpression`
- `Any To String (mtb)`
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `PrimitiveInt`
- `AILab_QwenVL`
- `VAELoader`
- `PreviewImage`
- `VRGDG_MiniMaxH3AudioDrive`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `SetNode`
- `AudioCrop`
- `AudioSeparation`
- `JoinStrings`
- `JjkText`
- `PrimitiveFloat`
- `LoadAudio`
- `PreviewAudio`
- `RandomNoise`
- `BasicGuider`
- `SoundFlow_GetLength`
- `GetNode`
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `SetNode`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `Any To String (mtb)`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `MiniMaxH3ReferenceToVideo`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **66%**（27/41）

**有卡**：`VAELoader`、`ComfyMathExpression`、`Any To String (mtb)`、`AILab_QwenVL`、`VRGDG_MiniMaxH3AudioDrive`、`ImageResizeKJv2`、`AudioCrop`、`AudioSeparation`、`JoinStrings`、`LoadAudio`、`PreviewAudio`、`RandomNoise`、`BasicGuider`、`SoundFlow_GetLength`、`VAEDecode`、`UNETLoader`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`CLIPLoader`、`MiniMaxH3ReferenceToVideo`、`KSamplerSelect`、`BasicScheduler`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
