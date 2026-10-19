---
key: 图片生成/文生图/comfyui_career_autodress_img2img222_1994612041421819905.json
name: comfyui_career_autodress_img2img222_1994612041421819905
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/comfyui_career_autodress_img2img222_1994612041421819905.json
hash: 7d9d9b84c6832d78
coverage: 0.857143
learned_at: 2026-10-19 21:33:10
nodes: [KSampler, EmptyLatentImage, VAEDecode, SaveImage, CheckpointLoaderSimple, IPAdapterUnifiedLoader, IPAdapter, CLIPTextEncode, CLIPTextEncode, LoadImage, LmcqDeepLoader, PrimitiveNode, LmcqDeepGen, ShowText|pysssss]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "juggernautXL_v9-Lightning_4S_V9 + RDPhoto 2.safetensors", "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 277436192846257, "steps": 30, "width": 1024}
---

# 图片生成/文生图/comfyui_career_autodress_img2img222_1994612041421819905.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/comfyui_career_autodress_img2img222_1994612041421819905.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（14 个）：
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `IPAdapterUnifiedLoader`
- `IPAdapter`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LmcqDeepLoader`
- `PrimitiveNode`
- `LmcqDeepGen`
- `ShowText|pysssss`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `277436192846257`
- `steps` = `30`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `checkpoint` = `juggernautXL_v9-Lightning_4S_V9 + RDPhoto 2.safetensors`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`KSampler`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`CheckpointLoaderSimple`、`IPAdapterUnifiedLoader`、`IPAdapter`、`CLIPTextEncode`、`LoadImage`、`LmcqDeepLoader`、`LmcqDeepGen`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、IPAdapterUnifiedLoader、IPAdapter
