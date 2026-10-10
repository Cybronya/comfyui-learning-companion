---
key: 视频生成/文生视频/wan2.2-aio-v7-文生视频_1982741566634762241.json
name: wan2.2-aio-v7-文生视频_1982741566634762241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-aio-v7-文生视频_1982741566634762241.json
hash: dda2fdc62c02d85d
coverage: 0.652174
learned_at: 2026-10-11 02:45:03
nodes: [WanVaceToVideo, JWInteger, CLIPTextEncode, MathExpression|pysssss, Note, Note, CLIPTextEncode, ModelSamplingSD3, KSampler, ImageFromBatch+, ApplySageAttention, GetNode, Note, JWInteger, CheckpointLoaderSimple, JWInteger, DeepTranslatorTextNode, VAEDecode, TT_img_enc_v2, SetNode, VHS_VideoCombine, Note, SaveImage]
patterns: []
missing: [ImageFromBatch+, MathExpression|pysssss]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v7-nsfw.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 7567358653673, "steps": 4}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2-aio-v7-文生视频_1982741566634762241.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2-aio-v7-文生视频_1982741566634762241.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `WanVaceToVideo`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `ImageFromBatch+`
- `ApplySageAttention`
- `GetNode`
- `Note`
- `JWInteger`
- `CheckpointLoaderSimple` ★核心
- `JWInteger`
- `DeepTranslatorTextNode`
- `VAEDecode` ★核心
- `TT_img_enc_v2`
- `SetNode`
- `VHS_VideoCombine`
- `Note`
- `SaveImage`

## 关键参数

- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v7-nsfw.safetensors`

## 知识

覆盖率 **65%**（15/23）

**有卡**：`WanVaceToVideo`、`JWInteger`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSampler`、`ApplySageAttention`、`CheckpointLoaderSimple`、`DeepTranslatorTextNode`、`VAEDecode`、`TT_img_enc_v2`、`VHS_VideoCombine`、`SaveImage`

**缺卡**（2）：`ImageFromBatch+`、`MathExpression|pysssss`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、SaveImage、ModelSamplingSD3、VHS_VideoCombine、DeepTranslatorTextNode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
