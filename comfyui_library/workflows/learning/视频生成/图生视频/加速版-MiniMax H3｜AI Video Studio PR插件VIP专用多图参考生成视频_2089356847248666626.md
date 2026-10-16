---
key: 视频生成/图生视频/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用多图参考生成视频_2089356847248666626.json
name: 加速版-MiniMax H3｜AI Video Studio PR插件VIP专用多图参考生成视频_2089356847248666626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用多图参考生成视频_2089356847248666626.json
hash: 7ceb678ca42f26de
coverage: 0.928571
learned_at: 2026-10-16 21:43:46
nodes: [PrimitiveFloat, UpscaleModelLoader, ComfyMathExpression, VAELoader, VAELoader, UNETLoader, CLIPLoader, RandomNoise, KSamplerSelect, BasicScheduler, BasicGuider, PathchSageAttentionKJ, EasyCache, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, ImageUpscaleWithModel, MiniMaxH3ReferenceToVideo, CreateVideo, SaveVideo, LoadImage, LoadImage, LoadImage, LoadImage, ResolutionSelector, CR Prompt Text, LoadImage, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/图生视频/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用多图参考生成视频_2089356847248666626.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用多图参考生成视频_2089356847248666626.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `PrimitiveFloat`
- `UpscaleModelLoader`
- `ComfyMathExpression`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `PathchSageAttentionKJ`
- `EasyCache`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `ImageUpscaleWithModel`
- `MiniMaxH3ReferenceToVideo`
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `CR Prompt Text`
- `LoadImage`
- `PrimitiveFloat`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`UpscaleModelLoader`、`ComfyMathExpression`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`PathchSageAttentionKJ`、`EasyCache`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeAudio`、`ImageUpscaleWithModel`、`MiniMaxH3ReferenceToVideo`、`CreateVideo`、`SaveVideo`、`LoadImage`、`ResolutionSelector`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
