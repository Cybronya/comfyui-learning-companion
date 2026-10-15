---
key: 图片生成/文生图/Wan 2.2 文生图工作流 免费课程对应工作流RunningHub在线运行版_1953741553124691969.json
name: Wan 2.2 文生图工作流 免费课程对应工作流RunningHub在线运行版_1953741553124691969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan 2.2 文生图工作流 免费课程对应工作流RunningHub在线运行版_1953741553124691969.json
hash: b57d164a1e2f8b57
coverage: 0.961538
learned_at: 2026-10-15 22:27:34
nodes: [ModelSamplingSD3, WanVideoNAG, FastFilmGrain, CLIPTextEncode, WanVideoNAG, SharkOptions_Beta, ClownOptions_DetailBoost_Beta, VAEDecode, FastFilmGrain, SaveImage, ClownsharKSampler_Beta, VAEDecodeTiled, UNETLoader, SaveImage, VAEDecode, KSampler, EmptySD3LatentImage, ModelSamplingFlux, ConditioningZeroOut, FluxGuidance, Power Lora Loader (rgthree), UNETLoader, Power Lora Loader (rgthree), UnetLoaderGGUF, ClownsharKSampler_Beta, LatentUpscaleBy, SaveImage, ModelPatchTorchSettings, VAELoader, UnetLoaderGGUF, CLIPTextEncode, VAEDecode, VAEDecodeTiled, EmptyHunyuanLatentVideo, VAELoader, VAELoader, SaveImage, DualCLIPLoaderGGUF, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPLoaderGGUF, KSampler, UnetLoaderGGUF, ModelSamplingSD3, Note, Note, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPLoaderGGUF, EmptyHunyuanLatentVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 35179593351718, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Wan 2.2 文生图工作流 免费课程对应工作流RunningHub在线运行版_1953741553124691969.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan 2.2 文生图工作流 免费课程对应工作流RunningHub在线运行版_1953741553124691969.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `ModelSamplingSD3`
- `WanVideoNAG`
- `FastFilmGrain`
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `SharkOptions_Beta`
- `ClownOptions_DetailBoost_Beta`
- `VAEDecode` ★核心
- `FastFilmGrain`
- `SaveImage`
- `ClownsharKSampler_Beta` ★核心
- `VAEDecodeTiled` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `ModelSamplingFlux`
- `ConditioningZeroOut`
- `FluxGuidance`
- `Power Lora Loader (rgthree)`
- `UNETLoader` ★核心
- `Power Lora Loader (rgthree)`
- `UnetLoaderGGUF` ★核心
- `ClownsharKSampler_Beta` ★核心
- `LatentUpscaleBy`
- `SaveImage`
- `ModelPatchTorchSettings`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `VAELoader`
- `SaveImage`
- `DualCLIPLoaderGGUF`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoaderGGUF`
- `KSampler` ★核心
- `UnetLoaderGGUF` ★核心
- `ModelSamplingSD3`
- `Note`
- `Note`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPLoaderGGUF`
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `35179593351718`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **96%**（50/52）

**有卡**：`ModelSamplingSD3`、`WanVideoNAG`、`FastFilmGrain`、`CLIPTextEncode`、`SharkOptions_Beta`、`ClownOptions_DetailBoost_Beta`、`VAEDecode`、`SaveImage`、`ClownsharKSampler_Beta`、`VAEDecodeTiled`、`UNETLoader`、`KSampler`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`ConditioningZeroOut`、`FluxGuidance`、`Power Lora Loader (rgthree)`、`UnetLoaderGGUF`、`LatentUpscaleBy`、`ModelPatchTorchSettings`、`VAELoader`、`EmptyHunyuanLatentVideo`、`DualCLIPLoaderGGUF`、`CLIPLoaderGGUF`、`PathchSageAttentionKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、FluxGuidance、ClownsharKSampler_Beta

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
