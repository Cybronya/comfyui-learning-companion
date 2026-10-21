---
key: 图片生成/图生图/Qwen_Image_2_1_Outpainting 图像外绘编辑+自然曝光Lora工作流_2104584979157180417.json
name: Qwen_Image_2_1_Outpainting 图像外绘编辑+自然曝光Lora工作流_2104584979157180417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2_1_Outpainting 图像外绘编辑+自然曝光Lora工作流_2104584979157180417.json
hash: 957d512956a9176d
coverage: 0.705882
learned_at: 2026-10-21 00:43:58
nodes: [VAEDecode, TextEncodeQwenImage21, Label (rgthree), UNETLoader, LoraLoaderModelOnly, VAELoader, KSampler, SaveImage, LoadImage, Textbox, CLIPLoader, ImagePadKJ, PreviewImage, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 343498791723066, "steps": 40}
---

# 图片生成/图生图/Qwen_Image_2_1_Outpainting 图像外绘编辑+自然曝光Lora工作流_2104584979157180417.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2_1_Outpainting 图像外绘编辑+自然曝光Lora工作流_2104584979157180417.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `Label (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `Textbox`
- `CLIPLoader`
- `ImagePadKJ`
- `PreviewImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`

## 关键参数

- `seed` = `343498791723066`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（12/17）

**有卡**：`VAEDecode`、`TextEncodeQwenImage21`、`Label (rgthree)`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`KSampler`、`SaveImage`、`LoadImage`、`Textbox`、`CLIPLoader`、`ImagePadKJ`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
