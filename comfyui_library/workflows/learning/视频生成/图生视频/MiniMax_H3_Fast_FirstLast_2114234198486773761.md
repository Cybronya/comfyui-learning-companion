---
key: 视频生成/图生视频/MiniMax_H3_Fast_FirstLast_2114234198486773761.json
name: MiniMax_H3_Fast_FirstLast_2114234198486773761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax_H3_Fast_FirstLast_2114234198486773761.json
hash: f3c7167a896a3676
coverage: 0.954545
learned_at: 2026-10-26 22:13:26
nodes: [VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, CreateVideo, PathchSageAttentionKJ, EasyCache, LoadImage, ComfyMathExpression, ResolutionSelector, PrimitiveFloat, LoadImage, CR Prompt Text, MiniMaxH3ImageToVideo, SaveVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax_H3_Fast_FirstLast_2114234198486773761.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax_H3_Fast_FirstLast_2114234198486773761.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（22 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `CreateVideo`
- `PathchSageAttentionKJ`
- `EasyCache`
- `LoadImage`
- `ComfyMathExpression`
- `ResolutionSelector`
- `PrimitiveFloat`
- `LoadImage`
- `CR Prompt Text`
- `MiniMaxH3ImageToVideo`
- `SaveVideo`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`PathchSageAttentionKJ`、`EasyCache`、`LoadImage`、`ComfyMathExpression`、`ResolutionSelector`、`CR Prompt Text`、`MiniMaxH3ImageToVideo`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
