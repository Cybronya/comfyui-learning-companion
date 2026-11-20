---
key: 平台全量/最强视频编辑工作流！Wan2.2 Bernini  提示词自动反推版！！_2062879748874919937.json
name: 最强视频编辑工作流！Wan2.2 Bernini  提示词自动反推版！！_2062879748874919937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/最强视频编辑工作流！Wan2.2 Bernini  提示词自动反推版！！_2062879748874919937.json
hash: d169b7d678eaec82
coverage: 0.9375
learned_at: 2026-11-14 02:15:22
nodes: [WanAnimatePlus SetBlockSwap, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus SetLoRAs, WanAnimatePlus Samplerv2, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanAnimatePlus ContextOptions, WanAnimatePlus VAELoader, INTConstant, SimpleMath+, VHS_VideoInfoLoaded, LoadImage, LoadImage, WanAnimatePlus ModelLoader, WanAnimatePlus ModelLoader, WanAnimatePlus LoraSelectMulti, WanAnimatePlus LoraSelectMulti, INTConstant, WanAnimatePlus Decode, Seed (rgthree), WanAnimatePlus Samplerv2, WanAnimatePlus Schedulerv2, WanAnimatePlus Schedulerv2, StringFunction|pysssss, ImageResizeKJv2, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, WanAnimatePlus TextEncodeCached, Label (rgthree), Label (rgthree), WanAnimatePlus Bernini, WanAnimatePlus SamplerExtraArgs, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, CreateVideo, RHLLMChatNode, PreviewAny, PreviewAny, RHLLMChatNode, BerniniPromptEnhancer, MarkdownNote, INTConstant]
patterns: []
missing: []
---

# 平台全量/最强视频编辑工作流！Wan2.2 Bernini  提示词自动反推版！！_2062879748874919937.json

> 来源文件 `comfyui_library/workflows/平台全量/最强视频编辑工作流！Wan2.2 Bernini  提示词自动反推版！！_2062879748874919937.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（48 个）：
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus Samplerv2` ★核心
- `VHS_VideoCombine`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus VAELoader`
- `INTConstant`
- `SimpleMath+`
- `VHS_VideoInfoLoaded`
- `LoadImage`
- `LoadImage`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus LoraSelectMulti`
- `INTConstant`
- `WanAnimatePlus Decode`
- `Seed (rgthree)`
- `WanAnimatePlus Samplerv2` ★核心
- `WanAnimatePlus Schedulerv2`
- `WanAnimatePlus Schedulerv2`
- `StringFunction|pysssss`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanAnimatePlus TextEncodeCached`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanAnimatePlus Bernini`
- `WanAnimatePlus SamplerExtraArgs` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `CreateVideo`
- `RHLLMChatNode`
- `PreviewAny`
- `PreviewAny`
- `RHLLMChatNode`
- `BerniniPromptEnhancer`
- `MarkdownNote`
- `INTConstant`

## 知识

覆盖率 **94%**（45/48）

**有卡**：`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus Samplerv2`、`VHS_VideoCombine`、`WanAnimatePlus BlockSwap`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus VAELoader`、`INTConstant`、`SimpleMath+`、`VHS_VideoInfoLoaded`、`LoadImage`、`WanAnimatePlus ModelLoader`、`WanAnimatePlus LoraSelectMulti`、`WanAnimatePlus Decode`、`Seed (rgthree)`、`WanAnimatePlus Schedulerv2`、`StringFunction|pysssss`、`ImageResizeKJv2`、`WanAnimatePlus TextEncodeCached`、`Label (rgthree)`、`WanAnimatePlus Bernini`、`WanAnimatePlus SamplerExtraArgs`、`VHS_LoadVideo`、`CreateVideo`、`RHLLMChatNode`、`BerniniPromptEnhancer`

**用到的条目**：LoadImage、Seed (rgthree)、WanAnimatePlus SamplerExtraArgs、WanAnimatePlus Samplerv2、WanAnimatePlus Decode、WanAnimatePlus TextEncodeCached、WanAnimatePlus VAELoader、WanAnimatePlus LoraSelectMulti
