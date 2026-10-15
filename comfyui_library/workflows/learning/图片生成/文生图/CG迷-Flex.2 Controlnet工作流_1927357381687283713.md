---
key: 图片生成/文生图/CG迷-Flex.2 Controlnet工作流_1927357381687283713.json
name: CG迷-Flex.2 Controlnet工作流_1927357381687283713
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/CG迷-Flex.2 Controlnet工作流_1927357381687283713.json
hash: e7669b3d5ac8efbf
coverage: 0.761905
learned_at: 2026-10-10 21:26:36
nodes: [PreviewImage, Florence2Run, ShowText|pysssss, AIO_Preprocessor, PreviewImage, DualCLIPLoader, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, VAEDecode, KSampler, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, Flex2Conditioner, Flex2Conditioner, AIO_Preprocessor, MarkdownNote, Florence2ModelLoader, LoadImage, VAELoader, UNETLoader]
patterns: [text_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 896, "sampler_name": "deis", "scheduler": "beta", "seed": 990138665214536, "steps": 28, "width": 1344}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/CG迷-Flex.2 Controlnet工作流_1927357381687283713.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/CG迷-Flex.2 Controlnet工作流_1927357381687283713.json`

## 结构

**节点**（21 个）：
- `PreviewImage`
- `Florence2Run`
- `ShowText|pysssss`
- `AIO_Preprocessor`
- `PreviewImage`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `VAEDecode`
- `KSampler`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Flex2Conditioner`
- `Flex2Conditioner`
- `AIO_Preprocessor`
- `MarkdownNote`
- `Florence2ModelLoader`
- `LoadImage`
- `VAELoader`
- `UNETLoader`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `896`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `seed` = `990138665214536`
- `steps` = `28`
- `width` = `1344`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`PreviewImage`、`Florence2Run`、`ShowText|pysssss`、`AIO_Preprocessor`、`DualCLIPLoader`、`EmptyLatentImage`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Flex2Conditioner`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
