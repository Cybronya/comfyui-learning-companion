---
key: 图片生成/文生图/文生图+LoRA 1.2.1.1_2047562720291065858.json
name: 文生图+LoRA 1.2.1.1_2047562720291065858
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图+LoRA 1.2.1.1_2047562720291065858.json
hash: 666c7e658e8df4c3
coverage: 0.451049
learned_at: 2026-10-21 03:00:32
nodes: [SetNode, GetNode, ImageScaleBy, LatentUpscale, VAEDecode, VAEDecode, GetNode, GetNode, KSampler, CheckpointLoaderSimple, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, CR Apply LoRA Stack, SetNode, CR LoRA Stack, CR LoRA Stack, SetNode, SetNode, VAELoader, EmptyLatentImage, SetNode, SaveImage, SetNode, SetNode, GetNode, GetNode, CR LoRA Stack, SetNode, CLIPTextEncode, SetNode, CR LoRA Stack, SetNode, SetNode, LayerUtility: TextJoinV2, GetNode, LayerUtility: TextJoinV2, GetNode, SetNode, LatentUpscale, VAEDecode, VAEDecode, SetNode, GetNode, GetNode, KSampler, CR Apply LoRA Stack, SaveImage, GetNode, GetNode, CLIPTextEncode, KSampler, CLIPTextEncode, ImageScaleBy, GetNode, LayerUtility: TextJoinV2, SetNode, CR LoRA Stack, GetNode, SetNode, LatentUpscale, VAEDecode, SetNode, GetNode, GetNode, GetNode, KSampler, CR Apply LoRA Stack, SaveImage, GetNode, GetNode, KSampler, CLIPTextEncode, GetNode, LayerUtility: TextJoinV2, CLIPTextEncode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, ImageScaleBy, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, LatentUpscale, VAEDecode, SetNode, GetNode, GetNode, GetNode, KSampler, CR Apply LoRA Stack, SaveImage, GetNode, GetNode, KSampler, CLIPTextEncode, GetNode, LayerUtility: TextJoinV2, CLIPTextEncode, SetNode, SetNode, GetNode, GetNode, GetNode, VAEDecode, ImageScaleBy, GetNode, GetNode, GetNode, Int, CR Prompt Text, CR LoRA Stack, CR Prompt Text, SetNode, LatentUpscale, VAEDecode, SetNode, GetNode, GetNode, GetNode, KSampler, CR Apply LoRA Stack, SaveImage, GetNode, GetNode, KSampler, CLIPTextEncode, GetNode, LayerUtility: TextJoinV2, CLIPTextEncode, SetNode, SetNode, GetNode, GetNode, GetNode, VAEDecode, ImageScaleBy, CR LoRA Stack, SetNode, LatentUpscale, VAEDecode, SetNode, GetNode, GetNode, GetNode, KSampler, CR Apply LoRA Stack, SaveImage, GetNode, GetNode, KSampler, CLIPTextEncode, GetNode, LayerUtility: TextJoinV2, CLIPTextEncode, SetNode, SetNode, GetNode, GetNode, GetNode, VAEDecode, ImageScaleBy, CR LoRA Stack, CR Prompt Text, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CR Prompt Text, SetNode, LatentUpscale, VAEDecode, SetNode, GetNode, GetNode, GetNode, KSampler, CR Apply LoRA Stack, SaveImage, GetNode, GetNode, KSampler, CLIPTextEncode, GetNode, LayerUtility: TextJoinV2, CLIPTextEncode, SetNode, SetNode, GetNode, GetNode, GetNode, VAEDecode, ImageScaleBy, CR LoRA Stack, CR Prompt Text, GetNode, GetNode, GetNode, SetNode, LatentUpscale, VAEDecode, SetNode, GetNode, GetNode, GetNode, KSampler, CR Apply LoRA Stack, SaveImage, GetNode, GetNode, KSampler, CLIPTextEncode, GetNode, LayerUtility: TextJoinV2, CLIPTextEncode, SetNode, SetNode, GetNode, GetNode, GetNode, VAEDecode, ImageScaleBy, CR LoRA Stack, CR Prompt Text, GetNode, GetNode, GetNode, SetNode, LatentUpscale, VAEDecode, SetNode, GetNode, GetNode, GetNode, KSampler, CR Apply LoRA Stack, SaveImage, GetNode, GetNode, KSampler, CLIPTextEncode, GetNode, LayerUtility: TextJoinV2, CLIPTextEncode, SetNode, SetNode, GetNode, GetNode, GetNode, VAEDecode, ImageScaleBy, CR LoRA Stack, GetNode, GetNode, GetNode, Int, SetNode, Int, CR LoRA Stack, CR Prompt Text, CR Prompt Text, Fast Groups Muter (rgthree), CLIPTextEncode, CR Prompt Text, CR Prompt Text, CR Prompt Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 3, "cfg": 3, "checkpoint": "waiNSFWIllustrious_v140.safetensors", "denoise": 1, "height": 512, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 150499559626019, "steps": 30, "width": 512}
---

