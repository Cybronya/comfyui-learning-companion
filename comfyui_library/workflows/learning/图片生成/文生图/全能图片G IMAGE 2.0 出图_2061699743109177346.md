---
key: 图片生成/文生图/全能图片G IMAGE 2.0 出图_2061699743109177346.json
name: 全能图片G IMAGE 2.0 出图_2061699743109177346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/全能图片G IMAGE 2.0 出图_2061699743109177346.json
hash: 31088c444a784f9a
coverage: 1
learned_at: 2026-10-19 23:03:44
nodes: [CLIPLoader, CLIPTextEncode, ConditioningCombine, Any To String (mtb), PreviewTextNode, CLIPTextEncode, SaveImage, RH_RhartImageG2TextToImage]
patterns: []
missing: []
---

# 图片生成/文生图/全能图片G IMAGE 2.0 出图_2061699743109177346.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/全能图片G IMAGE 2.0 出图_2061699743109177346.json`

## 结构

**生成流程**：Model → Condition → Output → Other

**节点**（8 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningCombine`
- `Any To String (mtb)`
- `PreviewTextNode`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `RH_RhartImageG2TextToImage`

## 知识

覆盖率 **100%**（8/8）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`ConditioningCombine`、`Any To String (mtb)`、`PreviewTextNode`、`SaveImage`、`RH_RhartImageG2TextToImage`

**用到的条目**：CLIPTextEncode、CLIPLoader、ConditioningCombine、SaveImage、PreviewTextNode、RH_RhartImageG2TextToImage、Any To String (mtb)、sd15-t2i-basic
