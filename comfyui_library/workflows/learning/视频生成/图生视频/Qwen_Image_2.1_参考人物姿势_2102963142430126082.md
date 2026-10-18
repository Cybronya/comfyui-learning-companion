---
key: 视频生成/图生视频/Qwen_Image_2.1_参考人物姿势_2102963142430126082.json
name: Qwen_Image_2.1_参考人物姿势_2102963142430126082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1_参考人物姿势_2102963142430126082.json
hash: e86ad58a0df723bf
coverage: 0.809524
learned_at: 2026-10-17 02:29:18
nodes: [QwenImage21Cache, UNETLoader, CLIPLoader, CR Prompt Text, VAEDecode, easy cleanGpuUsed, KSampler, SaveImage, Note, QwenPERewriteT8, easy showAnything, TextEncodeQwenImage21, ComfySwitchNode, EmptyLatentImage, LoadImage, ResolutionSelector, LoadImage, VAELoader, AIO_Preprocessor, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 视频生成/图生视频/Qwen_Image_2.1_参考人物姿势_2102963142430126082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1_参考人物姿势_2102963142430126082.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `SaveImage`
- `Note`
- `QwenPERewriteT8`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `VAELoader`
- `AIO_Preprocessor`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `seed` = `19960422`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`QwenImage21Cache`、`UNETLoader`、`CLIPLoader`、`CR Prompt Text`、`VAEDecode`、`easy cleanGpuUsed`、`KSampler`、`SaveImage`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`LoadImage`、`ResolutionSelector`、`VAELoader`、`AIO_Preprocessor`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
