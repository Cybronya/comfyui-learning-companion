---
key: 图片生成/文生图/Anima+2.9b+vs+Anima base+生图_2089681885474680834.json
name: Anima+2.9b+vs+Anima base+生图_2089681885474680834
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima+2.9b+vs+Anima base+生图_2089681885474680834.json
hash: 0297235b9c025437
coverage: 0.848485
learned_at: 2026-10-20 00:58:38
nodes: [VAELoader, CLIPLoader, CLIPTextEncode, VAEDecode, Fast Groups Bypasser (rgthree), Note, ModelSamplingAuraFlow, PreviewAny, LayerUtility: TextJoin, VAELoader, CLIPLoader, CLIPTextEncode, EmptyLatentImage, ModelSamplingAuraFlow, CLIPTextEncode, VAEDecode, SaveImage, KSampler, Text, CLIPTextEncode, EmptyLatentImage, UNETLoader, UNETLoader, SaveImage, SaveImage, ImageConcanate, AddLabel, KSampler, PrimitiveInt, PrimitiveInt, AddLabel, AddLabel, Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 5, "denoise": 1, "height": 1536, "sampler_name": "er_sde", "scheduler": "simple", "seed": 666, "steps": 30, "width": 920}
---

# 图片生成/文生图/Anima+2.9b+vs+Anima base+生图_2089681885474680834.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima+2.9b+vs+Anima base+生图_2089681885474680834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `LayerUtility: TextJoin`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `Text`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `SaveImage`
- `ImageConcanate`
- `AddLabel`
- `KSampler` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `AddLabel`
- `AddLabel`
- `Text`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `920`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `666`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`VAEDecode`、`ModelSamplingAuraFlow`、`LayerUtility: TextJoin`、`EmptyLatentImage`、`SaveImage`、`KSampler`、`Text`、`UNETLoader`、`ImageConcanate`、`AddLabel`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage
