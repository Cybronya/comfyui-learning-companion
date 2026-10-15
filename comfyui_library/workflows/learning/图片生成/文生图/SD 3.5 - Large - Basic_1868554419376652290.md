---
key: 图片生成/文生图/SD 3.5 - Large - Basic_1868554419376652290.json
name: SD 3.5 - Large - Basic_1868554419376652290
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD 3.5 - Large - Basic_1868554419376652290.json
hash: fb49327a1ad364e3
coverage: 0.928571
learned_at: 2026-10-10 20:59:10
nodes: [ModelSamplingSD3, KSampler, VAEDecode, PreviewImage, SaveImage, CLIPTextEncode, ConditioningZeroOut, ConditioningSetTimestepRange, ConditioningCombine, ConditioningSetTimestepRange, EmptyLatentImage, CheckpointLoaderSimple, TripleCLIPLoader, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "sd3.5_large.safetensors", "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 115937863918748, "steps": 50, "width": 1024}
---

# 图片生成/文生图/SD 3.5 - Large - Basic_1868554419376652290.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD 3.5 - Large - Basic_1868554419376652290.json`

## 结构

**节点**（14 个）：
- `ModelSamplingSD3`
- `KSampler`
- `VAEDecode`
- `PreviewImage`
- `SaveImage`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConditioningSetTimestepRange`
- `ConditioningCombine`
- `ConditioningSetTimestepRange`
- `EmptyLatentImage`
- `CheckpointLoaderSimple`
- `TripleCLIPLoader`
- `CLIPTextEncode`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `checkpoint` = `sd3.5_large.safetensors`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `seed` = `115937863918748`
- `steps` = `50`
- `width` = `1024`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`ModelSamplingSD3`、`KSampler`、`VAEDecode`、`PreviewImage`、`SaveImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`ConditioningSetTimestepRange`、`ConditioningCombine`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`TripleCLIPLoader`
