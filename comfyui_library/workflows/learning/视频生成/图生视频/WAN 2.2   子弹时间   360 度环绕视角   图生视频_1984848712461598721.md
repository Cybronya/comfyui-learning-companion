---
key: 视频生成/图生视频/WAN 2.2   子弹时间   360 度环绕视角   图生视频_1984848712461598721.json
name: WAN 2.2   子弹时间   360 度环绕视角   图生视频_1984848712461598721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1984848712461598721.json
hash: 4b0499be641f8621
coverage: 0.869565
learned_at: 2026-10-15 22:32:49
nodes: [CLIPLoader, VAELoader, PreviewImage, Note, Note, Note, ImageScaleBy, ModelSamplingSD3, ModelSamplingSD3, CLIPVisionEncode, WanImageToVideo, MathExpression|pysssss, JWInteger, MathExpression|pysssss, easy showAnything, Label (rgthree), KSamplerAdvanced, KSamplerAdvanced, CLIPVisionLoader, Seed (rgthree), CLIPTextEncode, easy cleanGpuUsed, VAEDecode, Pick From Batch (mtb), RIFE VFI, easy cleanGpuUsed, ImageScaleBy, SaveImage, VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode, Text Concatenate, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, wanBlockSwap, wanBlockSwap, JWInteger, LoraLoaderModelOnly, PrimitiveStringMultiline, LoadImage, LoraLoaderModelOnly, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN 2.2   子弹时间   360 度环绕视角   图生视频_1984848712461598721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1984848712461598721.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `Note`
- `Note`
- `Note`
- `ImageScaleBy`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPVisionEncode`
- `WanImageToVideo`
- `MathExpression|pysssss`
- `JWInteger`
- `MathExpression|pysssss`
- `easy showAnything`
- `Label (rgthree)`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPVisionLoader`
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Pick From Batch (mtb)`
- `RIFE VFI`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `SaveImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `Text Concatenate`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `wanBlockSwap`
- `wanBlockSwap`
- `JWInteger`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`CLIPLoader`、`VAELoader`、`ImageScaleBy`、`ModelSamplingSD3`、`CLIPVisionEncode`、`WanImageToVideo`、`MathExpression|pysssss`、`JWInteger`、`Label (rgthree)`、`KSamplerAdvanced`、`CLIPVisionLoader`、`Seed (rgthree)`、`CLIPTextEncode`、`easy cleanGpuUsed`、`VAEDecode`、`Pick From Batch (mtb)`、`RIFE VFI`、`SaveImage`、`VHS_VideoCombine`、`Text Concatenate`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`wanBlockSwap`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
