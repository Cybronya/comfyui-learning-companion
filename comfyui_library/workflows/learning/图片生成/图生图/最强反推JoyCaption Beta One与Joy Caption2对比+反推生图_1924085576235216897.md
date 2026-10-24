---
key: 图片生成/图生图/最强反推JoyCaption Beta One与Joy Caption2对比+反推生图_1924085576235216897.json
name: 最强反推JoyCaption Beta One与Joy Caption2对比+反推生图_1924085576235216897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最强反推JoyCaption Beta One与Joy Caption2对比+反推生图_1924085576235216897.json
hash: 67351280f5cd8881
coverage: 0.972973
learned_at: 2026-10-23 13:05:52
nodes: [easy cleanGpuUsed, Bjornulf_ShowStringText, Bjornulf_ShowStringText, UNETLoader, ArgosTranslateTextNode, LayerUtility: ImageScaleByAspectRatio V2, BasicScheduler, DualCLIPLoader, KSamplerSelect, CLIPTextEncodeFlux, FluxGuidance, ConditioningZeroOut, VAEDecode, easy cleanGpuUsed, SamplerCustom, VAELoader, VAEDecode, easy cleanGpuUsed, SaveImage, SaveImage, Bjornulf_ShowStringText, Bjornulf_ShowStringText, easy cleanGpuUsed, ArgosTranslateTextNode, LoadImage, Fast Groups Bypasser (rgthree), SamplerCustom, KSamplerSelect, ConditioningZeroOut, BasicScheduler, VAEEncode, easy cleanGpuUsed, CLIPTextEncodeFlux, FluxGuidance, Joy_caption_two, JJC_JoyCaption, Joy_caption_two_load]
patterns: []
missing: []
---

# 图片生成/图生图/最强反推JoyCaption Beta One与Joy Caption2对比+反推生图_1924085576235216897.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/最强反推JoyCaption Beta One与Joy Caption2对比+反推生图_1924085576235216897.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `easy cleanGpuUsed`
- `Bjornulf_ShowStringText`
- `Bjornulf_ShowStringText`
- `UNETLoader` ★核心
- `ArgosTranslateTextNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `BasicScheduler`
- `DualCLIPLoader`
- `KSamplerSelect` ★核心
- `CLIPTextEncodeFlux` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SamplerCustom` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `SaveImage`
- `Bjornulf_ShowStringText`
- `Bjornulf_ShowStringText`
- `easy cleanGpuUsed`
- `ArgosTranslateTextNode`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `BasicScheduler`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncodeFlux` ★核心
- `FluxGuidance`
- `Joy_caption_two`
- `JJC_JoyCaption`
- `Joy_caption_two_load`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`easy cleanGpuUsed`、`Bjornulf_ShowStringText`、`UNETLoader`、`ArgosTranslateTextNode`、`LayerUtility: ImageScaleByAspectRatio V2`、`BasicScheduler`、`DualCLIPLoader`、`KSamplerSelect`、`CLIPTextEncodeFlux`、`FluxGuidance`、`ConditioningZeroOut`、`VAEDecode`、`SamplerCustom`、`VAELoader`、`SaveImage`、`LoadImage`、`VAEEncode`、`Joy_caption_two`、`JJC_JoyCaption`、`Joy_caption_two_load`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、ConditioningZeroOut、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustom
