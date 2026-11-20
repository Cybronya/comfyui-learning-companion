---
key: 数字人/数字人/多图参考生视频  H3 Video with Multiple Images for Refere_2115614690868031489.json
name: 多图参考生视频  H3 Video with Multiple Images for Refere_2115614690868031489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/多图参考生视频  H3 Video with Multiple Images for Refere_2115614690868031489.json
hash: e4f59b10c30edc11
coverage: 0.857143
learned_at: 2026-10-30 17:56:44
nodes: [VAELoader, VAELoader, KSamplerSelect, UNETLoader, CLIPLoader, RandomNoise, PrimitiveFloat, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, ComfyMathExpression, DF_Int_to_Float, ImageResizeKJv2, ImageResizeKJv2, EasyCache, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, BasicScheduler, BasicGuider, SamplerCustomAdvanced, VAEDecodeAudio, VAEDecode, VHS_VideoCombine, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, ImageResizeKJv2]
patterns: []
missing: []
---

# 数字人/数字人/多图参考生视频  H3 Video with Multiple Images for Refere_2115614690868031489.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/多图参考生视频  H3 Video with Multiple Images for Refere_2115614690868031489.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Other

**节点**（28 个）：
- `VAELoader`
- `VAELoader`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `PrimitiveFloat`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ComfyMathExpression`
- `DF_Int_to_Float`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `EasyCache`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `BasicScheduler`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `ImageResizeKJv2`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`VAELoader`、`KSamplerSelect`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`LoadImage`、`LoraLoaderModelOnly`、`ComfyMathExpression`、`DF_Int_to_Float`、`ImageResizeKJv2`、`EasyCache`、`MiniMaxH3ReferenceToVideo`、`PathchSageAttentionKJ`、`BasicScheduler`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
