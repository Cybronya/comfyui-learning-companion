---
key: 视频生成/图生视频/Wan 2.2 Smooth Mix + Foley：图生视频（音画同步）_2036101580507844609.json
name: Wan 2.2 Smooth Mix + Foley：图生视频（音画同步）_2036101580507844609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2036101580507844609.json
hash: 4860e12c49bed145
coverage: 0.777778
learned_at: 2026-10-15 22:35:51
nodes: [Note, Note, CLIPLoader, VAELoader, Note, Note, Note, Seed (rgthree), Note, Note, Note, easy cleanGpuUsed, Pick From Batch (mtb), easy cleanGpuUsed, ImageScaleBy, VHS_VideoCombine, ModelSamplingSD3, ModelSamplingSD3, CLIPVisionEncode, KSamplerAdvanced, KSamplerAdvanced, MathExpression|pysssss, JWInteger, easy showAnything, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, wanBlockSwap, wanBlockSwap, CLIPTextEncode, CLIPVisionLoader, WanImageToVideo, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, LoadImage, UNETLoader, UNETLoader, MathExpression|pysssss, VAEDecode, PrimitiveStringMultiline, RH_Translator, PreviewAudio, easy showAnything, RIFE VFI, HunyuanVideoFoley, Label (rgthree), VHS_VideoCombine, AudioAdjustVolume, JWInteger, ConvertAny2Float, EmptyAudio, easy ifElse, Bool]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan 2.2 Smooth Mix + Foley：图生视频（音画同步）_2036101580507844609.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036101580507844609.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（54 个）：
- `Note`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `Note`
- `Note`
- `Seed (rgthree)`
- `Note`
- `Note`
- `Note`
- `easy cleanGpuUsed`
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPVisionEncode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `MathExpression|pysssss`
- `JWInteger`
- `easy showAnything`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `wanBlockSwap`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `WanImageToVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `RH_Translator`
- `PreviewAudio`
- `easy showAnything`
- `RIFE VFI`
- `HunyuanVideoFoley`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `AudioAdjustVolume`
- `JWInteger`
- `ConvertAny2Float`
- `EmptyAudio`
- `easy ifElse`
- `Bool`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **78%**（42/54）

**有卡**：`CLIPLoader`、`VAELoader`、`Seed (rgthree)`、`easy cleanGpuUsed`、`Pick From Batch (mtb)`、`ImageScaleBy`、`VHS_VideoCombine`、`ModelSamplingSD3`、`CLIPVisionEncode`、`KSamplerAdvanced`、`MathExpression|pysssss`、`JWInteger`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`wanBlockSwap`、`CLIPTextEncode`、`CLIPVisionLoader`、`WanImageToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`UNETLoader`、`VAEDecode`、`RH_Translator`、`PreviewAudio`、`RIFE VFI`、`HunyuanVideoFoley`、`Label (rgthree)`、`AudioAdjustVolume`、`ConvertAny2Float`、`EmptyAudio`、`Bool`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
