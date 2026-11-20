---
key: 平台全量/WanAnimatePlus Bernini无限视频编辑_2062771120050368513.json
name: WanAnimatePlus Bernini无限视频编辑_2062771120050368513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/WanAnimatePlus Bernini无限视频编辑_2062771120050368513.json
hash: 948c4c9455f6d7b6
coverage: 0.833333
learned_at: 2026-11-14 01:07:02
nodes: [WanAnimatePlus SetBlockSwap, WanAnimatePlus Schedulerv2, WanAnimatePlus BlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus Samplerv2, WanAnimatePlus VAELoader, WanAnimatePlus SamplerExtraArgs, WanAnimatePlus ContextOptions, WanAnimatePlus SetBlockSwap, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus ModelLoader, WanAnimatePlus ModelLoader, MarkdownNote, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus Schedulerv2, WanAnimatePlus Samplerv2, LoadImage, LoadImage, ImageResizeKJv2, VHS_LoadVideoFFmpeg, VHS_LoadVideoFFmpeg, ImageResizeKJv2, INTConstant, INTConstant, INTConstant, WanAnimatePlus Bernini, TextInput_, VHS_VideoInfoLoaded, Fast Groups Bypasser (rgthree), LoadImage, BasicScheduler, SplitSigmas, SamplerCustom, KSamplerSelect, UNETLoader, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, PathchSageAttentionKJ, CLIPLoader, VAEDecode, CLIPTextEncode, VAEDecode, VAELoader, BerniniConditioning, CreateVideo, PrimitiveInt, PrimitiveInt, LoadImage, ImageResizeKJv2, ImageResizeKJv2, LoadImage, LoadImage, ImageResizeKJv2, BerniniPromptResultParser, SplitStringByDelimiter, Reroute, CLIPTextEncode, SamplerCustom, ImageResizeKJv2, LoadImage, BatchImagesNode, PrimitiveInt, RH_LLMAPI_NODE, VAELoader, VAELoader, SaveVideo, PreviewAny, Note, BerniniPromptEnhancer, Reroute, PreviewAny, ComfySwitchNode, PreviewAny, PreviewAny, SplitStringByDelimiter, TTP_text_mix, Bool, WanAnimatePlus Decode, VHS_VideoCombine, Fast Groups Bypasser (rgthree), MarkdownNote, TextInput_, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus Bernini]
patterns: []
missing: []
---

# 平台全量/WanAnimatePlus Bernini无限视频编辑_2062771120050368513.json

> 来源文件 `comfyui_library/workflows/平台全量/WanAnimatePlus Bernini无限视频编辑_2062771120050368513.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus Schedulerv2`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus Samplerv2` ★核心
- `WanAnimatePlus VAELoader`
- `WanAnimatePlus SamplerExtraArgs` ★核心
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus ModelLoader`
- `MarkdownNote`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus Schedulerv2`
- `WanAnimatePlus Samplerv2` ★核心
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `VHS_LoadVideoFFmpeg`
- `VHS_LoadVideoFFmpeg`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanAnimatePlus Bernini`
- `TextInput_`
- `VHS_VideoInfoLoaded`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `BasicScheduler`
- `SplitSigmas`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `BerniniConditioning`
- `CreateVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `BerniniPromptResultParser`
- `SplitStringByDelimiter`
- `Reroute`
- `CLIPTextEncode` ★核心
- `SamplerCustom` ★核心
- `ImageResizeKJv2`
- `LoadImage`
- `BatchImagesNode`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `VAELoader`
- `VAELoader`
- `SaveVideo`
- `PreviewAny`
- `Note`
- `BerniniPromptEnhancer`
- `Reroute`
- `PreviewAny`
- `ComfySwitchNode`
- `PreviewAny`
- `PreviewAny`
- `SplitStringByDelimiter`
- `TTP_text_mix`
- `Bool`
- `WanAnimatePlus Decode`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `TextInput_`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus Bernini`

## 知识

覆盖率 **83%**（75/90）

**有卡**：`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus Schedulerv2`、`WanAnimatePlus BlockSwap`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus Samplerv2`、`WanAnimatePlus VAELoader`、`WanAnimatePlus SamplerExtraArgs`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus LoraSelectMulti`、`WanAnimatePlus ModelLoader`、`WanAnimatePlus TextEncodeCached`、`LoadImage`、`ImageResizeKJv2`、`VHS_LoadVideoFFmpeg`、`INTConstant`、`WanAnimatePlus Bernini`、`TextInput_`、`VHS_VideoInfoLoaded`、`BasicScheduler`、`SplitSigmas`、`SamplerCustom`、`KSamplerSelect`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`CLIPLoader`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`BerniniConditioning`、`CreateVideo`、`BerniniPromptResultParser`、`SplitStringByDelimiter`、`BatchImagesNode`、`RH_LLMAPI_NODE`、`SaveVideo`、`BerniniPromptEnhancer`、`TTP_text_mix`、`Bool`、`WanAnimatePlus Decode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect
