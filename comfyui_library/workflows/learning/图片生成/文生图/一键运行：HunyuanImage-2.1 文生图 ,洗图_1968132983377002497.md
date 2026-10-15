---
key: 图片生成/文生图/一键运行：HunyuanImage-2.1 文生图 ,洗图_1968132983377002497.json
name: 一键运行：HunyuanImage-2.1 文生图 ,洗图_1968132983377002497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/一键运行：HunyuanImage-2.1 文生图 ,洗图_1968132983377002497.json
hash: 88a5cb694ce73314
coverage: 0.846154
learned_at: 2026-10-15 22:28:08
nodes: [PreviewImage, KSampler (Efficient), UnetLoaderGGUF, Prompts Everywhere, CLIPTextEncode, CLIPTextEncode, EasyCache, DualCLIPLoader, VAELoader, EmptyHunyuanImageLatent, Note, SaveImage, LayerFilter: HDREffects]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 472575738928418, "steps": 20}
---

# 图片生成/文生图/一键运行：HunyuanImage-2.1 文生图 ,洗图_1968132983377002497.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/一键运行：HunyuanImage-2.1 文生图 ,洗图_1968132983377002497.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（13 个）：
- `PreviewImage`
- `KSampler (Efficient)` ★核心
- `UnetLoaderGGUF` ★核心
- `Prompts Everywhere`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EasyCache`
- `DualCLIPLoader`
- `VAELoader`
- `EmptyHunyuanImageLatent`
- `Note`
- `SaveImage`
- `LayerFilter: HDREffects`

## 关键参数

- `seed` = `472575738928418`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`KSampler (Efficient)`、`UnetLoaderGGUF`、`Prompts Everywhere`、`CLIPTextEncode`、`EasyCache`、`DualCLIPLoader`、`VAELoader`、`EmptyHunyuanImageLatent`、`SaveImage`、`LayerFilter: HDREffects`

**用到的条目**：VAELoader、CLIPTextEncode、KSampler (Efficient)、EmptyHunyuanImageLatent、Prompts Everywhere、SaveImage、DualCLIPLoader、UnetLoaderGGUF
