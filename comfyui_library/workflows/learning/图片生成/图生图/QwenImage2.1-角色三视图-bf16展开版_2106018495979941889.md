---
key: 图片生成/图生图/QwenImage2.1-角色三视图-bf16展开版_2106018495979941889.json
name: QwenImage2.1-角色三视图-bf16展开版_2106018495979941889.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenImage2.1-角色三视图-bf16展开版_2106018495979941889.json
hash: 485fdb1855507a14
coverage: 0.785714
learned_at: 2026-10-09 22:09:17
nodes: [UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, TextEncodeQwenImage21, EmptyLatentImage, KSampler, VAEDecode, SaveImage, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1152, "sampler_name": "euler", "scheduler": "simple", "seed": 239579204690786, "steps": 25, "width": 2048}
---

# 图片生成/图生图/QwenImage2.1-角色三视图-bf16展开版_2106018495979941889.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2106018495979941889.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `PrimitiveBoolean`

## 关键参数

- `width` = `2048`
- `height` = `1152`
- `batch_size` = `1`
- `seed` = `239579204690786`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
