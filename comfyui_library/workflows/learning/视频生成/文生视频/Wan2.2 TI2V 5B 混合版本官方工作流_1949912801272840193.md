---
key: 视频生成/文生视频/Wan2.2 TI2V 5B 混合版本官方工作流_1949912801272840193.json
name: Wan2.2 TI2V 5B 混合版本官方工作流_1949912801272840193.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1949912801272840193.json
hash: c6ae8ec3cc40bc72
coverage: 0.894737
learned_at: 2026-10-15 22:43:33
nodes: [CLIPLoader, CLIPTextEncode, UNETLoader, ModelSamplingSD3, VAELoader, easy showAnything, MathExpression|pysssss, JWInteger, CLIPTextEncode, LoadImage, VAEDecode, Wan22ImageToVideoLatent, ImageResizeKJv2, KSampler, Int, Int, RH_Translator, Note, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 988966284673135, "steps": 30}
---

# 视频生成/文生视频/Wan2.2 TI2V 5B 混合版本官方工作流_1949912801272840193.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1949912801272840193.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（19 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `easy showAnything`
- `MathExpression|pysssss`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `Wan22ImageToVideoLatent`
- `ImageResizeKJv2`
- `KSampler` ★核心
- `Int`
- `Int`
- `RH_Translator`
- `Note`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `988966284673135`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`ModelSamplingSD3`、`VAELoader`、`MathExpression|pysssss`、`JWInteger`、`LoadImage`、`VAEDecode`、`Wan22ImageToVideoLatent`、`ImageResizeKJv2`、`KSampler`、`Int`、`RH_Translator`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Wan22ImageToVideoLatent
