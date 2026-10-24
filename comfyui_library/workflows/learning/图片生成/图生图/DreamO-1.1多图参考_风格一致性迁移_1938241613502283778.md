---
key: 图片生成/图生图/DreamO-1.1多图参考_风格一致性迁移_1938241613502283778.json
name: DreamO-1.1多图参考_风格一致性迁移_1938241613502283778
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/DreamO-1.1多图参考_风格一致性迁移_1938241613502283778.json
hash: 06b8fa2efbbf680b
coverage: 0.896552
learned_at: 2026-10-23 10:52:23
nodes: [DualCLIPLoader, CLIPTextEncode, FluxGuidance, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, CR SDXL Aspect Ratio, LoraLoaderModelOnly, LoadImage, PreviewImage, PreviewImage, ApplyDreamO, CLIPTextEncode, VAEDecode, SaveImage, ImageConcatMulti, KSampler, LoadImage, PreviewImage, VAELoader, DreamOProcessorLoader, LoadImage, DreamORefEncode, ImageConcatMulti, DreamORefEncode, DreamORefEncode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "ays+", "seed": 506576813087008, "steps": 12}
---

# 图片生成/图生图/DreamO-1.1多图参考_风格一致性迁移_1938241613502283778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/DreamO-1.1多图参考_风格一致性迁移_1938241613502283778.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `CR SDXL Aspect Ratio`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `ApplyDreamO`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageConcatMulti`
- `KSampler` ★核心
- `LoadImage`
- `PreviewImage`
- `VAELoader`
- `DreamOProcessorLoader`
- `LoadImage`
- `DreamORefEncode`
- `ImageConcatMulti`
- `DreamORefEncode`
- `DreamORefEncode`

## 关键参数

- `seed` = `506576813087008`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `ays+`
- `denoise` = `1`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`DualCLIPLoader`、`CLIPTextEncode`、`FluxGuidance`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`CR SDXL Aspect Ratio`、`LoadImage`、`ApplyDreamO`、`VAEDecode`、`ImageConcatMulti`、`KSampler`、`VAELoader`、`DreamOProcessorLoader`、`DreamORefEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
