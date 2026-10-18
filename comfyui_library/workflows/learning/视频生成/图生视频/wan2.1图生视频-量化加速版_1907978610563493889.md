---
key: 视频生成/图生视频/wan2.1图生视频-量化加速版_1907978610563493889.json
name: wan2.1图生视频-量化加速版_1907978610563493889.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1图生视频-量化加速版_1907978610563493889.json
hash: b378d5f24f477cee
coverage: 0.670886
learned_at: 2026-10-15 22:29:27
nodes: [CLIPTextEncode, Int, Note _O, SetNode, SetNode, GetNode, SetNode, SetNode, Note _O, Int, Int, SetNode, ImpactSwitch, SetNode, CR String To Number, CR String To Number, SetNode, Bjornulf_ShowInt, SetNode, Bjornulf_ShowInt, ImpactSwitch, Int, Bjornulf_AnythingToText, Bjornulf_AnythingToText, Bjornulf_AnythingToText, Bjornulf_AnythingToText, GetNode, Int, Bjornulf_AnythingToText, Note _O, JjkText, Int, Int, ImpactSwitch, Int, Bjornulf_AnythingToText, CR String To Number, Note _O, Bjornulf_AnythingToText, Bjornulf_AnythingToText, CR String To Number, SetNode, Int, ImpactSwitch, JjkText, JjkText, Int, Int, CLIPLoader, CLIPVisionLoader, GetNode, GetNode, easy textSwitch, Bjornulf_ShowStringText, Bjornulf_ShowInt, CLIPVisionEncode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, VAEDecode, Int, GetNode, Bjornulf_ShowInt, VHS_VideoCombine, KSampler, mxSlider, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, CLIPTextEncode, WanImageToVideo, VAELoader, UnetLoaderGGUF, JjkText, LoadImage, PathchSageAttentionKJ, WanVideoTeaCacheKJ, mxSlider]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 840188459811136, "steps": 12}
---

# 视频生成/图生视频/wan2.1图生视频-量化加速版_1907978610563493889.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1907978610563493889.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（79 个）：
- `CLIPTextEncode` ★核心
- `Int`
- `Note _O`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Note _O`
- `Int`
- `Int`
- `SetNode`
- `ImpactSwitch`
- `SetNode`
- `CR String To Number`
- `CR String To Number`
- `SetNode`
- `Bjornulf_ShowInt`
- `SetNode`
- `Bjornulf_ShowInt`
- `ImpactSwitch`
- `Int`
- `Bjornulf_AnythingToText`
- `Bjornulf_AnythingToText`
- `Bjornulf_AnythingToText`
- `Bjornulf_AnythingToText`
- `GetNode`
- `Int`
- `Bjornulf_AnythingToText`
- `Note _O`
- `JjkText`
- `Int`
- `Int`
- `ImpactSwitch`
- `Int`
- `Bjornulf_AnythingToText`
- `CR String To Number`
- `Note _O`
- `Bjornulf_AnythingToText`
- `Bjornulf_AnythingToText`
- `CR String To Number`
- `SetNode`
- `Int`
- `ImpactSwitch`
- `JjkText`
- `JjkText`
- `Int`
- `Int`
- `CLIPLoader`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `easy textSwitch`
- `Bjornulf_ShowStringText`
- `Bjornulf_ShowInt`
- `CLIPVisionEncode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `Int`
- `GetNode`
- `Bjornulf_ShowInt`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `mxSlider`
- `ModelSamplingSD3`
- `WanVideoEnhanceAVideoKJ`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `JjkText`
- `LoadImage`
- `PathchSageAttentionKJ`
- `WanVideoTeaCacheKJ`
- `mxSlider`

## 关键参数

- `seed` = `840188459811136`
- `steps` = `12`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（53/79）

**有卡**：`CLIPTextEncode`、`Int`、`Note _O`、`CR String To Number`、`Bjornulf_ShowInt`、`Bjornulf_AnythingToText`、`CLIPLoader`、`CLIPVisionLoader`、`easy textSwitch`、`Bjornulf_ShowStringText`、`CLIPVisionEncode`、`VAEDecode`、`VHS_VideoCombine`、`KSampler`、`mxSlider`、`ModelSamplingSD3`、`WanVideoEnhanceAVideoKJ`、`WanImageToVideo`、`VAELoader`、`UnetLoaderGGUF`、`LoadImage`、`PathchSageAttentionKJ`、`WanVideoTeaCacheKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode、CLIPVisionLoader
