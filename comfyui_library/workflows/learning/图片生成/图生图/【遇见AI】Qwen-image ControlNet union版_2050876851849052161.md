---
key: 图片生成/图生图/【遇见AI】Qwen-image ControlNet union版_2050876851849052161.json
name: 【遇见AI】Qwen-image ControlNet union版_2050876851849052161
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】Qwen-image ControlNet union版_2050876851849052161.json
hash: 511fc748f5ff1864
coverage: 0.894737
learned_at: 2026-10-23 11:52:08
nodes: [PreviewImage, VAEDecode, SaveImage, CFGNorm, TextEncodeQwenImageEditPlus, ModelSamplingAuraFlow, KSampler, AIO_Preprocessor, TextEncodeQwenImageEditPlus, VAEEncode, ControlNetApplySD3, Note, LoadImage, LoadImage, ControlNetLoader, LoadImage, UNETLoader, CLIPLoader, VAELoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "controlnet_strength": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 73286214966507, "steps": 40}
---

# 图片生成/图生图/【遇见AI】Qwen-image ControlNet union版_2050876851849052161.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】Qwen-image ControlNet union版_2050876851849052161.json`

## 结构

**生成流程**：Model → Encode → Control → Sampling → Decode → Output → Other

**节点**（19 个）：
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `AIO_Preprocessor`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `ControlNetApplySD3` ★核心
- `Note`
- `LoadImage`
- `LoadImage`
- `ControlNetLoader`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `73286214966507`
- `steps` = `40`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`VAEDecode`、`SaveImage`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`ModelSamplingAuraFlow`、`KSampler`、`AIO_Preprocessor`、`VAEEncode`、`ControlNetApplySD3`、`LoadImage`、`ControlNetLoader`、`UNETLoader`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、ControlNetLoader、ControlNetApplySD3
