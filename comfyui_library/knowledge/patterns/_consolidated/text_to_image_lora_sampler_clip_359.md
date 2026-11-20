---
name: text_to_image_lora_sampler_clip_359
type: Text To Image
frequency: 6
level: strong
coverage: 0.898333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadVideo, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/星光视频超分高清_2109919163597803521.json, 数字人/数字人/RH Upscale双版本RH币API版视频极速高清放大，视频超分工具_2105803495495524354.json, 数字人/数字人/视频高清RH Upscale双模式工作流，数字人视频生视频超分处理工具_2106869306951819265.json, 视频生成/图生视频/RH Upscale双版本视频放大 极速高清视频超分处理工具_2113060056517402625.json, 视频生成/图生视频/星光视频超分高清放大，视频生视频画质增强利器_2113470381557374978.json, 视频生成/图生视频/视频高清RH_Upscale双模式工作流，数字人视频生视频超分处理工具_2109815199111925761.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_359

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/星光视频超分高清_2109919163597803521.json、数字人/数字人/RH Upscale双版本RH币API版视频极速高清放大，视频超分工具_2105803495495524354.json、数字人/数字人/视频高清RH Upscale双模式工作流，数字人视频生视频超分处理工具_2106869306951819265.json、视频生成/图生视频/RH Upscale双版本视频放大 极速高清视频超分处理工具_2113060056517402625.json、视频生成/图生视频/星光视频超分高清放大，视频生视频画质增强利器_2113470381557374978.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `RH_RhartVideoVideoUpscaler` —— 4/6 个有
- `RH_Upscale` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `EmptyImage` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `SaveImage` —— 3/6 个有
- `孤海注释` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `GetVideoComponents` —— 2/6 个有
- `QZ_ResolutionPreset` —— 2/6 个有
- `RH_Astra` —— 2/6 个有
- `RunningHub Deepcleaner` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
