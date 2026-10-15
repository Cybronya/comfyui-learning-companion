---
key: 视频生成/文生视频/提示词自动反推！！Wan2.2 Bernini Plus版节点 视频编辑工作流v2版_2071946665900208129.json
name: 提示词自动反推！！Wan2.2 Bernini Plus版节点 视频编辑工作流v2版_2071946665900208129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/提示词自动反推！！Wan2.2 Bernini Plus版节点 视频编辑工作流v2版_2071946665900208129.json
hash: d9d159fcb5890b2b
coverage: 0.942308
learned_at: 2026-10-15 22:48:37
nodes: [WanAnimatePlus SetBlockSwap, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus SetLoRAs, WanAnimatePlus Samplerv2, Label (rgthree), Label (rgthree), Label (rgthree), WanAnimatePlus BlockSwap, WanAnimatePlus ContextOptions, WanAnimatePlus VAELoader, INTConstant, SimpleMath+, LoadImage, LoadImage, WanAnimatePlus LoraSelectMulti, WanAnimatePlus LoraSelectMulti, INTConstant, WanAnimatePlus Decode, Seed (rgthree), VHS_LoadVideo, INTConstant, WanAnimatePlus Samplerv2, WanAnimatePlus Schedulerv2, WanAnimatePlus Schedulerv2, StringFunction|pysssss, PreviewAny, CreateVideo, MarkdownNote, ImageResizeKJv2, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, WanAnimatePlus TextEncodeCached, PreviewAny, Label (rgthree), Label (rgthree), WanAnimatePlus Bernini, WanAnimatePlus SamplerExtraArgs, LoadImage, WanAnimatePlus ModelLoader, WanAnimatePlus ModelLoader, LoadImage, VHS_VideoInfoLoaded, VHS_VideoCombine, RHLLMChatNode, Label (rgthree), RHLLMChatNode, BerniniPromptEnhancer, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/提示词自动反推！！Wan2.2 Bernini Plus版节点 视频编辑工作流v2版_2071946665900208129.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/提示词自动反推！！Wan2.2 Bernini Plus版节点 视频编辑工作流v2版_2071946665900208129.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（52 个）：
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus Samplerv2` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus VAELoader`
- `INTConstant`
- `SimpleMath+`
- `LoadImage`
- `LoadImage`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus LoraSelectMulti`
- `INTConstant`
- `WanAnimatePlus Decode`
- `Seed (rgthree)`
- `VHS_LoadVideo`
- `INTConstant`
- `WanAnimatePlus Samplerv2` ★核心
- `WanAnimatePlus Schedulerv2`
- `WanAnimatePlus Schedulerv2`
- `StringFunction|pysssss`
- `PreviewAny`
- `CreateVideo`
- `MarkdownNote`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanAnimatePlus TextEncodeCached`
- `PreviewAny`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanAnimatePlus Bernini`
- `WanAnimatePlus SamplerExtraArgs` ★核心
- `LoadImage`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus ModelLoader`
- `LoadImage`
- `VHS_VideoInfoLoaded`
- `VHS_VideoCombine`
- `RHLLMChatNode`
- `Label (rgthree)`
- `RHLLMChatNode`
- `BerniniPromptEnhancer`
- `LoadImage`

## 知识

覆盖率 **94%**（49/52）

**有卡**：`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus Samplerv2`、`Label (rgthree)`、`WanAnimatePlus BlockSwap`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus VAELoader`、`INTConstant`、`SimpleMath+`、`LoadImage`、`WanAnimatePlus LoraSelectMulti`、`WanAnimatePlus Decode`、`Seed (rgthree)`、`VHS_LoadVideo`、`WanAnimatePlus Schedulerv2`、`StringFunction|pysssss`、`CreateVideo`、`ImageResizeKJv2`、`WanAnimatePlus TextEncodeCached`、`WanAnimatePlus Bernini`、`WanAnimatePlus SamplerExtraArgs`、`WanAnimatePlus ModelLoader`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`RHLLMChatNode`、`BerniniPromptEnhancer`

**用到的条目**：LoadImage、Seed (rgthree)、WanAnimatePlus SamplerExtraArgs、WanAnimatePlus Samplerv2、WanAnimatePlus Decode、WanAnimatePlus TextEncodeCached、WanAnimatePlus VAELoader、WanAnimatePlus LoraSelectMulti
