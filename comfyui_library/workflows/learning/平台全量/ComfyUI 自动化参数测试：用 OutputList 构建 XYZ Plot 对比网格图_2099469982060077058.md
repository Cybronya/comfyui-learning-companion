---
key: 平台全量/ComfyUI 自动化参数测试：用 OutputList 构建 XYZ Plot 对比网格图_2099469982060077058.json
name: ComfyUI 自动化参数测试：用 OutputList 构建 XYZ Plot 对比网格图_2099469982060077058
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/ComfyUI 自动化参数测试：用 OutputList 构建 XYZ Plot 对比网格图_2099469982060077058.json
hash: b1a059c9a4e07adb
coverage: 0.414634
learned_at: 2026-11-14 00:22:21
nodes: [VAELoader, CLIPTextEncode, CLIPTextEncode, StringOutputList, SetNode, GetNode, KSampler, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, PreviewAny, PreviewAny, PreviewAny, SetNode, CombineOutputLists, GetNode, SetNode, SetNode, SetNode, StringOutputList, PreviewAny, GetNode, CLIPLoader, UNETLoader, EmptyLatentImage, GetNode, StringOutputList, StringFormat, ComfyMathExpression, PreviewImage, PreviewImage, XyzGridPlot, XyzGridPlot, GetNode, SetNode, VAEDecode, SaveImage, MarkdownNote]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 377858256889530, "steps": 6, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/ComfyUI 自动化参数测试：用 OutputList 构建 XYZ Plot 对比网格图_2099469982060077058.json

> 来源文件 `comfyui_library/workflows/平台全量/ComfyUI 自动化参数测试：用 OutputList 构建 XYZ Plot 对比网格图_2099469982060077058.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（41 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `StringOutputList`
- `SetNode`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `SetNode`
- `CombineOutputLists`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `StringOutputList`
- `PreviewAny`
- `GetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `GetNode`
- `StringOutputList`
- `StringFormat`
- `ComfyMathExpression`
- `PreviewImage`
- `PreviewImage`
- `XyzGridPlot`
- `XyzGridPlot`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `SaveImage`
- `MarkdownNote`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `377858256889530`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **41%**（17/41）

**有卡**：`VAELoader`、`CLIPTextEncode`、`StringOutputList`、`KSampler`、`CombineOutputLists`、`CLIPLoader`、`UNETLoader`、`EmptyLatentImage`、`StringFormat`、`ComfyMathExpression`、`XyzGridPlot`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、SaveImage、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
