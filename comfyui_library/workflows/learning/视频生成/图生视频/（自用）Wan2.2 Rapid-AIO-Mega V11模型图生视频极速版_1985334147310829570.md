---
key: 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V11模型图生视频极速版_1985334147310829570.json
name: （自用）Wan2.2 Rapid-AIO-Mega V11模型图生视频极速版_1985334147310829570.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1985334147310829570.json
hash: ee149e9346f82eaa
coverage: 0.869565
learned_at: 2026-10-15 22:32:50
nodes: [ModelSamplingSD3, CLIPTextEncode, WanVaceToVideo, WanVideoVACEStartToEndFrame, Note, Note, CLIPTextEncode, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ApplySageAttention, Note, TT_img_enc, SaveImage, SaveImage, VAEDecode, KSampler, CLIPLoader, TT_img_enc_v2, CR Prompt Text, CR Prompt Text, LoadImage, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v11.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 517599457731669, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V11模型图生视频极速版_1985334147310829570.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1985334147310829570.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `ApplySageAttention`
- `Note`
- `TT_img_enc`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `TT_img_enc_v2`
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `517599457731669`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v11.safetensors`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`ApplySageAttention`、`TT_img_enc`、`SaveImage`、`VAEDecode`、`KSampler`、`CLIPLoader`、`TT_img_enc_v2`、`CR Prompt Text`、`LoadImage`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、CR Prompt Text、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
