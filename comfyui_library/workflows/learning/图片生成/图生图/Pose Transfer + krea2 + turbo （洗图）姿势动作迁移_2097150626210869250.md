---
key: 图片生成/图生图/Pose Transfer + krea2 + turbo （洗图）姿势动作迁移_2097150626210869250.json
name: Pose Transfer + krea2 + turbo （洗图）姿势动作迁移_2097150626210869250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Pose Transfer + krea2 + turbo （洗图）姿势动作迁移_2097150626210869250.json
hash: d1cc405eab037e12
coverage: 0.833333
learned_at: 2026-10-21 00:41:52
nodes: [CLIPLoader, UNETLoader, PrimitiveNode, PrimitiveInt, VAEEncode, CLIPTextEncode, SamplerCustomAdvanced, VAEDecode, Image Comparer (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, LayerUtility: ImageScaleByAspectRatio V2, AILab_QwenVL, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, Int, SaveImage, SaveImage, VAELoader, Fast Groups Bypasser (rgthree), LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/Pose Transfer + krea2 + turbo （洗图）姿势动作迁移_2097150626210869250.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Pose Transfer + krea2 + turbo （洗图）姿势动作迁移_2097150626210869250.json`

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
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAEEncode`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`LayerUtility: ImageScaleByAspectRatio V2`、`AILab_QwenVL`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`Int`、`SaveImage`、`VAELoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
