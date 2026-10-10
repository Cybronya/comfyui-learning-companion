---
key: 视频生成/文生视频/Wan2.2万相4步加速视频生成-Rapid-AllInOne工作流_1972092157177884673.json
name: Wan2.2万相4步加速视频生成-Rapid-AllInOne工作流_1972092157177884673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2万相4步加速视频生成-Rapid-AllInOne工作流_1972092157177884673.json
hash: a9054410fac1b91c
coverage: 0.678571
learned_at: 2026-10-10 23:07:21
nodes: [ModelSamplingSD3, CLIPTextEncode, KSampler, VAEDecode, PreviewImage, VAEDecode, VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode, ModelSamplingSD3, WanImageToVideo, PreviewImage, KSampler, CLIPTextEncode, MathExpression|pysssss, Note, Note, JWInteger, MathExpression|pysssss, JWInteger, EmptyHunyuanLatentVideo, Note, Fast Groups Bypasser (rgthree), CLIPTextEncode, LoadImage, CheckpointLoaderSimple, CheckpointLoaderSimple, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, MathExpression|pysssss]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "normal", "seed": 442173459311585, "steps": 4}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2万相4步加速视频生成-Rapid-AllInOne工作流_1972092157177884673.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2万相4步加速视频生成-Rapid-AllInOne工作流_1972092157177884673.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `WanImageToVideo`
- `PreviewImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `Note`
- `Note`
- `JWInteger`
- `MathExpression|pysssss`
- `JWInteger`
- `EmptyHunyuanLatentVideo`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `seed` = `442173459311585`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `wan2.2-t2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **68%**（19/28）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`WanImageToVideo`、`JWInteger`、`EmptyHunyuanLatentVideo`、`LoadImage`、`CheckpointLoaderSimple`

**缺卡**（3）：`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`MathExpression|pysssss`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、EmptyHunyuanLatentVideo、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
