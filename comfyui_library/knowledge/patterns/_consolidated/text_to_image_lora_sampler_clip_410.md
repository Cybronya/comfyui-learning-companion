---
name: text_to_image_lora_sampler_clip_410
type: Text To Image
frequency: 5
level: strong
coverage: 0.8996
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyImage, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/DLSS5超分放大视频生成_视频超分辨率增强处理_2100422243741425665.json, 视频生成/图生视频/H3_Max_Turbo图生视频_首尾帧视频生成工具_2100424763167563778.json, 视频生成/图生视频/H3极速版Turbo加速视频生成处理工作流_2101019073734864897.json, 视频生成/图生视频/H3极速版工作流_Turbo加速快速出片视频生成_2100509732602728450.json, 视频生成/图生视频/RH Upscale双版本视频放大 极速高清视频超分处理工具_2113060056517402625.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_410

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/DLSS5超分放大视频生成_视频超分辨率增强处理_2100422243741425665.json、视频生成/图生视频/H3_Max_Turbo图生视频_首尾帧视频生成工具_2100424763167563778.json、视频生成/图生视频/H3极速版Turbo加速视频生成处理工作流_2101019073734864897.json、视频生成/图生视频/H3极速版工作流_Turbo加速快速出片视频生成_2100509732602728450.json、视频生成/图生视频/RH Upscale双版本视频放大 极速高清视频超分处理工具_2113060056517402625.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `SaveVideo` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `RH_MinimaxH3MaxTurboImageToVideo` —— 3/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `孤海注释` —— 2/5 个有
- `LoadVideo` —— 1/5 个有
- `RH_DLSS5Enhance` —— 1/5 个有
- `RH_RhartVideoVideoUpscaler` —— 1/5 个有
- `RH_Upscale` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `VHS_VideoCombine` —— 1/5 个有
- `VHS_VideoInfoLoaded` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
