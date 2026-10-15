---
key: 视频生成/文生视频/（自用）Wan2.2 All-in-one V10+CineScale文生视频_1962792297958125570.json
name: （自用）Wan2.2 All-in-one V10+CineScale文生视频_1962792297958125570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2 All-in-one V10+CineScale文生视频_1962792297958125570.json
hash: 3ac66855af99c9ba
coverage: 0.869565
learned_at: 2026-10-15 22:49:12
nodes: [ModelSamplingSD3, SaveLatent, EmptyHunyuanLatentVideo, LoadImage, SaveImage, Note, Note, Note, JWInteger, PathchSageAttentionKJ, KSampler, LoraLoaderModelOnly, JWInteger, JWInteger, CLIPTextEncode, CLIPTextEncode, JWInteger, CLIPLoader, VHS_VideoCombine, VAEDecode, CR Prompt Text, LoraLoaderModelOnly, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 328555508094343, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/（自用）Wan2.2 All-in-one V10+CineScale文生视频_1962792297958125570.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2 All-in-one V10+CineScale文生视频_1962792297958125570.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（23 个）：
- `ModelSamplingSD3`
- `SaveLatent`
- `EmptyHunyuanLatentVideo`
- `LoadImage`
- `SaveImage`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `PathchSageAttentionKJ`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JWInteger`
- `CLIPLoader`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `328555508094343`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-t2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`ModelSamplingSD3`、`SaveLatent`、`EmptyHunyuanLatentVideo`、`LoadImage`、`SaveImage`、`JWInteger`、`PathchSageAttentionKJ`、`KSampler`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`CLIPLoader`、`VHS_VideoCombine`、`VAEDecode`、`CR Prompt Text`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、SaveLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
