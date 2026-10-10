---
key: Qwen-Image-2.1 + LoRA 文生图 高清放大2k直出工作流_2104799390119579649.json
name: Qwen-Image-2.1 + LoRA 文生图 高清放大2k直出工作流_2104799390119579649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 + LoRA 文生图 高清放大2k直出工作流_2104799390119579649.json
hash: 0fc49df5748ee4da
coverage: 0.727273
learned_at: 2026-10-10 20:59:00
nodes: [EmptyLatentImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, CLIPLoader, VAELoader, TextEncodeQwenImage21, Seed (rgthree), UNETLoader, VAEDecode, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, KSampler, ResolutionSelector, PrimitiveStringMultiline, SaveImage, DF_Integer, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, SeedVR2LoadVAEModel, SaveImage, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree)]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 104424259736900, "steps": 35, "width": 1024}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# Qwen-Image-2.1 + LoRA 文生图 高清放大2k直出工作流_2104799390119579649.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 + LoRA 文生图 高清放大2k直出工作流_2104799390119579649.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `KSampler` ★核心
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `SaveImage`
- `DF_Integer`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `104424259736900`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（16/22）

**有卡**：`EmptyLatentImage`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`UNETLoader`、`VAEDecode`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`KSampler`、`ResolutionSelector`、`SaveImage`、`DF_Integer`、`SeedVR2LoadVAEModel`

**缺卡**（3）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
