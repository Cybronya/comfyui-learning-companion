---
key: 图片生成/文生图/🈚️基础 文生图-图片反推-Wan2.2-moe-native-Lightx_1953118044471160833.json
name: 🈚️基础 文生图-图片反推-Wan2.2-moe-native-Lightx_1953118044471160833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/🈚️基础 文生图-图片反推-Wan2.2-moe-native-Lightx_1953118044471160833.json
hash: 34febed2a3719f3e
coverage: 0.529412
learned_at: 2026-10-15 22:29:11
nodes: [CLIPTextEncode, VAELoader, SetNode, VAEDecode, CLIPTextEncode, CLIPLoader, SetNode, ApplySageAttention, SetNode, SetNode, wanBlockSwap, GetNode, GetNode, SetNode, SetNode, GetNode, easy seed, JWInteger, GetNode, GetNode, JWInteger, SetNode, LoraLoaderModelOnly, GetNode, LoadImage, GetNode, RebatchLatents, RebatchLatents, LatentPixelScale, ImageSmartSharpen+, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, UpscaleModelLoader, KSampler, WanMoeKSampler, GetNode, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, GetNode, GetNode, GetNode, JWInteger, SetNode, SetNode, GetNode, LayerUtility: JoyCaptionBeta1, CR Prompt Text, Qwen2.5VL, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, SetNode, UNETLoader, ApplySageAttention, GetNode, EmptyHunyuanLatentVideo, GetNode, GetNode, easy showAnything, easy cleanGpuUsed, SetNode, UNETLoader, ImpactSwitch, wanBlockSwap, LoraLoaderModelOnly, SaveImage, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 4, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/🈚️基础 文生图-图片反推-Wan2.2-moe-native-Lightx_1953118044471160833.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/🈚️基础 文生图-图片反推-Wan2.2-moe-native-Lightx_1953118044471160833.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SetNode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `SetNode`
- `ApplySageAttention`
- `SetNode`
- `SetNode`
- `wanBlockSwap`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy seed`
- `JWInteger`
- `GetNode`
- `GetNode`
- `JWInteger`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LoadImage`
- `GetNode`
- `RebatchLatents`
- `RebatchLatents`
- `LatentPixelScale`
- `ImageSmartSharpen+`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `UpscaleModelLoader`
- `KSampler` ★核心
- `WanMoeKSampler` ★核心
- `GetNode`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `GetNode`
- `GetNode`
- `GetNode`
- `JWInteger`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: JoyCaptionBeta1`
- `CR Prompt Text`
- `Qwen2.5VL`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `SetNode`
- `UNETLoader` ★核心
- `ApplySageAttention`
- `GetNode`
- `EmptyHunyuanLatentVideo`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `easy cleanGpuUsed`
- `SetNode`
- `UNETLoader` ★核心
- `ImpactSwitch`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `PreviewImage`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **53%**（36/68）

**有卡**：`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`CLIPLoader`、`ApplySageAttention`、`wanBlockSwap`、`easy seed`、`JWInteger`、`LoraLoaderModelOnly`、`LoadImage`、`RebatchLatents`、`LatentPixelScale`、`ImageSmartSharpen+`、`UpscaleModelLoader`、`KSampler`、`WanMoeKSampler`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: JoyCaptionBeta1`、`CR Prompt Text`、`Qwen2.5VL`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`EmptyHunyuanLatentVideo`、`easy cleanGpuUsed`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
