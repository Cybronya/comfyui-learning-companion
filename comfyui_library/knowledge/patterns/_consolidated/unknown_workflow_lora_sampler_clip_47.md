---
name: unknown_workflow_lora_sampler_clip_47
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.7172
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerAdvanced, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingAuraFlow, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [CR Text, LayerUtility: PurgeVRAM V2]
members: [图片生成/图生图/2091343877964910593.json, 图片生成/文生图/Dark Deco 暗黑装饰艺术 三采工作流（无反推模板）_2081052417982033921.json, 图片生成/文生图/Dark Deco 暗黑装饰艺术 全自动三采工作流_2081041992469012482.json, 图片生成/文生图/Krea2 文生图+三采+TTP高清_2100390063279529986.json, 视频生成/图生视频/2063550240493498369.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2091343877964910593.json、图片生成/文生图/Dark Deco 暗黑装饰艺术 三采工作流（无反推模板）_2081052417982033921.json、图片生成/文生图/Dark Deco 暗黑装饰艺术 全自动三采工作流_2081041992469012482.json、图片生成/文生图/Krea2 文生图+三采+TTP高清_2100390063279529986.json、视频生成/图生视频/2063550240493498369.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageSharpen` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `SeedVR2LoadDiTModel` —— 3/5 个有
- `SeedVR2LoadVAEModel` —— 3/5 个有
- `SeedVR2VideoUpscaler` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `llama_cpp_instruct_adv` —— 3/5 个有
- `llama_cpp_model_loader` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `Int` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `easy getNode` —— 2/5 个有
- `easy setNode` —— 2/5 个有
- `llama_cpp_parameters` —— 2/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有
- `TTP_Image_Assy` —— 1/5 个有
- `TTP_Image_Tile_Batch` —— 1/5 个有
- `TTP_Tile_image_size` —— 1/5 个有
- `easy imageSize` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 5 | 78% |
| 高度 | 1536 | 512 - 1536 | 5 | 69% |
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 40 | 5 | 0% |
| 采样算法 | 1 | 1 - 4 | 5 | 25% |
| 调度器 | euler | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，5 个样本
- 高度 中位数 1536，观测区间 512 - 1536，5 个样本
- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 40，5 个样本，取值分散，一致性仅 0%
- 采样算法 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- 调度器 最常用 euler，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: PurgeVRAM V2
