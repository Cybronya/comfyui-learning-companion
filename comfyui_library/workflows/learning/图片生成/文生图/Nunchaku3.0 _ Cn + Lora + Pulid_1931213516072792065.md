---
key: 图片生成/文生图/Nunchaku3.0 _ Cn + Lora + Pulid_1931213516072792065.json
name: Nunchaku3.0 _ Cn + Lora + Pulid_1931213516072792065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Nunchaku3.0 _ Cn + Lora + Pulid_1931213516072792065.json
hash: 2d6f1ce6cfe42899
coverage: 0.666667
learned_at: 2026-10-15 22:26:52
nodes: [VAELoader, EmptyLatentImage, DualCLIPLoader, NunchakuFluxDiTLoader, Anything Everywhere, Anything Everywhere, Anything Everywhere, ControlNetApplyAdvanced, Reroute, workflow>HAOTU-k采样+vae, workflow>HAOTU-k采样+vae, workflow>HAOTU-k采样+vae, Reroute, Reroute, Reroute, NunchakuFluxLoraLoader, Anything Everywhere, NunchakuPulidApply, NunchakuPulidLoader, CropFace, PreviewImage, LoadImage, workflow>HAOTU-k采样+vae, SaveImage, SaveImage, SaveImage, SaveImage, CLIPTextEncode, ControlNetLoader, AIO_Preprocessor, LoadImage, Anything Everywhere, FluxGuidance, CLIPTextEncode, Fast Groups Bypasser (rgthree), JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "controlnet_strength": 0.8000000000000002, "height": 1536, "width": 1024}
---

# 图片生成/文生图/Nunchaku3.0 _ Cn + Lora + Pulid_1931213516072792065.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Nunchaku3.0 _ Cn + Lora + Pulid_1931213516072792065.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Output → Other

**节点**（36 个）：
- `VAELoader`
- `EmptyLatentImage` ★核心
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `ControlNetApplyAdvanced` ★核心
- `Reroute`
- `workflow>HAOTU-k采样+vae`
- `workflow>HAOTU-k采样+vae`
- `workflow>HAOTU-k采样+vae`
- `Reroute`
- `Reroute`
- `Reroute`
- `NunchakuFluxLoraLoader` ★核心
- `Anything Everywhere`
- `NunchakuPulidApply`
- `NunchakuPulidLoader`
- `CropFace`
- `PreviewImage`
- `LoadImage`
- `workflow>HAOTU-k采样+vae`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `AIO_Preprocessor`
- `LoadImage`
- `Anything Everywhere`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `JjkText`

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **67%**（24/36）

**有卡**：`VAELoader`、`EmptyLatentImage`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`ControlNetApplyAdvanced`、`workflow>HAOTU-k采样+vae`、`NunchakuFluxLoraLoader`、`NunchakuPulidApply`、`NunchakuPulidLoader`、`CropFace`、`LoadImage`、`SaveImage`、`CLIPTextEncode`、`ControlNetLoader`、`AIO_Preprocessor`、`FluxGuidance`

**用到的条目**：VAELoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、FluxGuidance、workflow>HAOTU-k采样+vae
