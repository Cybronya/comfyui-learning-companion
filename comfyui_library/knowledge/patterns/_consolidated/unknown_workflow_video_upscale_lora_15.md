---
name: unknown_workflow_video_upscale_lora_15
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.653333
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ClownsharKSampler_Beta, EmptyHunyuanLatentVideo, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, LayerFilter: AddGrain, ModelSamplingSD3, PathchSageAttentionKJ, Power Lora Loader (rgthree), PreviewImage, SaveImage, String, StringConcatenate, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, WanVideoNAG]
problems: []
missing: [LayerFilter: AddGrain, easy textSwitch, CR SDXL Aspect Ratio, Power Lora Loader (rgthree), Text Multiline]
members: [图片生成/文生图/1960338805641441282.json, 图片生成/文生图/1982596622628593665.json, 视频生成/图生视频/1958396927266209793.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_15

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1960338805641441282.json、图片生成/文生图/1982596622628593665.json、视频生成/图生视频/1958396927266209793.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ClownsharKSampler_Beta`
- `EmptyHunyuanLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `LayerFilter: AddGrain`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Power Lora Loader (rgthree)`
- `PreviewImage`
- `SaveImage`
- `String`
- `StringConcatenate`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 2/3 个有
- `Int` —— 1/3 个有
- `Joy_caption_two` —— 1/3 个有
- `Joy_caption_two_load` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy textSwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | beta57 | - | 3 | 67% |
| Prompt 约束强度(CFG) | 12 | 3 - 12 | 3 | 53% |
| 采样算法 | 4 | -1 - 4 | 3 | 0% |
| 调度器 | 1 | 0.3 - 1 | 3 | 57% |
| 重绘幅度 | 3.5 | 2 - 3.5 | 3 | 76% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 beta57，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 12，观测区间 3 - 12，3 个样本
- 采样算法 中位数 4，观测区间 -1 - 4，3 个样本，取值分散，一致性仅 0%
- 调度器 中位数 1，观测区间 0.3 - 1，3 个样本
- 重绘幅度 中位数 3.5，观测区间 2 - 3.5，3 个样本
- 风险：重绘幅度 观测到 3.5，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerFilter: AddGrain、easy textSwitch、CR SDXL Aspect Ratio、Power Lora Loader (rgthree)、Text Multiline
