---
key: 图片生成/文生图/【遇见AI】SD3.5  完整版、GGUF版本基础工作流_2042551889518137346.json
name: 【遇见AI】SD3.5  完整版、GGUF版本基础工作流_2042551889518137346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【遇见AI】SD3.5  完整版、GGUF版本基础工作流_2042551889518137346.json
hash: e8bb8faa82d3e062
coverage: 0.805825
learned_at: 2026-10-21 02:58:07
nodes: [ConditioningZeroOut, EmptySD3LatentImage, VAEDecode, LayerUtility: PurgeVRAM, VAEDecode, ConditioningZeroOut, EmptySD3LatentImage, LayerUtility: PurgeVRAM, Bookmark (rgthree), VAEDecode, EmptySD3LatentImage, LayerUtility: PurgeVRAM, Bookmark (rgthree), SaveImage, SaveImage, VAEDecode, ConditioningZeroOut, EmptySD3LatentImage, Bookmark (rgthree), Bookmark (rgthree), SaveImage, CLIPTextEncode, VAEDecode, ConditioningZeroOut, EmptySD3LatentImage, LayerUtility: PurgeVRAM, Bookmark (rgthree), ModelSamplingSD3, ModelSamplingSD3, KSampler, ModelSamplingSD3, KSampler, ModelSamplingSD3, LayerUtility: PurgeVRAM, KSampler, KSampler, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, SaveImage, VAEDecode, ModelSamplingSD3, ConditioningZeroOut, EmptySD3LatentImage, KSampler, SaveImage, LayerUtility: PurgeVRAM, Bookmark (rgthree), Fast Groups Muter (rgthree), ConditioningZeroOut, ModelSamplingSD3, Fast Groups Muter (rgthree), CLIPTextEncode, Note, Fast Groups Muter (rgthree), ImpactSwitch, Note, SaveImage, LoadImage, LoadImage, TripleCLIPLoader, Note, DualCLIPLoader, TripleCLIPLoader, CLIPLoader, ImpactSwitch, Note, DualCLIPLoader, TripleCLIPLoader, CLIPLoader, ImpactSwitch, Note, DualCLIPLoader, TripleCLIPLoader, CLIPLoader, ImpactSwitch, DualCLIPLoader, TripleCLIPLoader, CLIPLoader, Note, ImpactSwitch, Note, DualCLIPLoader, TripleCLIPLoader, CLIPLoader, ImpactSwitch, VAELoader, VAELoader, CLIPLoader, DualCLIPLoader, CheckpointLoaderSimple, CheckpointLoaderSimple, CheckpointLoaderSimple, UnetLoaderGGUF, UnetLoaderGGUF, UnetLoaderGGUF, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), VAELoader, Fast Groups Muter (rgthree), Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 4, "checkpoint": "sd3.5_medium.safetensors", "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 275739503889539, "steps": 40}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/【遇见AI】SD3.5  完整版、GGUF版本基础工作流_2042551889518137346.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【遇见AI】SD3.5  完整版、GGUF版本基础工作流_2042551889518137346.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（103 个）：
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `LayerUtility: PurgeVRAM`
- `Bookmark (rgthree)`
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `LayerUtility: PurgeVRAM`
- `Bookmark (rgthree)`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Bookmark (rgthree)`
- `Bookmark (rgthree)`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `LayerUtility: PurgeVRAM`
- `Bookmark (rgthree)`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `Bookmark (rgthree)`
- `Fast Groups Muter (rgthree)`
- `ConditioningZeroOut`
- `ModelSamplingSD3`
- `Fast Groups Muter (rgthree)`
- `CLIPTextEncode` ★核心
- `Note`
- `Fast Groups Muter (rgthree)`
- `ImpactSwitch`
- `Note`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `TripleCLIPLoader`
- `Note`
- `DualCLIPLoader`
- `TripleCLIPLoader`
- `CLIPLoader`
- `ImpactSwitch`
- `Note`
- `DualCLIPLoader`
- `TripleCLIPLoader`
- `CLIPLoader`
- `ImpactSwitch`
- `Note`
- `DualCLIPLoader`
- `TripleCLIPLoader`
- `CLIPLoader`
- `ImpactSwitch`
- `DualCLIPLoader`
- `TripleCLIPLoader`
- `CLIPLoader`
- `Note`
- `ImpactSwitch`
- `Note`
- `DualCLIPLoader`
- `TripleCLIPLoader`
- `CLIPLoader`
- `ImpactSwitch`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `DualCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `VAELoader`
- `Fast Groups Muter (rgthree)`
- `Note`

## 关键参数

- `seed` = `275739503889539`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `sd3.5_medium.safetensors`

## 知识

覆盖率 **81%**（83/103）

**有卡**：`ConditioningZeroOut`、`EmptySD3LatentImage`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`Bookmark (rgthree)`、`SaveImage`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSampler`、`LoadImage`、`TripleCLIPLoader`、`DualCLIPLoader`、`CLIPLoader`、`VAELoader`、`CheckpointLoaderSimple`、`UnetLoaderGGUF`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
