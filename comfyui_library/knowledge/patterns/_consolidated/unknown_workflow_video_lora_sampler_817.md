---
name: unknown_workflow_video_lora_sampler_817
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9045
common_nodes: [BerniniPromptEnhancer, CreateVideo, INTConstant, ImageResizeKJv2, LoadImage, PreviewAny, Seed (rgthree), SimpleMath+, StringFunction|pysssss, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus Bernini, WanAnimatePlus BlockSwap, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SamplerExtraArgs, WanAnimatePlus Samplerv2, WanAnimatePlus Schedulerv2, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2064109526978224129.json, 视频生成/文生视频/提示词自动反推！！Wan2.2 Bernini Plus版节点 视频编辑工作流v2版_2071946665900208129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_817

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2064109526978224129.json、视频生成/文生视频/提示词自动反推！！Wan2.2 Bernini Plus版节点 视频编辑工作流v2版_2071946665900208129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `BerniniPromptEnhancer`
- `CreateVideo`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewAny`
- `Seed (rgthree)`
- `SimpleMath+`
- `StringFunction|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimatePlus Bernini`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SamplerExtraArgs`
- `WanAnimatePlus Samplerv2`
- `WanAnimatePlus Schedulerv2`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
