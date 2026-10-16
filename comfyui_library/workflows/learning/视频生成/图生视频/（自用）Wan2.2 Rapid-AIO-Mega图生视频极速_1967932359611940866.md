---
key: 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega图生视频极速_1967932359611940866.json
name: （自用）Wan2.2 Rapid-AIO-Mega图生视频极速_1967932359611940866.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967932359611940866.json
hash: 2090e79f06df9ee8
coverage: 0.857143
learned_at: 2026-10-15 22:31:43
nodes: [ModelSamplingSD3, CLIPTextEncode, WanVaceToVideo, Note, WanVideoVACEStartToEndFrame, CheckpointLoaderSimple, ApplySageAttention, Note, Note, CLIPTextEncode, SaveImage, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, KSampler, JWInteger, VAEDecode, TT_img_enc, LoadImage, LoadImage, SaveImage, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 781779088034801, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega图生视频极速_1967932359611940866.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967932359611940866.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `Note`
- `WanVideoVACEStartToEndFrame`
- `CheckpointLoaderSimple` ★核心
- `ApplySageAttention`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `JWInteger`
- `VAEDecode` ★核心
- `TT_img_enc`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `CR Prompt Text`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`
- `seed` = `781779088034801`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`CheckpointLoaderSimple`、`ApplySageAttention`、`SaveImage`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`VAEDecode`、`TT_img_enc`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CR Prompt Text、SaveImage、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
