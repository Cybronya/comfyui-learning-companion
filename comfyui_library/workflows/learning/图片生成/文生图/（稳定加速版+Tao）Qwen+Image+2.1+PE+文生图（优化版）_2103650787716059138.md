---
key: 图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（优化版）_2103650787716059138.json
name: （稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（优化版）_2103650787716059138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（优化版）_2103650787716059138.json
hash: 6373bcbb167f6268
coverage: 0.583333
learned_at: 2026-10-07 02:03:21
nodes: [VAEDecode, TextEncodeQwenImage21, easy cleanGpuUsed, SaveImage, QwenPERewriteT8, QwenImage21Cache, KSampler, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, VAELoader, easy showAnything, UNETLoader, CLIPLoader, Note, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, Note, CR Prompt Text, ComfySwitchNode, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 272015956792580, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（优化版）_2103650787716059138.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（优化版）_2103650787716059138.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `easy cleanGpuUsed`
- `SaveImage`
- `QwenPERewriteT8`
- `QwenImage21Cache`
- `KSampler` ★核心
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAELoader`
- `easy showAnything`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Note`
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `Note`
- `CR Prompt Text`
- `ComfySwitchNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `seed` = `272015956792580`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **58%**（14/24）

**有卡**：`VAEDecode`、`TextEncodeQwenImage21`、`SaveImage`、`QwenPERewriteT8`、`QwenImage21Cache`、`KSampler`、`ResolutionSelector`、`EmptyLatentImage`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
