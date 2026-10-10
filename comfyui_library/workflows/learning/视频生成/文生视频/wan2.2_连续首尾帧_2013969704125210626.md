---
key: 视频生成/文生视频/wan2.2_连续首尾帧_2013969704125210626.json
name: wan2.2_连续首尾帧_2013969704125210626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2_连续首尾帧_2013969704125210626.json
hash: 2e67d2bd39d79072
coverage: 0.516129
learned_at: 2026-10-11 03:07:13
nodes: [SetNode, SetNode, ImpactInt, PathchSageAttentionKJ, PathchSageAttentionKJ, UNETLoader, CLIPLoader, CLIPVisionLoader, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LoadImage, SetNode, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPVisionEncode, GetNode, GetNode, UNETLoader, ModelSamplingSD3, GetNode, GetNode, KSamplerAdvanced, GetNode, GetNode, GetNode, SetNode, CLIPVisionEncode, GetNode, CLIPVisionEncode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, GetNode, CLIPVisionEncode, GetNode, CLIPVisionEncode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, GetNode, CLIPVisionEncode, GetNode, CLIPVisionEncode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, GetNode, CLIPVisionEncode, GetNode, CLIPVisionEncode, GetNode, GetNode, GetNode, CLIPVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, WanFirstLastFrameToVideo, KSamplerAdvanced, WanFirstLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, WanFirstLastFrameToVideo, KSamplerAdvanced, WanFirstLastFrameToVideo, VAEDecode, Anything Everywhere?, CLIPTextEncode, Anything Everywhere?, Anything Everywhere?, ModelSamplingSD3, ImpactInt, Anything Everywhere?, SetNode, WanFirstLastFrameToVideo, VAEDecode, VAEDecode, VAEDecode, ImageBatchJoin, VAEDecode, ImageBatchJoin, ImageBatchJoin, ImageBatchJoin, CreateVideo, SaveVideo, VHS_VideoCombine, ImpactInt, MuyeMathCalculator, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: [Anything Everywhere?, Anything Everywhere?, Anything Everywhere?, Anything Everywhere?]
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `Anything Everywhere?` 知识库中没有该节点类型的任何知识, 次要节点 `Anything Everywhere?` 知识库中没有该节点类型的任何知识, 次要节点 `Anything Everywhere?` 知识库中没有该节点类型的任何知识, 次要节点 `Anything Everywhere?` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2_连续首尾帧_2013969704125210626.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2_连续首尾帧_2013969704125210626.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（124 个）：
- `SetNode`
- `SetNode`
- `ImpactInt`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPVisionEncode`
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `WanFirstLastFrameToVideo`
- `VAEDecode` ★核心
- `Anything Everywhere?`
- `CLIPTextEncode` ★核心
- `Anything Everywhere?`
- `Anything Everywhere?`
- `ModelSamplingSD3`
- `ImpactInt`
- `Anything Everywhere?`
- `SetNode`
- `WanFirstLastFrameToVideo`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageBatchJoin`
- `VAEDecode` ★核心
- `ImageBatchJoin`
- `ImageBatchJoin`
- `ImageBatchJoin`
- `CreateVideo`
- `SaveVideo`
- `VHS_VideoCombine`
- `ImpactInt`
- `MuyeMathCalculator`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **52%**（64/124）

**有卡**：`ImpactInt`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPLoader`、`CLIPVisionLoader`、`LoadImage`、`CLIPVisionEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAELoader`、`LoraLoaderModelOnly`、`WanFirstLastFrameToVideo`、`VAEDecode`、`CLIPTextEncode`、`ImageBatchJoin`、`CreateVideo`、`SaveVideo`、`VHS_VideoCombine`、`MuyeMathCalculator`

**缺卡**（4）：`Anything Everywhere?`、`Anything Everywhere?`、`Anything Everywhere?`、`Anything Everywhere?`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `Anything Everywhere?` 知识库中没有该节点类型的任何知识
- 次要节点 `Anything Everywhere?` 知识库中没有该节点类型的任何知识
- 次要节点 `Anything Everywhere?` 知识库中没有该节点类型的任何知识
- 次要节点 `Anything Everywhere?` 知识库中没有该节点类型的任何知识
