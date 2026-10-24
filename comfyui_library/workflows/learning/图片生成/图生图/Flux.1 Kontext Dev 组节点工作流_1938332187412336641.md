---
key: 图片生成/图生图/Flux.1 Kontext Dev 组节点工作流_1938332187412336641.json
name: Flux.1 Kontext Dev 组节点工作流_1938332187412336641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1 Kontext Dev 组节点工作流_1938332187412336641.json
hash: 9d0a776ea5b22a96
coverage: 0.769231
learned_at: 2026-10-23 10:58:39
nodes: [VAELoader, FluxKontextImageScale, SaveImage, SaveImage, ImageStitch, VAEEncode, workflow>Edit, PreviewImage, workflow>Edit, MarkdownNote, MarkdownNote, LoadImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.1 Kontext Dev 组节点工作流_1938332187412336641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1 Kontext Dev 组节点工作流_1938332187412336641.json`

## 结构

**生成流程**：Model → Encode → Process → Output → Other

**节点**（13 个）：
- `VAELoader`
- `FluxKontextImageScale`
- `SaveImage`
- `SaveImage`
- `ImageStitch`
- `VAEEncode` ★核心
- `workflow>Edit`
- `PreviewImage`
- `workflow>Edit`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`VAELoader`、`FluxKontextImageScale`、`SaveImage`、`ImageStitch`、`VAEEncode`、`workflow>Edit`、`LoadImage`

**用到的条目**：VAELoader、LoadImage、VAEEncode、FluxKontextImageScale、SaveImage、ImageStitch、ImageStitch、workflow>Edit
