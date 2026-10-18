---
key: 视频生成/图生视频/AIO-mega-v9-Wan2.2_fast_图生视频_1981747829813190657.json
name: AIO-mega-v9-Wan2.2_fast_图生视频_1981747829813190657.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AIO-mega-v9-Wan2.2_fast_图生视频_1981747829813190657.json
hash: 571024b9514427f2
coverage: 0.823529
learned_at: 2026-10-15 22:32:38
nodes: [ModelSamplingSD3, WanVaceToVideo, CLIPTextEncode, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, LoadImage, KSampler, VAEDecode, DF_Integer, PrimitiveInt, DF_Integer, WanVideoVACEStartToEndFrame, CheckpointLoaderSimple, SimpleMath+, VHS_VideoCombine, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v9.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "beta", "seed": 6456545463549, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/AIO-mega-v9-Wan2.2_fast_图生视频_1981747829813190657.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981747829813190657.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `ModelSamplingSD3`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `DF_Integer`
- `PrimitiveInt`
- `DF_Integer`
- `WanVideoVACEStartToEndFrame`
- `CheckpointLoaderSimple` ★核心
- `SimpleMath+`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `6456545463549`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v9.safetensors`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`ModelSamplingSD3`、`WanVaceToVideo`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`KSampler`、`VAEDecode`、`DF_Integer`、`WanVideoVACEStartToEndFrame`、`CheckpointLoaderSimple`、`SimpleMath+`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、DF_Integer、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
