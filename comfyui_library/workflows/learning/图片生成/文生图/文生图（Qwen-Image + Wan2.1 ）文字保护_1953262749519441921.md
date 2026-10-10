---
key: 文生图（Qwen-Image + Wan2.1 ）文字保护_1953262749519441921.json
name: 文生图（Qwen-Image + Wan2.1 ）文字保护_1953262749519441921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图（Qwen-Image + Wan2.1 ）文字保护_1953262749519441921.json
hash: 1cdf932d614f7d53
coverage: 0.769231
learned_at: 2026-10-10 20:59:49
nodes: [CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, ModelSamplingAuraFlow, CLIPTextEncode, EmptySD3LatentImage, SaveImage, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, InpaintModelConditioning, VAEDecode, KSampler, SaveImage, LayerUtility: PurgeVRAM, QwenVLDetection, DownloadAndLoadQwenModel, CR Prompt Text, BBoxesToSAM2, easy showAnything, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, INPAINT_ExpandMask, LayerMask: LoadSAM2Model, LayerUtility: PurgeVRAM, InvertMask, MaskPreview+, JWInteger, JWInteger, KSampler, VAEDecode, CR Prompt Text]
patterns: []
missing: [LayerMask: LoadSAM2Model, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CR Prompt Text, CR Prompt Text, MaskPreview+]
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 322764980478862, "steps": 20}
discoveries: [次要节点 `LayerMask: LoadSAM2Model` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: SAM2UltraV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 文生图（Qwen-Image + Wan2.1 ）文字保护_1953262749519441921.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图（Qwen-Image + Wan2.1 ）文字保护_1953262749519441921.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `InpaintModelConditioning`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `QwenVLDetection`
- `DownloadAndLoadQwenModel`
- `CR Prompt Text`
- `BBoxesToSAM2`
- `easy showAnything`
- `LayerMask: SAM2UltraV2`
- `LayerUtility: PurgeVRAM`
- `INPAINT_ExpandMask`
- `LayerMask: LoadSAM2Model`
- `LayerUtility: PurgeVRAM`
- `InvertMask`
- `MaskPreview+`
- `JWInteger`
- `JWInteger`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CR Prompt Text`

## 关键参数

- `seed` = `322764980478862`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **77%**（30/39）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`SaveImage`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`InpaintModelConditioning`、`VAEDecode`、`KSampler`、`QwenVLDetection`、`DownloadAndLoadQwenModel`、`BBoxesToSAM2`、`INPAINT_ExpandMask`、`InvertMask`、`JWInteger`

**缺卡**（8）：`LayerMask: LoadSAM2Model`、`LayerMask: SAM2UltraV2`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`、`CR Prompt Text`、`MaskPreview+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、InpaintModelConditioning

## 学习发现

- 次要节点 `LayerMask: LoadSAM2Model` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: SAM2UltraV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明
