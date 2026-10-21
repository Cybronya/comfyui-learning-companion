---
key: 图片生成/文生图/Anima Yume1.5测试 对比工作流_2098318586065547265.json
name: Anima Yume1.5测试 对比工作流_2098318586065547265
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima Yume1.5测试 对比工作流_2098318586065547265.json
hash: 2ac8b616cec94693
coverage: 0.816667
learned_at: 2026-10-20 01:34:15
nodes: [Reroute, LayerUtility: ImageReelComposit, CLIPLoader, EmptyLatentImage, VAELoader, VAEDecode, SaveImage, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, VAEDecode, SaveImage, easy promptList, easy promptList, easy promptList, easy mathInt, KSampler, CLIPTextEncode, KSampler, CLIPTextEncode, Reroute, UNETLoader, UNETLoader, Fast Groups Bypasser (rgthree), Reroute, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, SaveImage, KSampler, UNETLoader, easy promptList, Reroute, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, SaveImage, KSampler, ImageOnlyCheckpointLoader, Reroute, Reroute, VAEDecode, VAEDecode, LayerUtility: ImageReel, SaveImage, TTResolutionSelector, Reroute, Reroute, easy promptList, Reroute, easy promptList, easy anythingIndexSwitch, PrimitiveInt, Seed (rgthree)]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "checkpoint": "miaomiaoHarem_anima12.safetensors", "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "beta", "seed": 338144620226380, "steps": 36, "width": 512}
---

# 图片生成/文生图/Anima Yume1.5测试 对比工作流_2098318586065547265.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima Yume1.5测试 对比工作流_2098318586065547265.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `Reroute`
- `LayerUtility: ImageReelComposit`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy mathInt`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `easy promptList`
- `Reroute`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `KSampler` ★核心
- `ImageOnlyCheckpointLoader` ★核心
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `SaveImage`
- `TTResolutionSelector`
- `Reroute`
- `Reroute`
- `easy promptList`
- `Reroute`
- `easy promptList`
- `easy anythingIndexSwitch`
- `PrimitiveInt`
- `Seed (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `338144620226380`
- `steps` = `36`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `miaomiaoHarem_anima12.safetensors`

## 知识

覆盖率 **82%**（49/60）

**有卡**：`LayerUtility: ImageReelComposit`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`easy promptList`、`easy mathInt`、`KSampler`、`UNETLoader`、`ImageOnlyCheckpointLoader`、`LayerUtility: ImageReel`、`TTResolutionSelector`、`easy anythingIndexSwitch`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、Seed (rgthree)
