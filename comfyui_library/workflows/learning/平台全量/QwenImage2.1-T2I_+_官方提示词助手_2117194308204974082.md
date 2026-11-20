---
key: 平台全量/QwenImage2.1-T2I_+_官方提示词助手_2117194308204974082.json
name: QwenImage2.1-T2I_+_官方提示词助手_2117194308204974082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/QwenImage2.1-T2I_+_官方提示词助手_2117194308204974082.json
hash: f3b0c220409ce364
coverage: 0.764706
learned_at: 2026-11-14 00:53:21
nodes: [UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, Any Switch (rgthree), Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, PrimitiveStringMultiline, TextGenerate, TextConcatenator, JsonExtractString, CLIPLoader, ShowAnything|Mie, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 0, "steps": 30, "width": 1560}
---

# 平台全量/QwenImage2.1-T2I_+_官方提示词助手_2117194308204974082.json

> 来源文件 `comfyui_library/workflows/平台全量/QwenImage2.1-T2I_+_官方提示词助手_2117194308204974082.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `Any Switch (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `TextConcatenator`
- `JsonExtractString`
- `CLIPLoader`
- `ShowAnything|Mie`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1560`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`TextGenerate`、`TextConcatenator`、`JsonExtractString`、`ShowAnything|Mie`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage
