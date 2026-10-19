---
key: 数字人/数字人/H3+Video+Costume+Changes!+H3+Video H3视频换装！H3视频编辑_2109550806524579841.json
name: H3+Video+Costume+Changes!+H3+Video H3视频换装！H3视频编辑_2109550806524579841
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/H3+Video+Costume+Changes!+H3+Video H3视频换装！H3视频编辑_2109550806524579841.json
hash: 679b4422900fed64
coverage: 0.833333
learned_at: 2026-10-19 00:40:59
nodes: [BasicGuider, PathchSageAttentionKJ, MiniMaxH3MemoryEfficientSageAttentionPatch, KSamplerSelect, VAEDecode, SamplerCustomAdvanced, JoinStrings, JoinStrings, ComfyMathExpression, PrimitiveStringMultiline, PrimitiveStringMultiline, UNETLoader, CLIPLoader, VAELoader, VAELoader, RandomNoise, VAEDecodeAudio, ComfyMathExpression, DF_Int_to_Float, ImageConcanate, ImageConcanate, LoraLoaderModelOnly, AILab_QwenVL, MiniMaxH3ReferenceToVideo, JoinStrings, ImageResizeKJv2, PrimitiveStringMultiline, ImageResizeKJv2, BasicScheduler, PrimitiveInt, PrimitiveInt, PrimitiveFloat, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/H3+Video+Costume+Changes!+H3+Video H3视频换装！H3视频编辑_2109550806524579841.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/H3+Video+Costume+Changes!+H3+Video H3视频换装！H3视频编辑_2109550806524579841.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Other

**节点**（36 个）：
- `BasicGuider`
- `PathchSageAttentionKJ`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `JoinStrings`
- `JoinStrings`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `RandomNoise`
- `VAEDecodeAudio` ★核心
- `ComfyMathExpression`
- `DF_Int_to_Float`
- `ImageConcanate`
- `ImageConcanate`
- `LoraLoaderModelOnly` ★核心
- `AILab_QwenVL`
- `MiniMaxH3ReferenceToVideo`
- `JoinStrings`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `ImageResizeKJv2`
- `BasicScheduler`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`BasicGuider`、`PathchSageAttentionKJ`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`KSamplerSelect`、`VAEDecode`、`SamplerCustomAdvanced`、`JoinStrings`、`ComfyMathExpression`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`RandomNoise`、`VAEDecodeAudio`、`DF_Int_to_Float`、`ImageConcanate`、`LoraLoaderModelOnly`、`AILab_QwenVL`、`MiniMaxH3ReferenceToVideo`、`ImageResizeKJv2`、`BasicScheduler`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
