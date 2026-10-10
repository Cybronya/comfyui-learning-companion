---
key: 视频生成/文生视频/（Wan2.2_5B模型）视频高清放大video_wan2_2_14Bi2v_5BUpscale_1951274170883756033.json
name: （Wan2.2_5B模型）视频高清放大video_wan2_2_14Bi2v_5BUpscale_1951274170883756033
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（Wan2.2_5B模型）视频高清放大video_wan2_2_14Bi2v_5BUpscale_1951274170883756033.json
hash: ede16c17235db796
coverage: 0.617647
learned_at: 2026-10-10 23:14:28
nodes: [CLIPTextEncode, WanImageToVideo, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, LayerUtility: PurgeVRAM, VAEDecode, VAEDecodeTiled, PreviewImage, GetNode, GetNode, KSamplerAdvanced, GetNode, GetNode, KSamplerAdvanced, VAEDecode, SetNode, GetNode, ImageScaleBy, VAEEncode, VHS_VideoCombine, UNETLoader, UNETLoader, VAELoader, ImageResizeKJv2, PathchSageAttentionKJ, GetNode, GetNode, GetNode, CLIPLoader, VAELoader, UNETLoader, Note, Video_Upscale_With_Model, VHS_VideoCombine, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, Note, GetNode, SetNode, SetNode, INTConstant, LoadImage, INTConstant, INTConstant, CLIPTextEncode, VHS_VideoCombine, INTConstant, MathExpression|pysssss, SetNode, SetNode, SetNode, VHS_VideoCombine, MathExpression|pysssss, INTConstant, Note, CLIPTextEncode, CLIPTextEncode, KSampler, LayerUtility: PurgeVRAM, Note, Note, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, MathExpression|pysssss, MathExpression|pysssss]
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 777, "steps": 12}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/（Wan2.2_5B模型）视频高清放大video_wan2_2_14Bi2v_5BUpscale_1951274170883756033.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（Wan2.2_5B模型）视频高清放大video_wan2_2_14Bi2v_5BUpscale_1951274170883756033.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `PreviewImage`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `ImageScaleBy`
- `VAEEncode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `ImageResizeKJv2`
- `PathchSageAttentionKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `Note`
- `Video_Upscale_With_Model`
- `VHS_VideoCombine`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `Note`
- `GetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `INTConstant`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `INTConstant`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `Note`
- `Note`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `777`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **62%**（42/68）

**有卡**：`CLIPTextEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`VAEDecode`、`VAEDecodeTiled`、`KSamplerAdvanced`、`ImageScaleBy`、`VAEEncode`、`VHS_VideoCombine`、`UNETLoader`、`VAELoader`、`ImageResizeKJv2`、`CLIPLoader`、`Video_Upscale_With_Model`、`LoraLoaderModelOnly`、`INTConstant`、`LoadImage`、`KSampler`

**缺卡**（4）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`MathExpression|pysssss`、`MathExpression|pysssss`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
