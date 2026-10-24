---
name: text_to_image_lora_sampler_clip_525
type: Text To Image
frequency: 3
level: strong
coverage: 0.808333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, INTConstant, Image Comparer (rgthree), JjkText, JoinStringMulti, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, PreviewAny, PreviewImage, RH_LLMAPI_Pro_Node, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch, easy int]
problems: []
missing: []
members: [图片生成/文生图/批量出动漫文生图模型ANIMA正式版-自动提示词版_2056377666349129729.json, 图片生成/文生图/超强动漫模型ANIMA正式版-全自动版本-快速生图_2055965249399992321.json, 图片生成/文生图/超强动漫模型ANIMA正式版-全自动版本_2055574416897134593.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_525

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/批量出动漫文生图模型ANIMA正式版-自动提示词版_2056377666349129729.json、图片生成/文生图/超强动漫模型ANIMA正式版-全自动版本-快速生图_2055965249399992321.json、图片生成/文生图/超强动漫模型ANIMA正式版-全自动版本_2055574416897134593.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `INTConstant`
- `Image Comparer (rgthree)`
- `JjkText`
- `JoinStringMulti`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageCASharpening+` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `RunningHub Deepcleaner` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `TTP_Image_Assy` —— 1/3 个有
- `TTP_Image_Tile_Batch` —— 1/3 个有
- `TTP_Tile_image_size` —— 1/3 个有
- `easy promptLine` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 1920 - 1920 | 3 | 100% |
| 高度 | 1128 | 1128 - 1128 | 3 | 100% |
| 采样步数 | 40 | 40 - 40 | 3 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1128，观测区间 1128 - 1128，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 40 - 40，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
