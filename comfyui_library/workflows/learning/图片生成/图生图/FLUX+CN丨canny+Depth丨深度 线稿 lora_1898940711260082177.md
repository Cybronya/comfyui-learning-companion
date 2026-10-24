---
key: 图片生成/图生图/FLUX+CN丨canny+Depth丨深度 线稿 lora_1898940711260082177.json
name: FLUX+CN丨canny+Depth丨深度 线稿 lora_1898940711260082177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX+CN丨canny+Depth丨深度 线稿 lora_1898940711260082177.json
hash: 77335d0df2fb43fd
coverage: 0.894737
learned_at: 2026-10-23 10:53:39
nodes: [SaveImage, UNETLoader, FluxGuidance, ConditioningZeroOut, InstructPixToPixConditioning, Canny, PreviewImage, LoraLoaderModelOnly, LoraLoaderModelOnly, DepthAnythingPreprocessor, PreviewImage, DualCLIPLoader, VAELoader, DifferentialDiffusion, KSampler, VAEDecode, LoraLoaderModelOnly, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 844333358789971, "steps": 28}
---

# 图片生成/图生图/FLUX+CN丨canny+Depth丨深度 线稿 lora_1898940711260082177.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX+CN丨canny+Depth丨深度 线稿 lora_1898940711260082177.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `SaveImage`
- `UNETLoader` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `InstructPixToPixConditioning`
- `Canny`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DepthAnythingPreprocessor`
- `PreviewImage`
- `DualCLIPLoader`
- `VAELoader`
- `DifferentialDiffusion`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `844333358789971`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`SaveImage`、`UNETLoader`、`FluxGuidance`、`ConditioningZeroOut`、`InstructPixToPixConditioning`、`Canny`、`LoraLoaderModelOnly`、`DepthAnythingPreprocessor`、`DualCLIPLoader`、`VAELoader`、`DifferentialDiffusion`、`KSampler`、`VAEDecode`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
