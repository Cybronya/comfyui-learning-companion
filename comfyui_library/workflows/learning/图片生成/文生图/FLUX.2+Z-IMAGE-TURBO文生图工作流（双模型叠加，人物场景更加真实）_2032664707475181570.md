---
key: 图片生成/文生图/FLUX.2+Z-IMAGE-TURBO文生图工作流（双模型叠加，人物场景更加真实）_2032664707475181570.json
name: FLUX.2+Z-IMAGE-TURBO文生图工作流（双模型叠加，人物场景更加真实）_2032664707475181570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2+Z-IMAGE-TURBO文生图工作流（双模型叠加，人物场景更加真实）_2032664707475181570.json
hash: 844f2d4ad0b2ce74
coverage: 0.903226
learned_at: 2026-10-21 02:51:49
nodes: [SamplerCustomAdvanced, RandomNoise, VAEDecode, VAELoader, UNETLoader, CLIPLoader, CFGGuider, PainterFluxImageEdit, Flux2Scheduler, KSamplerSelect, LoraLoaderModelOnly, LoraLoaderModelOnly, RunningHub Deepcleaner, ModelSamplingAuraFlow, Save Image w/o Metadata, GetNode, SetNode, Image Comparer (rgthree), CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, UNETLoader, RH_Captioner, VAEDecode, KSampler, LayerMask: HumanPartsUltra, InpaintModelConditioning, VAELoader, CR Image Size, CLIPTextEncode, CR Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.6000000000000001, "sampler_name": "euler", "scheduler": "beta57", "seed": 642226499225461, "steps": 10}
---

# 图片生成/文生图/FLUX.2+Z-IMAGE-TURBO文生图工作流（双模型叠加，人物场景更加真实）_2032664707475181570.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2+Z-IMAGE-TURBO文生图工作流（双模型叠加，人物场景更加真实）_2032664707475181570.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CFGGuider`
- `PainterFluxImageEdit`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RunningHub Deepcleaner`
- `ModelSamplingAuraFlow`
- `Save Image w/o Metadata`
- `GetNode`
- `SetNode`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `RH_Captioner`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LayerMask: HumanPartsUltra`
- `InpaintModelConditioning`
- `VAELoader`
- `CR Image Size`
- `CLIPTextEncode` ★核心
- `CR Text`

## 关键参数

- `seed` = `642226499225461`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`SamplerCustomAdvanced`、`RandomNoise`、`VAEDecode`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`CFGGuider`、`PainterFluxImageEdit`、`Flux2Scheduler`、`KSamplerSelect`、`LoraLoaderModelOnly`、`RunningHub Deepcleaner`、`ModelSamplingAuraFlow`、`Save Image w/o Metadata`、`CLIPTextEncode`、`RH_Captioner`、`KSampler`、`LayerMask: HumanPartsUltra`、`InpaintModelConditioning`、`CR Image Size`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、CFGGuider
