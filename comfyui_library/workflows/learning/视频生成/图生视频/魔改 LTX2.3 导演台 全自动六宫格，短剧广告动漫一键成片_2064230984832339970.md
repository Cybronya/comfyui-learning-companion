---
key: 视频生成/图生视频/魔改 LTX2.3 导演台 全自动六宫格，短剧广告动漫一键成片_2064230984832339970.json
name: 魔改 LTX2.3 导演台 全自动六宫格，短剧广告动漫一键成片_2064230984832339970.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/魔改 LTX2.3 导演台 全自动六宫格，短剧广告动漫一键成片_2064230984832339970.json
hash: a813cda567fcaf77
coverage: 0.969697
learned_at: 2026-10-15 22:39:21
nodes: [LTXVConcatAVLatent, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, LTXVCropGuides, LTXVSeparateAVLatent, LTXDirectorGuide, SamplerCustomAdvanced, VAEDecodeTiled, VRAM_Debug, LTXVAudioVAEDecode, Label (rgthree), Label (rgthree), Label (rgthree), CR Text, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ConditioningZeroOut, LTXVConditioning, ShowText|pysssss, LoraLoaderModelOnly, CS-LTXGridDirector, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, RH_LLMAPI_Pro_Node, CompressImages, SaveMP4]
patterns: []
missing: []
---

# 视频生成/图生视频/魔改 LTX2.3 导演台 全自动六宫格，短剧广告动漫一键成片_2064230984832339970.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064230984832339970.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXDirectorGuide`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `VRAM_Debug`
- `LTXVAudioVAEDecode` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `CR Text`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `LTXVConditioning`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `CS-LTXGridDirector`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `RH_LLMAPI_Pro_Node`
- `CompressImages`
- `SaveMP4`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXDirectorGuide`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`VRAM_Debug`、`LTXVAudioVAEDecode`、`Label (rgthree)`、`CR Text`、`LoadImage`、`LoraLoaderModelOnly`、`UNETLoader`、`ConditioningZeroOut`、`LTXVConditioning`、`CS-LTXGridDirector`、`DualCLIPLoader`、`VAELoaderKJ`、`RH_LLMAPI_Pro_Node`、`CompressImages`、`SaveMP4`

**用到的条目**：LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
