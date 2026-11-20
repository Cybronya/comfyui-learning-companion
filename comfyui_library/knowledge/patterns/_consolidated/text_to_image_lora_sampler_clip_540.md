---
name: text_to_image_lora_sampler_clip_540
type: Text To Image
frequency: 3
level: strong
coverage: 0.778667
common_nodes: [Any Switch (rgthree), Anything Everywhere3, CLIPLoader, CLIPTextEncode, CR Text, ComfySwitchNode, DepthAnythingV2Preprocessor, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Lora Loader Stack (rgthree), LoraLoaderModelOnly, MOSSImageControl, ModelSamplingAuraFlow, PreviewAny, PreviewImage, RHLLMChatNode, ResolutionSelector, SaveImage, SkipLayerGuidanceDiTSimple, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/MOSS全自动提示词生图+洗图工作流合集_2115762978753695745.json, 视频生成/图生视频/MOSS全自动提示词生图+洗图工作流合集_2115957165751103490.json, 视频生成/图生视频/MOSS全自动提示词生图+洗图工作流合集_2115968918291574785.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_540

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/MOSS全自动提示词生图+洗图工作流合集_2115762978753695745.json、视频生成/图生视频/MOSS全自动提示词生图+洗图工作流合集_2115957165751103490.json、视频生成/图生视频/MOSS全自动提示词生图+洗图工作流合集_2115968918291574785.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ComfySwitchNode`
- `DepthAnythingV2Preprocessor`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `Label (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `LoraLoaderModelOnly`
- `MOSSImageControl`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `PreviewImage`
- `RHLLMChatNode`
- `ResolutionSelector`
- `SaveImage`
- `SkipLayerGuidanceDiTSimple`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.75 | 0.75 - 0.75 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.75，观测区间 0.75 - 0.75，3 个样本，取值集中（一致性 100%）
