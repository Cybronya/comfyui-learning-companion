---
key: 图片生成/图生图/图片加细节变真实 真实美女图片制作 Flux upscale-Detail Daemon_1914151169525252098.json
name: 图片加细节变真实 真实美女图片制作 Flux upscale-Detail Daemon_1914151169525252098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片加细节变真实 真实美女图片制作 Flux upscale-Detail Daemon_1914151169525252098.json
hash: e2c6e2007aa7b45e
coverage: 0.8125
learned_at: 2026-10-23 12:40:12
nodes: [KSamplerSelect, VAELoader, ConditioningZeroOut, CLIPTextEncodeFlux, ModelSamplingFlux, BasicScheduler, UltimateSDUpscaleCustomSample, UpscaleModelLoader, UnetLoaderGGUF, DualCLIPLoaderGGUF, SaveImage, Image Comparer (rgthree), DetailDaemonSamplerNode, LoadImage, PrimitiveFloat, Note]
patterns: []
missing: []
---

# 图片生成/图生图/图片加细节变真实 真实美女图片制作 Flux upscale-Detail Daemon_1914151169525252098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片加细节变真实 真实美女图片制作 Flux upscale-Detail Daemon_1914151169525252098.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（16 个）：
- `KSamplerSelect` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `CLIPTextEncodeFlux` ★核心
- `ModelSamplingFlux`
- `BasicScheduler`
- `UltimateSDUpscaleCustomSample`
- `UpscaleModelLoader`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoaderGGUF`
- `SaveImage`
- `Image Comparer (rgthree)`
- `DetailDaemonSamplerNode` ★核心
- `LoadImage`
- `PrimitiveFloat`
- `Note`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`KSamplerSelect`、`VAELoader`、`ConditioningZeroOut`、`CLIPTextEncodeFlux`、`ModelSamplingFlux`、`BasicScheduler`、`UltimateSDUpscaleCustomSample`、`UpscaleModelLoader`、`UnetLoaderGGUF`、`DualCLIPLoaderGGUF`、`SaveImage`、`DetailDaemonSamplerNode`、`LoadImage`

**用到的条目**：VAELoader、ConditioningZeroOut、LoadImage、DetailDaemonSamplerNode、KSamplerSelect、CLIPTextEncodeFlux、ModelSamplingFlux、UpscaleModelLoader
