---
key: 图片生成/图生图/▶WAN2.2单底噪局部重绘流_1956285683411374082.json
name: ▶WAN2.2单底噪局部重绘流_1956285683411374082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/▶WAN2.2单底噪局部重绘流_1956285683411374082.json
hash: 92bb187cf8b31cbb
coverage: 0.9
learned_at: 2026-10-23 11:47:26
nodes: [DifferentialDiffusion, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), VAEDecode, InpaintModelConditioning, LoadImage, CLIPTextEncode, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, MaskPreview+, ModelSamplingSD3, ShowText|pysssss, LayerUtility: Florence2Image2Prompt, LayerMask: LoadFlorence2Model, UNETLoader, VAELoader, INPAINT_ExpandMask, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "beta", "seed": 1075897170071637, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/▶WAN2.2单底噪局部重绘流_1956285683411374082.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/▶WAN2.2单底噪局部重绘流_1956285683411374082.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `DifferentialDiffusion`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `InpaintModelConditioning`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `MaskPreview+`
- `ModelSamplingSD3`
- `ShowText|pysssss`
- `LayerUtility: Florence2Image2Prompt`
- `LayerMask: LoadFlorence2Model`
- `UNETLoader` ★核心
- `VAELoader`
- `INPAINT_ExpandMask`
- `KSampler` ★核心

## 关键参数

- `seed` = `1075897170071637`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`DifferentialDiffusion`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`InpaintModelConditioning`、`LoadImage`、`CLIPTextEncode`、`CLIPLoader`、`LoraLoaderModelOnly`、`MaskPreview+`、`ModelSamplingSD3`、`LayerUtility: Florence2Image2Prompt`、`LayerMask: LoadFlorence2Model`、`UNETLoader`、`VAELoader`、`INPAINT_ExpandMask`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
