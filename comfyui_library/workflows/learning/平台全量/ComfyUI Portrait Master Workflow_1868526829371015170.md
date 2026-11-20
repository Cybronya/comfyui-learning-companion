---
key: 平台全量/ComfyUI Portrait Master Workflow_1868526829371015170.json
name: ComfyUI Portrait Master Workflow_1868526829371015170
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/ComfyUI Portrait Master Workflow_1868526829371015170.json
hash: 445356691fa8b92f
coverage: 0.928571
learned_at: 2026-11-14 00:22:18
nodes: [PortraitMasterSkinDetails, PortraitMasterStylePose, ShowText|pysssss, KSampler, CheckpointLoaderSimple, Seed (rgthree), PortraitMasterBaseCharacter, CLIPSetLastLayer, PortraitMasterMakeup, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 1007786533813303, "steps": 30, "width": 1024}
---

# 平台全量/ComfyUI Portrait Master Workflow_1868526829371015170.json

> 来源文件 `comfyui_library/workflows/平台全量/ComfyUI Portrait Master Workflow_1868526829371015170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `PortraitMasterSkinDetails`
- `PortraitMasterStylePose`
- `ShowText|pysssss`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `Seed (rgthree)`
- `PortraitMasterBaseCharacter`
- `CLIPSetLastLayer`
- `PortraitMasterMakeup`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1007786533813303`
- `steps` = `30`
- `cfg` = `4.5`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`PortraitMasterSkinDetails`、`PortraitMasterStylePose`、`KSampler`、`CheckpointLoaderSimple`、`Seed (rgthree)`、`PortraitMasterBaseCharacter`、`CLIPSetLastLayer`、`PortraitMasterMakeup`、`CLIPTextEncode`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、Seed (rgthree)、PortraitMasterStylePose、CLIPSetLastLayer
