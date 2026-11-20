---
name: unknown_workflow_sampler_clip_unet_489
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7835
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyImage, Flux2Scheduler, GetImageSizeAndCount, GetNode, KSamplerSelect, Qwen3VL_Chat, RH_LLMAPI_NODE, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, StringFunction|pysssss, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/生图-文生图(角色白底图)-FLUX2-Klein_2013161608507301890.json, 图片生成/文生图/生图-文生图自动-FLUX2-Klein_2012451327334420481.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_489

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/生图-文生图(角色白底图)-FLUX2-Klein_2013161608507301890.json、图片生成/文生图/生图-文生图自动-FLUX2-Klein_2012451327334420481.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyImage`
- `Flux2Scheduler`
- `GetImageSizeAndCount`
- `GetNode`
- `KSamplerSelect`
- `Qwen3VL_Chat`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `StringFunction|pysssss`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
