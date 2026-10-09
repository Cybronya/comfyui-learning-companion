---
key: 图片生成/文生图/wan2.2-文生视频-极速超长视频-精准控制动作_1953042137630896130.json
name: wan2.2-文生视频-极速超长视频-精准控制动作_1953042137630896130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2-文生视频-极速超长视频-精准控制动作_1953042137630896130.json
hash: e00072da0faa45af
coverage: 0.54902
learned_at: 2026-10-07 23:11:31
nodes: [VAELoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, UNETLoader, UNETLoader, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, easy showAnything, Int, Int, easy batchAnything, MathExpression|pysssss, GetImageSizeAndCount, LayerUtility: PurgeVRAM V2, VAEDecode, PathchSageAttentionKJ, ModelSamplingSD3, Fast Groups Muter (rgthree), easy showAnything, Text Load Line From File, VHS_VideoCombine, LoraLoaderModelOnly, ImageFromBatch, easy forLoopStart, PathchSageAttentionKJ, ModelSamplingSD3, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, CR Model Input Switch, CR Text, CR Model Input Switch, ConditionalTextOutput, easy convertAnything, CR Text, easy showAnything, CR Model Input Switch, CR Text, PreviewImage, easy forLoopEnd, KSamplerAdvanced, WanImageToVideo, Text Multiline, VHS_VideoCombine, Int, KSamplerAdvanced]
patterns: []
missing: [CR Model Input Switch, CR Model Input Switch, CR Model Input Switch, CR Text, CR Text, CR Text, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, Text Load Line From File, Text Multiline, easy batchAnything, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy convertAnything, easy forLoopEnd, easy forLoopStart]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 2.5, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `CR Model Input Switch` 知识库中没有该节点类型的任何知识, 次要节点 `CR Model Input Switch` 知识库中没有该节点类型的任何知识, 次要节点 `CR Model Input Switch` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/wan2.2-文生视频-极速超长视频-精准控制动作_1953042137630896130.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1953042137630896130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `Int`
- `Int`
- `easy batchAnything`
- `MathExpression|pysssss`
- `GetImageSizeAndCount`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Fast Groups Muter (rgthree)`
- `easy showAnything`
- `Text Load Line From File`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `ImageFromBatch`
- `easy forLoopStart`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CR Model Input Switch`
- `CR Text`
- `CR Model Input Switch`
- `ConditionalTextOutput`
- `easy convertAnything`
- `CR Text`
- `easy showAnything`
- `CR Model Input Switch`
- `CR Text`
- `PreviewImage`
- `easy forLoopEnd`
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `Text Multiline`
- `VHS_VideoCombine`
- `Int`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `2.5`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **55%**（28/51）

**有卡**：`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`Int`、`GetImageSizeAndCount`、`VAEDecode`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VHS_VideoCombine`、`ImageFromBatch`、`ConditionalTextOutput`、`KSamplerAdvanced`、`WanImageToVideo`

**缺卡**（18）：`CR Model Input Switch`、`CR Model Input Switch`、`CR Model Input Switch`、`CR Text`、`CR Text`、`CR Text`、`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`、`Text Load Line From File`、`Text Multiline`、`easy batchAnything`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy convertAnything`、`easy forLoopEnd`、`easy forLoopStart`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、GetImageSizeAndCount

## 学习发现

- 次要节点 `CR Model Input Switch` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Model Input Switch` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Model Input Switch` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
