---
key: 视频生成/文生视频/（自用）Wan2.2 All-in-one V9.1+CineScale文生视频_1959492706500292610.json
name: （自用）Wan2.2 All-in-one V9.1+CineScale文生视频_1959492706500292610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2 All-in-one V9.1+CineScale文生视频_1959492706500292610.json
hash: c622e8a79138b4ec
coverage: 0.826087
learned_at: 2026-10-10 23:14:40
nodes: [ModelSamplingSD3, VHS_VideoCombine, SaveLatent, EmptyHunyuanLatentVideo, LoadImage, SaveImage, VAEDecode, Note, Note, Note, CLIPLoader, JWInteger, CheckpointLoaderSimple, LoraLoaderModelOnly, PathchSageAttentionKJ, KSampler, LoraLoaderModelOnly, JWInteger, JWInteger, CLIPTextEncode, CLIPTextEncode, CR Prompt Text, JWInteger]
patterns: []
missing: [CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-nsfw-v7.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 620183626160808, "steps": 4}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/（自用）Wan2.2 All-in-one V9.1+CineScale文生视频_1959492706500292610.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2 All-in-one V9.1+CineScale文生视频_1959492706500292610.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（23 个）：
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `SaveLatent`
- `EmptyHunyuanLatentVideo`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心
- `Note`
- `Note`
- `Note`
- `CLIPLoader`
- `JWInteger`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `JWInteger`

## 关键参数

- `checkpoint` = `wan2.2-t2v-rapid-aio-nsfw-v7.safetensors`
- `seed` = `620183626160808`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`ModelSamplingSD3`、`VHS_VideoCombine`、`SaveLatent`、`EmptyHunyuanLatentVideo`、`LoadImage`、`SaveImage`、`VAEDecode`、`CLIPLoader`、`JWInteger`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`KSampler`、`CLIPTextEncode`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、SaveLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
