---
key: 视频生成/文生视频/Anima-2.9B｜智能图生图_Qwen3VL反推_2089343535781859329.json
name: Anima-2.9B｜智能图生图_Qwen3VL反推_2089343535781859329
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Anima-2.9B｜智能图生图_Qwen3VL反推_2089343535781859329.json
hash: e7afced7cd75be53
coverage: 0.928571
learned_at: 2026-10-11 21:19:37
nodes: [Qwen3VLProcessor, KSampler, VAEDecode, image_scale_pixel_v2, SaveImage, UNETLoader, CLIPTextEncode, CLIPTextEncode, VAEEncode, VAELoaderKJ, CLIPLoader, PathchSageAttentionKJ, LoadImage, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 5, "denoise": 0.7, "sampler_name": "res_multistep", "scheduler": "linear_quadratic", "seed": 440806743335793, "steps": 28}
---

# 视频生成/文生视频/Anima-2.9B｜智能图生图_Qwen3VL反推_2089343535781859329.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Anima-2.9B｜智能图生图_Qwen3VL反推_2089343535781859329.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `Qwen3VLProcessor`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `image_scale_pixel_v2`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAELoaderKJ`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `LoadImage`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `440806743335793`
- `steps` = `28`
- `cfg` = `5`
- `sampler_name` = `res_multistep`
- `scheduler` = `linear_quadratic`
- `denoise` = `0.7`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`Qwen3VLProcessor`、`KSampler`、`VAEDecode`、`image_scale_pixel_v2`、`SaveImage`、`UNETLoader`、`CLIPTextEncode`、`VAEEncode`、`VAELoaderKJ`、`CLIPLoader`、`PathchSageAttentionKJ`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode、VAELoaderKJ
