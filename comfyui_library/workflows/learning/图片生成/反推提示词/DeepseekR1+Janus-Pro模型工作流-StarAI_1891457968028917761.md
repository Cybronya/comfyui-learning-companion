---
key: 图片生成/反推提示词/DeepseekR1+Janus-Pro模型工作流-StarAI_1891457968028917761.json
name: DeepseekR1+Janus-Pro模型工作流-StarAI_1891457968028917761
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/DeepseekR1+Janus-Pro模型工作流-StarAI_1891457968028917761.json
hash: c36468c501402ac3
coverage: 0.829268
learned_at: 2026-10-26 01:45:01
nodes: [EmptyLatentImage, DifferentialDiffusion, ConditioningZeroOut, DifferentialDiffusion, ConditioningZeroOut, CLIPTextEncode, Note Plus (mtb), easy clearCacheAll, LayerUtility: PurgeVRAM, VAEDecode, easy clearCacheAll, VAEDecode, Fast Groups Bypasser (rgthree), ArgosTranslateTextNode, LayerUtility: PurgeVRAM, KSampler, EmptyLatentImage, LayerUtility: PurgeVRAM, PreviewImage, ShowText|pysssss, CLIPTextEncode, ShowText|pysssss, JanusImageUnderstanding, LoadImage, JanusModelLoader, UNETLoader, VAELoader, DualCLIPLoader, KSampler, ShowText|pysssss, LayerUtility: PurgeVRAM, easy cleanGpuUsed, ShowText|pysssss, SaveImage, UNETLoader, DualCLIPLoader, VAELoader, LmcqDeepGen, easy cleanGpuUsed, Fast Groups Bypasser (rgthree), LmcqDeepLoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "normal", "seed": 444778580130075, "steps": 20, "width": 512}
---

# 图片生成/反推提示词/DeepseekR1+Janus-Pro模型工作流-StarAI_1891457968028917761.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/DeepseekR1+Janus-Pro模型工作流-StarAI_1891457968028917761.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `EmptyLatentImage` ★核心
- `DifferentialDiffusion`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `Note Plus (mtb)`
- `easy clearCacheAll`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ArgosTranslateTextNode`
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `JanusImageUnderstanding`
- `LoadImage`
- `JanusModelLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `KSampler` ★核心
- `ShowText|pysssss`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `SaveImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LmcqDeepGen`
- `easy cleanGpuUsed`
- `Fast Groups Bypasser (rgthree)`
- `LmcqDeepLoader`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `444778580130075`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **83%**（34/41）

**有卡**：`EmptyLatentImage`、`DifferentialDiffusion`、`ConditioningZeroOut`、`CLIPTextEncode`、`Note Plus (mtb)`、`easy clearCacheAll`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`ArgosTranslateTextNode`、`KSampler`、`JanusImageUnderstanding`、`LoadImage`、`JanusModelLoader`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`easy cleanGpuUsed`、`SaveImage`、`LmcqDeepGen`、`LmcqDeepLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage、UNETLoader
