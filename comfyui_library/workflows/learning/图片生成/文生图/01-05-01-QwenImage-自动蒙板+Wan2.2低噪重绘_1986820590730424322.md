---
key: 图片生成/文生图/01-05-01-QwenImage-自动蒙板+Wan2.2低噪重绘_1986820590730424322.json
name: 01-05-01-QwenImage-自动蒙板+Wan2.2低噪重绘_1986820590730424322.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/01-05-01-QwenImage-自动蒙板+Wan2.2低噪重绘_1986820590730424322.json
hash: 89c19ade6be332e0
coverage: 0.612903
learned_at: 2026-10-09 20:13:12
nodes: [INTConstant, SetNode, INTConstant, SetNode, SetNode, PreviewImage, MaskToImage, SetNode, VAELoader, GetNode, MaskPreview+, LayerUtility: PurgeVRAM, VAEDecode, BBoxesToSAM2, GetNode, Sam2Segmentation, CLIPTextEncode, CLIPTextEncode, Note, VAELoader, CLIPLoader, GetNode, GetNode, EmptySD3LatentImage, CLIPTextEncode, CLIPLoader, ShowText|pysssss, easy cleanGpuUsed, easy cleanGpuUsed, ModelSamplingSD3, InvertMask, GetNode, PathchSageAttentionKJ, easy showAnything, KSampler, Florence2Run, KSampler, DownloadAndLoadSAM2Model, Florence2toCoordinates, VAEDecode, LoraLoaderModelOnly, InpaintModelConditioning, UnetLoaderGGUF, SaveImage, GetNode, SetNode, NunchakuQwenImageDiTLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, CachePreviewBridge, CLIPTextEncode, CR Prompt Text, Note, DownloadAndLoadFlorence2Model, CR Prompt Text, Note, UnetLoaderGGUF, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, INPAINT_ExpandMask]
patterns: []
missing: [LayerUtility: PurgeVRAM, easy cleanGpuUsed, easy cleanGpuUsed, CR Prompt Text, CR Prompt Text, MaskPreview+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 436504485801435, "steps": 8}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/01-05-01-QwenImage-自动蒙板+Wan2.2低噪重绘_1986820590730424322.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1986820590730424322.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `MaskToImage`
- `SetNode`
- `VAELoader`
- `GetNode`
- `MaskPreview+`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `BBoxesToSAM2`
- `GetNode`
- `Sam2Segmentation`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `VAELoader`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `InvertMask`
- `GetNode`
- `PathchSageAttentionKJ`
- `easy showAnything`
- `KSampler` ★核心
- `Florence2Run`
- `KSampler` ★核心
- `DownloadAndLoadSAM2Model`
- `Florence2toCoordinates`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `InpaintModelConditioning`
- `UnetLoaderGGUF` ★核心
- `SaveImage`
- `GetNode`
- `SetNode`
- `NunchakuQwenImageDiTLoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CachePreviewBridge`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `Note`
- `DownloadAndLoadFlorence2Model`
- `CR Prompt Text`
- `Note`
- `UnetLoaderGGUF` ★核心
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INPAINT_ExpandMask`

## 关键参数

- `seed` = `436504485801435`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **61%**（38/62）

**有卡**：`INTConstant`、`MaskToImage`、`VAELoader`、`VAEDecode`、`BBoxesToSAM2`、`Sam2Segmentation`、`CLIPTextEncode`、`CLIPLoader`、`EmptySD3LatentImage`、`ModelSamplingSD3`、`InvertMask`、`PathchSageAttentionKJ`、`KSampler`、`Florence2Run`、`DownloadAndLoadSAM2Model`、`Florence2toCoordinates`、`LoraLoaderModelOnly`、`InpaintModelConditioning`、`UnetLoaderGGUF`、`SaveImage`、`NunchakuQwenImageDiTLoader`、`ModelSamplingAuraFlow`、`CachePreviewBridge`、`DownloadAndLoadFlorence2Model`、`INPAINT_ExpandMask`

**缺卡**（6）：`LayerUtility: PurgeVRAM`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`CR Prompt Text`、`CR Prompt Text`、`MaskPreview+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、InpaintModelConditioning、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
