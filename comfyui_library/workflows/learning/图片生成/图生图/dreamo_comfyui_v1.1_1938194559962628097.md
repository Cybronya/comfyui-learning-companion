---
key: 图片生成/图生图/dreamo_comfyui_v1.1_1938194559962628097.json
name: dreamo_comfyui_v1.1_1938194559962628097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/dreamo_comfyui_v1.1_1938194559962628097.json
hash: 6666d054ac40930e
coverage: 0.909091
learned_at: 2026-10-23 11:34:38
nodes: [DualCLIPLoader, CLIPTextEncode, VAEDecode, UNETLoader, FluxGuidance, VAELoader, ApplyDreamO, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, EmptySD3LatentImage, SaveImage, PreviewImage, DreamORefEncode, DreamOProcessorLoader, PrimitiveNode, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 386712261816250, "steps": 20}
---

# 图片生成/图生图/dreamo_comfyui_v1.1_1938194559962628097.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/dreamo_comfyui_v1.1_1938194559962628097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `FluxGuidance`
- `VAELoader`
- `ApplyDreamO`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `SaveImage`
- `PreviewImage`
- `DreamORefEncode`
- `DreamOProcessorLoader`
- `PrimitiveNode`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

## 关键参数

- `seed` = `386712261816250`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`DualCLIPLoader`、`CLIPTextEncode`、`VAEDecode`、`UNETLoader`、`FluxGuidance`、`VAELoader`、`ApplyDreamO`、`LoraLoaderModelOnly`、`EmptySD3LatentImage`、`SaveImage`、`DreamORefEncode`、`DreamOProcessorLoader`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
