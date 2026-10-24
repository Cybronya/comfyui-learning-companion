---
key: 图片生成/图生图/Dark daze art（Z-image-dazz）_1998590663778271234.json
name: Dark daze art（Z-image-dazz）_1998590663778271234
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Dark daze art（Z-image-dazz）_1998590663778271234.json
hash: d23405a02cad7e15
coverage: 0.866667
learned_at: 2026-10-23 10:52:16
nodes: [KSampler, VAEDecode, UNETLoader, ConditioningZeroOut, MuyeSizeSelector, CLIPTextEncode, LayerUtility: TextJoinV2, VAELoader, SaveImage, LoraLoaderModelOnly, PrimitiveStringMultiline, PrimitiveStringMultiline, CLIPLoader, EmptyLatentImage, Primitive integer [Crystools]]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 209830424637852, "steps": 10, "width": 1080}
---

# 图片生成/图生图/Dark daze art（Z-image-dazz）_1998590663778271234.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Dark daze art（Z-image-dazz）_1998590663778271234.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `MuyeSizeSelector`
- `CLIPTextEncode` ★核心
- `LayerUtility: TextJoinV2`
- `VAELoader`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `Primitive integer [Crystools]`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `209830424637852`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`KSampler`、`VAEDecode`、`UNETLoader`、`ConditioningZeroOut`、`MuyeSizeSelector`、`CLIPTextEncode`、`LayerUtility: TextJoinV2`、`VAELoader`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPLoader`、`EmptyLatentImage`、`Primitive integer [Crystools]`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
