---
key: 图片生成/文生图/MOSS_StepLab_50_8_4_50·8·4步三档生图.json_2115298864763858946.json
name: MOSS_StepLab_50_8_4_50·8·4步三档生图.json_2115298864763858946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/MOSS_StepLab_50_8_4_50·8·4步三档生图.json_2115298864763858946.json
hash: 5480cbc1a0a0357d
coverage: 0.954545
learned_at: 2026-10-30 17:54:46
nodes: [Note, CLIPTextEncode, CLIPTextEncode, EmptyFlux2LatentImage, UNETLoader, SkipLayerGuidanceDiTSimple, KSampler, VAEDecode, UNETLoader, KSampler, VAEDecode, UNETLoader, LoraLoaderModelOnly, KSampler, VAEDecode, LoraLoaderModelOnly, CLIPLoader, VAELoader, SaveImage, SaveImage, SaveImage, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 4242, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/MOSS_StepLab_50_8_4_50·8·4步三档生图.json_2115298864763858946.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/MOSS_StepLab_50_8_4_50·8·4步三档生图.json_2115298864763858946.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyFlux2LatentImage`
- `UNETLoader` ★核心
- `SkipLayerGuidanceDiTSimple`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `4242`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`CLIPTextEncode`、`EmptyFlux2LatentImage`、`UNETLoader`、`SkipLayerGuidanceDiTSimple`、`KSampler`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、SkipLayerGuidanceDiTSimple

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
