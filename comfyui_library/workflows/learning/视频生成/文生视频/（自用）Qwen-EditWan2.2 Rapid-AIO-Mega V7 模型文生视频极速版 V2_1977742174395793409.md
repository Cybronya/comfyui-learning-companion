---
key: 视频生成/文生视频/（自用）Qwen-EditWan2.2 Rapid-AIO-Mega V7 模型文生视频极速版 V2_1977742174395793409.json
name: （自用）Qwen-EditWan2.2 Rapid-AIO-Mega V7 模型文生视频极速版 V2_1977742174395793409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Qwen-EditWan2.2 Rapid-AIO-Mega V7 模型文生视频极速版 V2_1977742174395793409.json
hash: 6b316d2d53af5373
coverage: 0.708333
learned_at: 2026-10-10 23:14:37
nodes: [Note, JWInteger, Note, Note, WanVaceToVideo, ModelSamplingSD3, ApplySageAttention, CLIPTextEncode, JWInteger, JWInteger, Note, VAEDecode, CheckpointLoaderSimple, KSampler, SaveImage, SaveImage, ImageFromBatch+, TT_img_enc, CR Prompt Text, Note, CLIPTextEncode, TT_img_enc_v2, SaveImage, LoadImage]
patterns: []
missing: [ImageFromBatch+, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v7-nsfw.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 7567358653673, "steps": 4}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/（自用）Qwen-EditWan2.2 Rapid-AIO-Mega V7 模型文生视频极速版 V2_1977742174395793409.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（自用）Qwen-EditWan2.2 Rapid-AIO-Mega V7 模型文生视频极速版 V2_1977742174395793409.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `Note`
- `JWInteger`
- `Note`
- `Note`
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `ApplySageAttention`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`
- `Note`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `ImageFromBatch+`
- `TT_img_enc`
- `CR Prompt Text`
- `Note`
- `CLIPTextEncode` ★核心
- `TT_img_enc_v2`
- `SaveImage`
- `LoadImage`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-v7-nsfw.safetensors`
- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **71%**（17/24）

**有卡**：`JWInteger`、`WanVaceToVideo`、`ModelSamplingSD3`、`ApplySageAttention`、`CLIPTextEncode`、`VAEDecode`、`CheckpointLoaderSimple`、`KSampler`、`SaveImage`、`TT_img_enc`、`TT_img_enc_v2`、`LoadImage`

**缺卡**（2）：`ImageFromBatch+`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveImage、ModelSamplingSD3、JWInteger

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
