---
key: 图片生成/图生图/Next Scene V2+QwenAIOV7.1 AI短剧电影分镜自动生成镜头风格一致_1981021578404184066.json
name: Next Scene V2+QwenAIOV7.1 AI短剧电影分镜自动生成镜头风格一致_1981021578404184066
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Next Scene V2+QwenAIOV7.1 AI短剧电影分镜自动生成镜头风格一致_1981021578404184066.json
hash: 55fd5afc724028fb
coverage: 0.882353
learned_at: 2026-10-23 11:09:51
nodes: [TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, VAEDecode, LayerUtility: PurgeVRAM V2, VAEEncode, LoadImage, JjkText, easy showAnything, RHHiddenNodes, CheckpointLoaderSimple, LoraLoaderModelOnly, RHHiddenNodes, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, Int, Int]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v7.1.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "simple", "seed": 290391012364761, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Next Scene V2+QwenAIOV7.1 AI短剧电影分镜自动生成镜头风格一致_1981021578404184066.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Next Scene V2+QwenAIOV7.1 AI短剧电影分镜自动生成镜头风格一致_1981021578404184066.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEEncode` ★核心
- `LoadImage`
- `JjkText`
- `easy showAnything`
- `RHHiddenNodes`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `RHHiddenNodes`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `Int`
- `Int`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `290391012364761`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v7.1.safetensors`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`TextEncodeQwenImageEditPlus`、`KSampler`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`VAEEncode`、`LoadImage`、`RHHiddenNodes`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`Int`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、LoadImage、TextEncodeQwenImageEditPlus、VAEEncode、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
