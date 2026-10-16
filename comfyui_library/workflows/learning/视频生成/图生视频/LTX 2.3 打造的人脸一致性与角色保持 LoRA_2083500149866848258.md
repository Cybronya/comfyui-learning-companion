---
key: 视频生成/图生视频/LTX 2.3 打造的人脸一致性与角色保持 LoRA_2083500149866848258.json
name: LTX 2.3 打造的人脸一致性与角色保持 LoRA_2083500149866848258
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3 打造的人脸一致性与角色保持 LoRA_2083500149866848258.json
hash: d0596281b9812fd2
coverage: 0.446154
learned_at: 2026-10-16 19:17:08
nodes: [PrimitiveBoolean, PrimitiveInt, MarkdownNote, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, SetNode, VAEDecode, GetNode, SetNode, LatentUpscaleModelLoader, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, UNETLoader, SetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, SetNode, SetNode, SetNode, SetNode, RandomNoise, GetNode, GetNode, GetNode, SamplerCustomAdvanced, ManualSigmas, GetNode, KSamplerSelect, CFGGuider, SetNode, RMBG, PreviewImage, VHS_VideoCombine, LTXVSeparateAVLatent, LoraLoaderModelOnly, MarkdownNote, PrimitiveInt, GetNode, BasicScheduler, ImageResizeKJv2, LTXIdentityOverlapConditioning, LoadImage, ComfyMathExpression, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX 2.3 打造的人脸一致性与角色保持 LoRA_2083500149866848258.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX 2.3 打造的人脸一致性与角色保持 LoRA_2083500149866848258.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `PrimitiveBoolean`
- `PrimitiveInt`
- `MarkdownNote`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `GetNode`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SetNode`
- `RMBG`
- `PreviewImage`
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `PrimitiveInt`
- `GetNode`
- `BasicScheduler`
- `ImageResizeKJv2`
- `LTXIdentityOverlapConditioning`
- `LoadImage`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **45%**（29/65）

**有卡**：`PrimitiveBoolean`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`ComfyMathExpression`、`VAEDecode`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`UNETLoader`、`LTXVConcatAVLatent`、`RandomNoise`、`SamplerCustomAdvanced`、`ManualSigmas`、`KSamplerSelect`、`CFGGuider`、`RMBG`、`VHS_VideoCombine`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`BasicScheduler`、`ImageResizeKJv2`、`LTXIdentityOverlapConditioning`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
