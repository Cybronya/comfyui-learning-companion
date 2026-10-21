---
key: 图片生成/图生图/Image Replication洗图姿势动作迁移 SeedVR+高清放大_2100745991401070594.json
name: Image Replication洗图姿势动作迁移 SeedVR+高清放大_2100745991401070594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Image Replication洗图姿势动作迁移 SeedVR+高清放大_2100745991401070594.json
hash: b91c886414d10b8f
coverage: 0.833333
learned_at: 2026-10-21 00:40:21
nodes: [CLIPLoader, UNETLoader, PrimitiveNode, PrimitiveInt, VAEEncode, CLIPTextEncode, SamplerCustomAdvanced, VAEDecode, Image Comparer (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, LayerUtility: ImageScaleByAspectRatio V2, AILab_QwenVL, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, Int, SaveImage, SaveImage, VAELoader, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/Image Replication洗图姿势动作迁移 SeedVR+高清放大_2100745991401070594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Image Replication洗图姿势动作迁移 SeedVR+高清放大_2100745991401070594.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `PrimitiveNode`
- `PrimitiveInt`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AILab_QwenVL`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `Int`
- `SaveImage`
- `SaveImage`
- `VAELoader`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAEEncode`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`LayerUtility: ImageScaleByAspectRatio V2`、`AILab_QwenVL`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`Int`、`SaveImage`、`VAELoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
