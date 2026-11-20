---
name: text_to_image_lora_sampler_clip_432
type: Text To Image
frequency: 4
level: moderate
coverage: 0.81425
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DepthAnythingV2Preprocessor, EmptyLatentImage, KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, LoadImage, PreviewAny, SaveImage, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2-深度控制图片反推生图_2077206480499077122.json, 图片生成/图生图/krea2_深度控制姿势图生图（反推+Cosplay人像lora）_2081293171086151681.json, 图片生成/文生图/Krea2-深度控制文生图_2077200610818088962.json, 图片生成/文生图/Krea2-深度控制文生图_2078085516737736705.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_432

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Krea2-深度控制图片反推生图_2077206480499077122.json、图片生成/图生图/krea2_深度控制姿势图生图（反推+Cosplay人像lora）_2081293171086151681.json、图片生成/文生图/Krea2-深度控制文生图_2077200610818088962.json、图片生成/文生图/Krea2-深度控制文生图_2078085516737736705.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DepthAnythingV2Preprocessor`
- `EmptyLatentImage`
- `KSampler`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `LoadImage`
- `PreviewAny`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `ConditioningKrea2Rebalance` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `CR Prompt Text` —— 1/4 个有
- `DF_String_Concatenate` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `TextConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 512 | 512 - 1024 | 4 | 65% |
| 高度 | 512 | 512 - 1024 | 4 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 1024，4 个样本
- 高度 中位数 512，观测区间 512 - 1024，4 个样本
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
