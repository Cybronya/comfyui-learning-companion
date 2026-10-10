---
key: SD 3.5 - Large - Basic_1868554419376652290.json
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

# SD 3.5 - Large - Basic_1868554419376652290.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD 3.5 - Large - Basic_1868554419376652290.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `ModelSamplingSD3`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ConditioningSetTimestepRange`
- `ConditioningCombine`
- `ConditioningSetTimestepRange`
- `EmptyLatentImage` ★核心
- `CheckpointLoaderSimple` ★核心
- `TripleCLIPLoader`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `115937863918748`
- `steps` = `50`
- `cfg` = `4.5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `checkpoint` = `sd3.5_large.safetensors`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`ModelSamplingSD3`、`KSampler`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`ConditioningSetTimestepRange`、`ConditioningCombine`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`TripleCLIPLoader`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、ConditioningSetTimestepRange、ConditioningCombine
