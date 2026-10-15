---
key: 图片生成/文生图/Qwen2.1-文生图_2106946374871904257.json
name: Qwen2.1-文生图_2106946374871904257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1-文生图_2106946374871904257.json
hash: 7df83dbccb2d5e79
coverage: 1
learned_at: 2026-10-10 20:59:06
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, SamplerCustomAdvanced, SaveImageAdvanced, TextEncodeQwenImage21, QwenImage21FunPDDLoader, BasicGuider, RandomNoise]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Qwen2.1-文生图_2106946374871904257.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1-文生图_2106946374871904257.json`

## 结构

**节点**（11 个）：
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `VAEDecode`
- `SamplerCustomAdvanced`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `QwenImage21FunPDDLoader`
- `BasicGuider`
- `RandomNoise`

## 关键参数

- `batch_size` = `1`
- `height` = `1024`
- `width` = `1024`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`SamplerCustomAdvanced`、`SaveImageAdvanced`、`TextEncodeQwenImage21`、`QwenImage21FunPDDLoader`、`BasicGuider`、`RandomNoise`
