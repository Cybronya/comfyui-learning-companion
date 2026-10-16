---
key: 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V3.1图生视频极速带音频_1973021430713593858.json
name: （自用）Wan2.2 Rapid-AIO-Mega V3.1图生视频极速带音频_1973021430713593858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1973021430713593858.json
hash: ece3c87d0a72819f
coverage: 0.875
learned_at: 2026-10-15 22:32:01
nodes: [ModelSamplingSD3, CLIPTextEncode, WanVaceToVideo, Note, WanVideoVACEStartToEndFrame, ApplySageAttention, Note, Note, CLIPTextEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, KSampler, JWInteger, JWInteger, SaveImage, CR Prompt Text, LayerUtility: PurgeVRAM V2, CheckpointLoaderSimple, VAEDecode, HunyuanVideoFoley, TT_img_enc, LoadImage, SaveImage, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-nsfw-aio-v3.1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 864193246780606, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V3.1图生视频极速带音频_1973021430713593858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1973021430713593858.json`

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
- `JWInteger`
- `JWInteger`
- `SaveImage`
- `CR Prompt Text`
- `LayerUtility: PurgeVRAM V2`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `HunyuanVideoFoley`
- `TT_img_enc`
- `LoadImage`
- `SaveImage`
- `CR Prompt Text`

## 关键参数

- `seed` = `864193246780606`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-nsfw-aio-v3.1.safetensors`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`ApplySageAttention`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`JWInteger`、`SaveImage`、`CR Prompt Text`、`LayerUtility: PurgeVRAM V2`、`CheckpointLoaderSimple`、`VAEDecode`、`HunyuanVideoFoley`、`TT_img_enc`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CR Prompt Text、SaveImage、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
