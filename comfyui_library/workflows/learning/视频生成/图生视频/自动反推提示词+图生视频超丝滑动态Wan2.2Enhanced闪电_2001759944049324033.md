---
key: 视频生成/图生视频/自动反推提示词+图生视频超丝滑动态Wan2.2Enhanced闪电_2001759944049324033.json
name: 自动反推提示词+图生视频超丝滑动态Wan2.2Enhanced闪电_2001759944049324033.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2001759944049324033.json
hash: 7170ebd48af859be
coverage: 0.828571
learned_at: 2026-10-15 22:33:46
nodes: [CLIPTextEncode, ModelPatchTorchSettings, WanVideoNAG, PrimitiveFloat, CLIPLoader, PathchSageAttentionKJ, easy cleanGpuUsed, Int, Int, JjkText, ShowText|pysssss, ShowText|pysssss, VHS_VideoCombine, ShowText|pysssss, Doubao_ImageToPrompt, GLM_ImageToPrompt, LoadImage, FindPerfectResolution, PainterI2V, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPTextEncode, Int, MathExpression|pysssss, VAELoader, Note, KSamplerAdvanced, Qwen3VL_Advanced, Qwen3VL_ExtraOptions, KSamplerAdvanced, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/自动反推提示词+图生视频超丝滑动态Wan2.2Enhanced闪电_2001759944049324033.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001759944049324033.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（35 个）：
- `CLIPTextEncode` ★核心
- `ModelPatchTorchSettings`
- `WanVideoNAG`
- `PrimitiveFloat`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `easy cleanGpuUsed`
- `Int`
- `Int`
- `JjkText`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `Doubao_ImageToPrompt`
- `GLM_ImageToPrompt`
- `LoadImage`
- `FindPerfectResolution`
- `PainterI2V`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `Int`
- `MathExpression|pysssss`
- `VAELoader`
- `Note`
- `KSamplerAdvanced` ★核心
- `Qwen3VL_Advanced`
- `Qwen3VL_ExtraOptions`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（29/35）

**有卡**：`CLIPTextEncode`、`ModelPatchTorchSettings`、`WanVideoNAG`、`CLIPLoader`、`PathchSageAttentionKJ`、`easy cleanGpuUsed`、`Int`、`VHS_VideoCombine`、`Doubao_ImageToPrompt`、`GLM_ImageToPrompt`、`LoadImage`、`FindPerfectResolution`、`PainterI2V`、`ModelSamplingSD3`、`VAEDecode`、`MathExpression|pysssss`、`VAELoader`、`KSamplerAdvanced`、`Qwen3VL_Advanced`、`Qwen3VL_ExtraOptions`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Doubao_ImageToPrompt
