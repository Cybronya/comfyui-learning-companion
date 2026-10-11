---
key: 视频生成/文生视频/Wan2.2双模型首尾帧视频_2064706031250395137.json
name: Wan2.2双模型首尾帧视频_2064706031250395137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2双模型首尾帧视频_2064706031250395137.json
hash: 8007d219d0568d75
coverage: 0.815789
learned_at: 2026-10-11 20:21:31
nodes: [CLIPVisionLoader, CLIPLoader, VAELoader, JWInteger, UNETLoader, CLIPTextEncode, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, wanBlockSwap, wanBlockSwap, ImageResizeKJ, Qwen3_VQA, CLIPVisionEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, ImageConcanate, easy textSwitch, ModelPatchTorchSettings, ModelPatchTorchSettings, easy showAnything, CLIPTextEncode, WanFirstLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, JWInteger, intToFloat _O, UNETLoader, VHS_VideoCombine, Images to RGB, ModelSamplingSD3, ModelSamplingSD3, JWInteger, MathExpression|pysssss, LoadImage, LoadImage, CR Text]
patterns: []
missing: [CR Text, Images to RGB, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, easy textSwitch, intToFloat _O]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Images to RGB` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `intToFloat _O` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2双模型首尾帧视频_2064706031250395137.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2双模型首尾帧视频_2064706031250395137.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `CLIPVisionLoader`
- `CLIPLoader`
- `VAELoader`
- `JWInteger`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `wanBlockSwap`
- `wanBlockSwap`
- `ImageResizeKJ`
- `Qwen3_VQA`
- `CLIPVisionEncode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ImageConcanate`
- `easy textSwitch`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `JWInteger`
- `intToFloat _O`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `Images to RGB`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `JWInteger`
- `MathExpression|pysssss`
- `LoadImage`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（31/38）

**有卡**：`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`JWInteger`、`UNETLoader`、`CLIPTextEncode`、`ImageConcanate`、`CLIPVisionEncode`、`wanBlockSwap`、`ImageResizeKJ`、`Qwen3_VQA`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`WanFirstLastFrameToVideo`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`ModelSamplingSD3`、`LoadImage`

**缺卡**（6）：`CR Text`、`Images to RGB`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`easy textSwitch`、`intToFloat _O`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Images to RGB` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `intToFloat _O` 知识库中没有该节点类型的任何知识
