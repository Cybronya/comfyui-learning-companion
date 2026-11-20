---
key: 图片生成/图生图/多图换装丨Qwen Image 2.1丨服饰搭配·姿态参考_2113116714740305921.json
name: 多图换装丨Qwen Image 2.1丨服饰搭配·姿态参考_2113116714740305921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多图换装丨Qwen Image 2.1丨服饰搭配·姿态参考_2113116714740305921.json
hash: d59e772e772b69c5
coverage: 0.76
learned_at: 2026-11-02 19:14:24
nodes: [LoadImage, CLIPLoader, VAELoader, UNETLoader, ResolutionSelector, ResolutionSelector, LoadImage, ResolutionSelector, Fast Groups Muter (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Prompt Text, CR Prompt Text, CLIPLoader, CLIPLoader, CR Prompt Text, PrimitiveStringMultiline, EmptyLatentImage, EmptyLatentImage, EmptyLatentImage, QwenImage21Cache, TextGenerate, TextGenerate, BatchImagesNode, TextGenerate, ComfySwitchNode, ComfySwitchNode, TextEncodeQwenImage21, TextEncodeQwenImage21, ShowText|pysssss, easy showAnything, ComfySwitchNode, ComfySwitchNode, TextEncodeQwenImage21, KSampler, PreviewAny, VAEDecode, KSampler, ComfySwitchNode, VAEDecode, KSampler, SaveImage, Image Comparer (rgthree), VAEDecode, SaveImage, Image Comparer (rgthree), SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2016, "sampler_name": "euler", "scheduler": "simple", "seed": 985625657145008, "steps": 40, "width": 1152}
---

# 图片生成/图生图/多图换装丨Qwen Image 2.1丨服饰搭配·姿态参考_2113116714740305921.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多图换装丨Qwen Image 2.1丨服饰搭配·姿态参考_2113116714740305921.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `ResolutionSelector`
- `LoadImage`
- `ResolutionSelector`
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `CLIPLoader`
- `CLIPLoader`
- `CR Prompt Text`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `TextGenerate`
- `TextGenerate`
- `BatchImagesNode`
- `TextGenerate`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `ShowText|pysssss`
- `easy showAnything`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `PreviewAny`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`

## 关键参数

- `width` = `1152`
- `height` = `2016`
- `batch_size` = `1`
- `seed` = `985625657145008`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（38/50）

**有卡**：`LoadImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ResolutionSelector`、`CR Prompt Text`、`EmptyLatentImage`、`QwenImage21Cache`、`TextGenerate`、`BatchImagesNode`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
