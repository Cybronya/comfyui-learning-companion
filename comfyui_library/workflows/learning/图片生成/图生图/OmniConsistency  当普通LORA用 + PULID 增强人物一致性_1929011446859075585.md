---
key: 图片生成/图生图/OmniConsistency  当普通LORA用 + PULID 增强人物一致性_1929011446859075585.json
name: OmniConsistency  当普通LORA用 + PULID 增强人物一致性_1929011446859075585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/OmniConsistency  当普通LORA用 + PULID 增强人物一致性_1929011446859075585.json
hash: 76c7852fce0e04c4
coverage: 0.891892
learned_at: 2026-10-23 11:10:11
nodes: [KSamplerSelect, SamplerCustomAdvanced, BasicGuider, VAEDecode, VAELoader, ImageConcanate, ConditioningZeroOut, StyleModelLoader, CLIPVisionLoader, LoraLoaderModelOnly, PulidFluxInsightFaceLoader, PulidFluxEvaClipLoader, UNETLoader, PixelPerfectResolution, easy imageSize, InstructPixToPixConditioning, AIO_Preprocessor, SaveImage, SaveImage, ReduxAdvanced, RandomNoise, LoraLoaderModelOnly, BasicScheduler, FluxGuidance, ApplyPulidFlux, PulidFluxModelLoader, CR Text Replace, easy showAnything, easy showAnything, CR String To Combo, ACE_TextSelector, LoadImage, JWImageResizeByLongerSide, PrimitiveInt, CLIPTextEncode, DualCLIPLoader, MarkdownNote]
patterns: []
missing: []
---

# 图片生成/图生图/OmniConsistency  当普通LORA用 + PULID 增强人物一致性_1929011446859075585.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/OmniConsistency  当普通LORA用 + PULID 增强人物一致性_1929011446859075585.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `VAEDecode` ★核心
- `VAELoader`
- `ImageConcanate`
- `ConditioningZeroOut`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `PulidFluxInsightFaceLoader`
- `PulidFluxEvaClipLoader`
- `UNETLoader` ★核心
- `PixelPerfectResolution`
- `easy imageSize`
- `InstructPixToPixConditioning`
- `AIO_Preprocessor`
- `SaveImage`
- `SaveImage`
- `ReduxAdvanced`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `FluxGuidance`
- `ApplyPulidFlux`
- `PulidFluxModelLoader`
- `CR Text Replace`
- `easy showAnything`
- `easy showAnything`
- `CR String To Combo`
- `ACE_TextSelector`
- `LoadImage`
- `JWImageResizeByLongerSide`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `MarkdownNote`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`VAEDecode`、`VAELoader`、`ImageConcanate`、`ConditioningZeroOut`、`StyleModelLoader`、`CLIPVisionLoader`、`LoraLoaderModelOnly`、`PulidFluxInsightFaceLoader`、`PulidFluxEvaClipLoader`、`UNETLoader`、`PixelPerfectResolution`、`easy imageSize`、`InstructPixToPixConditioning`、`AIO_Preprocessor`、`SaveImage`、`ReduxAdvanced`、`RandomNoise`、`BasicScheduler`、`FluxGuidance`、`ApplyPulidFlux`、`PulidFluxModelLoader`、`CR Text Replace`、`CR String To Combo`、`ACE_TextSelector`、`LoadImage`、`JWImageResizeByLongerSide`、`CLIPTextEncode`、`DualCLIPLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
