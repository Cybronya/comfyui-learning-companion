---
key: 视频生成/图生视频/WAN 2.2 I2V Bullet Time：子弹时间凝固瞬间，解锁 360 度环绕视角！图生视频_1984539603493404673.json
name: WAN 2.2 I2V Bullet Time：子弹时间凝固瞬间，解锁 360 度环绕视角！图生视频_1984539603493404673.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN 2.2 I2V Bullet Time：子弹时间凝固瞬间，解锁 360 度环绕视角！图生视频_1984539603493404673.json
hash: b696d1cd89e45862
coverage: 0.87234
learned_at: 2026-10-15 22:32:48
nodes: [CLIPLoader, VAELoader, PreviewImage, Note, Note, Note, Seed (rgthree), easy cleanGpuUsed, Pick From Batch (mtb), easy cleanGpuUsed, ImageScaleBy, SaveImage, RIFE VFI, ImageScaleBy, VHS_VideoCombine, VHS_VideoCombine, CLIPVisionLoader, ModelSamplingSD3, ModelSamplingSD3, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, VAEDecode, WanImageToVideo, CLIPTextEncode, JWInteger, MathExpression|pysssss, JWInteger, MathExpression|pysssss, easy showAnything, Label (rgthree), CLIPTextEncode, LoraLoaderModelOnly, Text Concatenate, PrimitiveStringMultiline, Wan22PromptSelector, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, UNETLoader, Label (rgthree), LoadImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN 2.2 I2V Bullet Time：子弹时间凝固瞬间，解锁 360 度环绕视角！图生视频_1984539603493404673.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1984539603493404673.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `Note`
- `Note`
- `Note`
- `Seed (rgthree)`
- `easy cleanGpuUsed`
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `SaveImage`
- `RIFE VFI`
- `ImageScaleBy`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `MathExpression|pysssss`
- `JWInteger`
- `MathExpression|pysssss`
- `easy showAnything`
- `Label (rgthree)`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text Concatenate`
- `PrimitiveStringMultiline`
- `Wan22PromptSelector`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Label (rgthree)`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **87%**（41/47）

**有卡**：`CLIPLoader`、`VAELoader`、`Seed (rgthree)`、`easy cleanGpuUsed`、`Pick From Batch (mtb)`、`ImageScaleBy`、`SaveImage`、`RIFE VFI`、`VHS_VideoCombine`、`CLIPVisionLoader`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionEncode`、`VAEDecode`、`WanImageToVideo`、`CLIPTextEncode`、`JWInteger`、`MathExpression|pysssss`、`Label (rgthree)`、`LoraLoaderModelOnly`、`Text Concatenate`、`Wan22PromptSelector`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`UNETLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
