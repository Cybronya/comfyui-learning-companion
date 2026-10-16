---
key: 视频生成/图生视频/wan2.2 Animate无限延长无VRAM限制_1978781425929490434.json
name: wan2.2 Animate无限延长无VRAM限制_1978781425929490434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1978781425929490434.json
hash: 6c17ed623c2b157a
coverage: 0.424
learned_at: 2026-10-15 22:32:20
nodes: [SetNode, GetNode, TrimVideoLatent, GetNode, KSampler, GetNode, TrimVideoLatent, GetNode, KSampler, TrimVideoLatent, GetNode, KSampler, VAEDecode, VAEDecode, SetNode, SetNode, ImageBatch, RIFE VFI, GetNode, RIFE VFI, GetNode, ImageBatch, WanAnimateToVideo, GetNode, GetNode, WanAnimateToVideo, WanAnimateToVideo, GetNode, SetNode, INTConstant, LoadImage, LoadImage, VHS_LoadVideo, INTConstant, SetNode, RIFE VFI, GetNode, VAEDecode, SetNode, SetNode, CLIPVisionEncode, CLIPVisionLoader, UnetLoaderGGUF, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, VAELoader, SetNode, CLIPLoader, CLIPTextEncode, SetNode, SetNode, LoraLoaderModelOnly, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy seed, LoadImage, CLIPTextEncode, Note, DrawViTPose, LoadImage, OnnxDetectionModelLoader, Note, GetNode, ImageScale, SetNode, SetNode, SetNode, SetNode, PoseAndFaceDetection, SetNode, SetNode, GetNode, SetNode, MathExpression|pysssss, Int, MathExpression|pysssss, Int, Int, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, MathExpression|pysssss, Fast Groups Muter (rgthree), GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, Label (rgthree), Label (rgthree), Label (rgthree), VHS_VideoCombine, Note, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 40, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan2.2 Animate无限延长无VRAM限制_1978781425929490434.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978781425929490434.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（125 个）：
- `SetNode`
- `GetNode`
- `TrimVideoLatent`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `TrimVideoLatent`
- `GetNode`
- `KSampler` ★核心
- `TrimVideoLatent`
- `GetNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `ImageBatch`
- `RIFE VFI`
- `GetNode`
- `RIFE VFI`
- `GetNode`
- `ImageBatch`
- `WanAnimateToVideo`
- `GetNode`
- `GetNode`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `GetNode`
- `SetNode`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `INTConstant`
- `SetNode`
- `RIFE VFI`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy seed`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Note`
- `DrawViTPose`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `Note`
- `GetNode`
- `ImageScale`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `MathExpression|pysssss`
- `Int`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `Note`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `40`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **42%**（53/125）

**有卡**：`TrimVideoLatent`、`KSampler`、`VAEDecode`、`ImageBatch`、`RIFE VFI`、`WanAnimateToVideo`、`INTConstant`、`LoadImage`、`VHS_LoadVideo`、`CLIPVisionEncode`、`CLIPVisionLoader`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`easy seed`、`DrawViTPose`、`OnnxDetectionModelLoader`、`ImageScale`、`PoseAndFaceDetection`、`MathExpression|pysssss`、`Int`、`VHS_VideoCombine`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、easy seed

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
