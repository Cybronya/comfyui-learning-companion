---
key: 视频生成/文生视频/LTX2.3 Product Commercial LoRA 商业广告视频生成_2074728813149380610.json
name: LTX2.3 Product Commercial LoRA 商业广告视频生成_2074728813149380610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 Product Commercial LoRA 商业广告视频生成_2074728813149380610.json
hash: a187991cc20365b8
coverage: 0.393443
learned_at: 2026-10-10 23:00:20
nodes: [VAEDecode, SetNode, GetNode, CR Float To Integer, GetNode, GetNode, GetNode, PrimitiveInt, GetNode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, SetNode, easy cleanGpuUsed, easy clearCacheAll, SetNode, SetNode, SetNode, SetNode, PrimitiveInt, LTXVEmptyLatentAudio, PrimitiveFloat, LTXVConditioning, KSamplerSelect, GetNode, VisualizeSigmasKJ, GetNode, SetNode, ResizeImageMaskNode, GetNode, PreviewImage, VHS_VideoCombine, GetNode, BasicScheduler, PreviewImage, EmptyLTXVLatentVideo, GetImageSize, LTXVPreprocess, PathchSageAttentionKJ, SetNode, VAELoader, SetNode, VAELoader, SetNode, SetNode, UNETLoader, Note, SetNode, MathExpression|pysssss, SetNode, LTXVConcatAVLatent, GetNode, LTXVImgToVideoInplaceKJ, DualCLIPLoader, GetNode, GetNode, ConditioningZeroOut, SamplerCustom, Load Lora, PromptRelayEncode, LoadImage]
patterns: []
missing: [CR Float To Integer, MathExpression|pysssss, easy cleanGpuUsed, easy clearCacheAll, Load Lora]
parameters: {"batch_size": 1, "height": 25, "width": 505}
discoveries: [次要节点 `CR Float To Integer` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `Load Lora` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX2.3 Product Commercial LoRA 商业广告视频生成_2074728813149380610.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 Product Commercial LoRA 商业广告视频生成_2074728813149380610.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `CR Float To Integer`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveFloat`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `GetNode`
- `VisualizeSigmasKJ`
- `GetNode`
- `SetNode`
- `ResizeImageMaskNode`
- `GetNode`
- `PreviewImage`
- `VHS_VideoCombine`
- `GetNode`
- `BasicScheduler`
- `PreviewImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `LTXVPreprocess`
- `PathchSageAttentionKJ`
- `SetNode`
- `VAELoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `Note`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `DualCLIPLoader`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `SamplerCustom` ★核心
- `Load Lora`
- `PromptRelayEncode`
- `LoadImage`

## 关键参数

- `width` = `505`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **39%**（24/61）

**有卡**：`VAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`KSamplerSelect`、`VisualizeSigmasKJ`、`ResizeImageMaskNode`、`VHS_VideoCombine`、`BasicScheduler`、`EmptyLTXVLatentVideo`、`GetImageSize`、`LTXVPreprocess`、`PathchSageAttentionKJ`、`VAELoader`、`UNETLoader`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplaceKJ`、`DualCLIPLoader`、`ConditioningZeroOut`、`SamplerCustom`、`PromptRelayEncode`、`LoadImage`

**缺卡**（5）：`CR Float To Integer`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`easy clearCacheAll`、`Load Lora`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent

## 学习发现

- 次要节点 `CR Float To Integer` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `Load Lora` 仅有 LoRA 的通用知识，没有该节点自己的说明
