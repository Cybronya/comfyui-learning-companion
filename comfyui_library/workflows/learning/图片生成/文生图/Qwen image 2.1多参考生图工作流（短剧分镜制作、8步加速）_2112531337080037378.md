---
key: 图片生成/文生图/Qwen image 2.1多参考生图工作流（短剧分镜制作、8步加速）_2112531337080037378.json
name: Qwen image 2.1多参考生图工作流（短剧分镜制作、8步加速）_2112531337080037378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1多参考生图工作流（短剧分镜制作、8步加速）_2112531337080037378.json
hash: cb61f0b896f2e9b0
coverage: 0.909091
learned_at: 2026-10-21 02:54:19
nodes: [Note, Note, RandomNoise, QwenImage21Cache, CLIPLoader, EmptyLatentImage, CFGGuider, KSamplerSelect, BasicScheduler, ExtendIntermediateSigmas, UNETLoader, VAEDecode, SamplerCustomAdvanced, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, LoadImage, LoraLoaderModelOnly, LoadImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1920, "width": 1440}
---

# 图片生成/文生图/Qwen image 2.1多参考生图工作流（短剧分镜制作、8步加速）_2112531337080037378.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1多参考生图工作流（短剧分镜制作、8步加速）_2112531337080037378.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（22 个）：
- `Note`
- `Note`
- `RandomNoise`
- `QwenImage21Cache`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ExtendIntermediateSigmas`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`

## 关键参数

- `width` = `1440`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`RandomNoise`、`QwenImage21Cache`、`CLIPLoader`、`EmptyLatentImage`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`ExtendIntermediateSigmas`、`UNETLoader`、`VAEDecode`、`SamplerCustomAdvanced`、`SaveImage`、`LoraLoaderModelOnly`、`VAELoader`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
