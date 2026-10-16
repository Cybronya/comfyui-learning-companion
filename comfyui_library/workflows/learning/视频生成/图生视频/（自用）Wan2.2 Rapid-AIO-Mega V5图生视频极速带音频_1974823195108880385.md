---
key: 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V5图生视频极速带音频_1974823195108880385.json
name: （自用）Wan2.2 Rapid-AIO-Mega V5图生视频极速带音频_1974823195108880385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1974823195108880385.json
hash: 51f81d77cfcf1d72
coverage: 0.875
learned_at: 2026-10-15 22:32:06
nodes: [ModelSamplingSD3, CLIPTextEncode, WanVaceToVideo, Note, WanVideoVACEStartToEndFrame, ApplySageAttention, Note, Note, CLIPTextEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, KSampler, SaveImage, CR Prompt Text, LayerUtility: PurgeVRAM V2, VAEDecode, HunyuanVideoFoley, TT_img_enc, CheckpointLoaderSimple, JWInteger, JWInteger, CR Prompt Text, LoadImage, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v5.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 454805549067572, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V5图生视频极速带音频_1974823195108880385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1974823195108880385.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `Note`
- `WanVideoVACEStartToEndFrame`
- `ApplySageAttention`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `SaveImage`
- `CR Prompt Text`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `HunyuanVideoFoley`
- `TT_img_enc`
- `CheckpointLoaderSimple` ★核心
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `LoadImage`
- `SaveImage`

## 关键参数

- `seed` = `454805549067572`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v5.safetensors`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`ApplySageAttention`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`SaveImage`、`CR Prompt Text`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`HunyuanVideoFoley`、`TT_img_enc`、`CheckpointLoaderSimple`、`JWInteger`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CR Prompt Text、SaveImage、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
