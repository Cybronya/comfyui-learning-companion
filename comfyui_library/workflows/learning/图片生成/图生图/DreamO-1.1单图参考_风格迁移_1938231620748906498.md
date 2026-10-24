---
key: 图片生成/图生图/DreamO-1.1单图参考_风格迁移_1938231620748906498.json
name: DreamO-1.1单图参考_风格迁移_1938231620748906498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/DreamO-1.1单图参考_风格迁移_1938231620748906498.json
hash: b390681c4ef82bd0
coverage: 0.954545
learned_at: 2026-10-23 10:52:23
nodes: [DualCLIPLoader, CLIPTextEncode, FluxGuidance, KSampler, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, VAELoader, DreamOProcessorLoader, ApplyDreamO, PreviewImage, VAEDecode, LoadImage, SaveImage, SaveImage, ImageConcatMulti, CR SDXL Aspect Ratio, LoraLoaderModelOnly, DreamORefEncode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 40, "steps": 12}
---

# 图片生成/图生图/DreamO-1.1单图参考_风格迁移_1938231620748906498.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/DreamO-1.1单图参考_风格迁移_1938231620748906498.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `DreamOProcessorLoader`
- `ApplyDreamO`
- `PreviewImage`
- `VAEDecode` ★核心
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `ImageConcatMulti`
- `CR SDXL Aspect Ratio`
- `LoraLoaderModelOnly` ★核心
- `DreamORefEncode`

## 关键参数

- `seed` = `40`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`DualCLIPLoader`、`CLIPTextEncode`、`FluxGuidance`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`DreamOProcessorLoader`、`ApplyDreamO`、`VAEDecode`、`LoadImage`、`SaveImage`、`ImageConcatMulti`、`CR SDXL Aspect Ratio`、`DreamORefEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
