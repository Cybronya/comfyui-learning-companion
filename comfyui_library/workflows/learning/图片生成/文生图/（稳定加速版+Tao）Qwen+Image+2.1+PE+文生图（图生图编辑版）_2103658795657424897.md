---
key: 图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（图生图编辑版）_2103658795657424897.json
name: （稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（图生图编辑版）_2103658795657424897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（图生图编辑版）_2103658795657424897.json
hash: 586ef0c605e76bdb
coverage: 0.576923
learned_at: 2026-10-10 21:00:00
nodes: [VAEDecode, TextEncodeQwenImage21, easy cleanGpuUsed, SaveImage, QwenPERewriteT8, QwenImage21Cache, KSampler, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, VAELoader, easy showAnything, UNETLoader, CLIPLoader, Note, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, Note, CR Prompt Text, ComfySwitchNode, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, LoadImage]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 691316769154056, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（图生图编辑版）_2103658795657424897.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（图生图编辑版）_2103658795657424897.json`

## 结构

**节点**（26 个）：
- `VAEDecode`
- `TextEncodeQwenImage21`
- `easy cleanGpuUsed`
- `SaveImage`
- `QwenPERewriteT8`
- `QwenImage21Cache`
- `KSampler`
- `ResolutionSelector`
- `EmptyLatentImage`
- `ComfySwitchNode`
- `VAELoader`
- `easy showAnything`
- `UNETLoader`
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
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `691316769154056`
- `steps` = `40`
- `width` = `1024`

## 知识

覆盖率 **58%**（15/26）

**有卡**：`VAEDecode`、`TextEncodeQwenImage21`、`easy cleanGpuUsed`、`SaveImage`、`QwenPERewriteT8`、`QwenImage21Cache`、`KSampler`、`ResolutionSelector`、`EmptyLatentImage`、`ComfySwitchNode`、`VAELoader`、`easy showAnything`、`UNETLoader`、`CLIPLoader`、`Note`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
