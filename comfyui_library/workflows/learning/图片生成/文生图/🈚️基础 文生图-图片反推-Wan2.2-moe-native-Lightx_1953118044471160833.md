---
key: 图片生成/文生图/🈚️基础 文生图-图片反推-Wan2.2-moe-native-Lightx_1953118044471160833.json
name: 🈚️基础 文生图-图片反推-Wan2.2-moe-native-Lightx_1953118044471160833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/🈚️基础 文生图-图片反推-Wan2.2-moe-native-Lightx_1953118044471160833.json
hash: 34febed2a3719f3e
coverage: 0.397059
learned_at: 2026-10-10 21:00:01
nodes: [CLIPTextEncode, VAELoader, SetNode, VAEDecode, CLIPTextEncode, CLIPLoader, SetNode, ApplySageAttention, SetNode, SetNode, wanBlockSwap, GetNode, GetNode, SetNode, SetNode, GetNode, easy seed, JWInteger, GetNode, GetNode, JWInteger, SetNode, LoraLoaderModelOnly, GetNode, LoadImage, GetNode, RebatchLatents, RebatchLatents, LatentPixelScale, ImageSmartSharpen+, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, UpscaleModelLoader, KSampler, WanMoeKSampler, GetNode, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, GetNode, GetNode, GetNode, JWInteger, SetNode, SetNode, GetNode, LayerUtility: JoyCaptionBeta1, CR Prompt Text, Qwen2.5VL, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, SetNode, UNETLoader, ApplySageAttention, GetNode, EmptyHunyuanLatentVideo, GetNode, GetNode, easy showAnything, easy cleanGpuUsed, SetNode, UNETLoader, ImpactSwitch, wanBlockSwap, LoraLoaderModelOnly, SaveImage, PreviewImage]
patterns: []
missing: [ImageSmartSharpen+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, Qwen2.5VL, easy cleanGpuUsed, CR Prompt Text, easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 4, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
discoveries: [次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识, 次要节点 `Qwen2.5VL` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/🈚️基础 文生图-图片反推-Wan2.2-moe-native-Lightx_1953118044471160833.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/🈚️基础 文生图-图片反推-Wan2.2-moe-native-Lightx_1953118044471160833.json`

## 结构

**节点**（68 个）：
- `CLIPTextEncode`
- `VAELoader`
- `SetNode`
- `VAEDecode`
- `CLIPTextEncode`
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
- `LoraLoaderModelOnly`
- `GetNode`
- `LoadImage`
- `GetNode`
- `RebatchLatents`
- `RebatchLatents`
- `LatentPixelScale`
- `ImageSmartSharpen+`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `GetNode`
- `UpscaleModelLoader`
- `KSampler`
- `WanMoeKSampler`
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
- `UNETLoader`
- `ApplySageAttention`
- `GetNode`
- `EmptyHunyuanLatentVideo`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `easy cleanGpuUsed`
- `SetNode`
- `UNETLoader`
- `ImpactSwitch`
- `wanBlockSwap`
- `LoraLoaderModelOnly`
- `SaveImage`
- `PreviewImage`

## 关键参数

- `cfg` = `4`
- `denoise` = `euler_ancestral`
- `sampler_name` = `1`
- `scheduler` = `1`
- `seed` = `0.875`
- `steps` = `randomize`

## 知识

覆盖率 **40%**（27/68）

**有卡**：`CLIPTextEncode`、`VAELoader`、`SetNode`、`VAEDecode`、`CLIPLoader`、`ApplySageAttention`、`wanBlockSwap`、`GetNode`、`easy seed`、`JWInteger`、`LoraLoaderModelOnly`、`LoadImage`、`RebatchLatents`

**缺卡**（9）：`ImageSmartSharpen+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: LoadJoyCaptionBeta1Model`、`Qwen2.5VL`、`easy cleanGpuUsed`、`CR Prompt Text`、`easy seed`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
- 次要节点 `Qwen2.5VL` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
