---
name: unknown_workflow_lora_sampler_clip_260
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.906
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, Flux2Scheduler, ImageConcatMulti, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/游戏_动漫角色设计（画风参考文生图）二次元可用_2055120295245172737.json, 数字人/数字人/发型替换  - Klein_2083890877629558785.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_260

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/游戏_动漫角色设计（画风参考文生图）二次元可用_2055120295245172737.json、数字人/数字人/发型替换  - Klein_2083890877629558785.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
