---
key: 视频生成/图生视频/Video+Costume+Changes!+H3+Video+EH3视频换装！H3视频编辑_2106912081130901505.json
name: Video+Costume+Changes!+H3+Video+EH3视频换装！H3视频编辑_2106912081130901505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Video+Costume+Changes!+H3+Video+EH3视频换装！H3视频编辑_2106912081130901505.json
hash: 1979947b5e462b93
coverage: 0.833333
learned_at: 2026-10-17 22:19:06
nodes: [BasicGuider, PathchSageAttentionKJ, MiniMaxH3MemoryEfficientSageAttentionPatch, KSamplerSelect, VAEDecode, SamplerCustomAdvanced, JoinStrings, JoinStrings, ComfyMathExpression, PrimitiveStringMultiline, PrimitiveStringMultiline, UNETLoader, CLIPLoader, VAELoader, VAELoader, RandomNoise, VAEDecodeAudio, ComfyMathExpression, DF_Int_to_Float, ImageConcanate, ImageConcanate, LoraLoaderModelOnly, AILab_QwenVL, MiniMaxH3ReferenceToVideo, JoinStrings, ImageResizeKJv2, PrimitiveStringMultiline, ImageResizeKJv2, BasicScheduler, PrimitiveInt, PrimitiveInt, PrimitiveFloat, VHS_VideoCombine, VHS_VideoCombine, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Video+Costume+Changes!+H3+Video+EH3视频换装！H3视频编辑_2106912081130901505.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Video+Costume+Changes!+H3+Video+EH3视频换装！H3视频编辑_2106912081130901505.json`

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
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`BasicGuider`、`PathchSageAttentionKJ`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`KSamplerSelect`、`VAEDecode`、`SamplerCustomAdvanced`、`JoinStrings`、`ComfyMathExpression`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`RandomNoise`、`VAEDecodeAudio`、`DF_Int_to_Float`、`ImageConcanate`、`LoraLoaderModelOnly`、`AILab_QwenVL`、`MiniMaxH3ReferenceToVideo`、`ImageResizeKJv2`、`BasicScheduler`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
