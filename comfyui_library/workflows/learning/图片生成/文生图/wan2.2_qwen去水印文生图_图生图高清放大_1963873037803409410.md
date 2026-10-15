---
key: 图片生成/文生图/wan2.2_qwen去水印文生图_图生图高清放大_1963873037803409410.json
name: wan2.2_qwen去水印文生图_图生图高清放大_1963873037803409410
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2_qwen去水印文生图_图生图高清放大_1963873037803409410.json
hash: 269d206e80a49298
coverage: 0.609091
learned_at: 2026-10-10 20:59:27
nodes: [VAELoader, LoadImageOutput, MarkdownNote, CLIPTextEncode, FluxKontextImageScale, PreviewImage, ReferenceLatent, VAEEncode, ConditioningZeroOut, FluxGuidance, EmptySD3LatentImage, KSampler, ModelSamplingSD3, easy clearCacheAll, PurgeVRAM_UTK, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, easy clearCacheAll, PurgeVRAM_UTK, LoraLoaderModelOnly, PathchSageAttentionKJ, SetNode, SetNode, SetNode, SetNode, VAELoader, CLIPLoader, GetNode, LoraLoaderModelOnly, UNETLoader, UNETLoader, PurgeVRAM_UTK, SeedVR2ExtraArgs, VAEDecode, easy clearCacheAll, GetNode, PreviewImage, ImageStitch, PreviewImage, VAEDecode, easy clearCacheAll, PurgeVRAM_UTK, ImageStitch, SaveImage, GetNode, CLIPTextEncode, SeedVR2GGUF, SimpleCondition+, GetNode, EmptyHunyuanLatentVideo, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, Reroute, LoadImage, SetNode, RH_Captioner, CLIPTextEncode, LoraLoaderModelOnly, GetNode, GetNode, PurgeVRAM_UTK, DualCLIPLoader, NunchakuFluxDiTLoader, VAEDecode, PurgeVRAM_UTK, SeedVR2GGUF, SeedVR2ExtraArgs, KSamplerAdvanced, KSamplerAdvanced, PreviewImage, VAEEncode, GetNode, CLIPTextEncode, MarkdownNote, Note, CLIPLoader, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, UNETLoader, Note, GetNode, EmptySD3LatentImage, GetNode, GetNode, ModelSamplingAuraFlow, ModelSamplingAuraFlow, KSampler, easy clearCacheAll, VAEDecode, easy clearCacheAll, SeedVR2ExtraArgs, PurgeVRAM_UTK, SeedVR2GGUF, PreviewImage, INTConstant, INTConstant, SetNode, SetNode, KSampler, Fast Groups Muter (rgthree), JWStringMultiline, SetNode, PreviewImage, PreviewImage, PreviewImage]
patterns: [image_to_image]
missing: [SimpleCondition+, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.45000000000000007, "sampler_name": "euler", "scheduler": "kl_optimal", "seed": 305861248366345, "steps": 10}
discoveries: [次要节点 `SimpleCondition+` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.2_qwen去水印文生图_图生图高清放大_1963873037803409410.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2_qwen去水印文生图_图生图高清放大_1963873037803409410.json`

## 结构

**节点**（110 个）：
- `VAELoader`
- `LoadImageOutput`
- `MarkdownNote`
- `CLIPTextEncode`
- `FluxKontextImageScale`
- `PreviewImage`
- `ReferenceLatent`
- `VAEEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingSD3`
- `easy clearCacheAll`
- `PurgeVRAM_UTK`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `easy clearCacheAll`
- `PurgeVRAM_UTK`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `CLIPLoader`
- `GetNode`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `UNETLoader`
- `PurgeVRAM_UTK`
- `SeedVR2ExtraArgs`
- `VAEDecode`
- `easy clearCacheAll`
- `GetNode`
- `PreviewImage`
- `ImageStitch`
- `PreviewImage`
- `VAEDecode`
- `easy clearCacheAll`
- `PurgeVRAM_UTK`
- `ImageStitch`
- `SaveImage`
- `GetNode`
- `CLIPTextEncode`
- `SeedVR2GGUF`
- `SimpleCondition+`
- `GetNode`
- `EmptyHunyuanLatentVideo`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `LoadImage`
- `SetNode`
- `RH_Captioner`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `GetNode`
- `GetNode`
- `PurgeVRAM_UTK`
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `VAEDecode`
- `PurgeVRAM_UTK`
- `SeedVR2GGUF`
- `SeedVR2ExtraArgs`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `PreviewImage`
- `VAEEncode`
- `GetNode`
- `CLIPTextEncode`
- `MarkdownNote`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `UNETLoader`
- `Note`
- `GetNode`
- `EmptySD3LatentImage`
- `GetNode`
- `GetNode`
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `KSampler`
- `easy clearCacheAll`
- `VAEDecode`
- `easy clearCacheAll`
- `SeedVR2ExtraArgs`
- `PurgeVRAM_UTK`
- `SeedVR2GGUF`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `KSampler`
- `Fast Groups Muter (rgthree)`
- `JWStringMultiline`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `1`
- `denoise` = `0.45000000000000007`
- `sampler_name` = `euler`
- `scheduler` = `kl_optimal`
- `seed` = `305861248366345`
- `steps` = `10`

## 知识

覆盖率 **61%**（67/110）

**有卡**：`VAELoader`、`LoadImageOutput`、`MarkdownNote`、`CLIPTextEncode`、`FluxKontextImageScale`、`PreviewImage`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`FluxGuidance`、`EmptySD3LatentImage`、`KSampler`、`ModelSamplingSD3`、`easy clearCacheAll`、`PurgeVRAM_UTK`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`SetNode`、`CLIPLoader`、`GetNode`、`UNETLoader`、`SeedVR2ExtraArgs`、`VAEDecode`、`ImageStitch`、`SaveImage`、`SeedVR2GGUF`、`SimpleCondition+`、`EmptyHunyuanLatentVideo`、`ImageResizeKJv2`、`Reroute`、`LoadImage`、`RH_Captioner`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`

**缺卡**（7）：`SimpleCondition+`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `SimpleCondition+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