# 图片生成/文生图/文生图+LoRA 1.2.1.1_2047562720291065858.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图+LoRA 1.2.1.1_2047562720291065858.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（286 个）：
- `SetNode`
- `GetNode`
- `ImageScaleBy`
- `LatentUpscale`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CR Apply LoRA Stack`
- `SetNode`
- `CR LoRA Stack`
- `CR LoRA Stack`
- `SetNode`
- `SetNode`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `SetNode`
- `SaveImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CR LoRA Stack`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `CR LoRA Stack`
- `SetNode`
- `SetNode`
- `LayerUtility: TextJoinV2`
- `GetNode`
- `LayerUtility: TextJoinV2`
- `GetNode`
- `SetNode`
- `LatentUpscale`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CR Apply LoRA Stack`
- `SaveImage`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ImageScaleBy`
- `GetNode`
- `LayerUtility: TextJoinV2`
- `SetNode`
- `CR LoRA Stack`
- `GetNode`
- `SetNode`
- `LatentUpscale`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CR Apply LoRA Stack`
- `SaveImage`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `LayerUtility: TextJoinV2`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LatentUpscale`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CR Apply LoRA Stack`
- `SaveImage`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `LayerUtility: TextJoinV2`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `CR Prompt Text`
- `CR LoRA Stack`
- `CR Prompt Text`
- `SetNode`
- `LatentUpscale`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CR Apply LoRA Stack`
- `SaveImage`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `LayerUtility: TextJoinV2`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `CR LoRA Stack`
- `SetNode`
- `LatentUpscale`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CR Apply LoRA Stack`
- `SaveImage`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `LayerUtility: TextJoinV2`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `CR LoRA Stack`
- `CR Prompt Text`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Prompt Text`
- `SetNode`
- `LatentUpscale`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CR Apply LoRA Stack`
- `SaveImage`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `LayerUtility: TextJoinV2`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `CR LoRA Stack`
- `CR Prompt Text`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LatentUpscale`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CR Apply LoRA Stack`
- `SaveImage`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `LayerUtility: TextJoinV2`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `CR LoRA Stack`
- `CR Prompt Text`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LatentUpscale`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CR Apply LoRA Stack`
- `SaveImage`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `LayerUtility: TextJoinV2`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `CR LoRA Stack`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `SetNode`
- `Int`
- `CR LoRA Stack`
- `CR Prompt Text`
- `CR Prompt Text`
- `Fast Groups Muter (rgthree)`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `150499559626019`
- `steps` = `30`
- `cfg` = `3`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `waiNSFWIllustrious_v140.safetensors`
- `width` = `512`
- `height` = `512`
- `batch_size` = `3`

## 知识

覆盖率 **45%**（129/286）

**有卡**：`ImageScaleBy`、`LatentUpscale`、`VAEDecode`、`KSampler`、`CheckpointLoaderSimple`、`CR Apply LoRA Stack`、`CR LoRA Stack`、`VAELoader`、`EmptyLatentImage`、`SaveImage`、`CLIPTextEncode`、`LayerUtility: TextJoinV2`、`Int`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、CR Apply LoRA Stack、CR LoRA Stack
