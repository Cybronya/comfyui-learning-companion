---
name: text_to_image_lora_sampler_clip_179
type: Text To Image
frequency: 5
level: strong
coverage: 0.8786
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/视频高清RH Upscale双模式工作流，数字人视频生视频超分处理工具_2106869306951819265.json, 视频生成/图生视频/MiniMax H3电影MV一键生成 图生视频创作工具_2098834260370219009.json, 视频生成/图生视频/RH Upscale视频极速高清放大工作流，PR插件适配视频超分工具_2106535133057740802.json, 视频生成/图生视频/minimaxH3电影MV一键成片工作流｜图生视频直出大片质感_2099107946394378241.json, 视频生成/图生视频/视频高清RH_Upscale双模式工作流，数字人视频生视频超分处理工具_2109815199111925761.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_179

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/视频高清RH Upscale双模式工作流，数字人视频生视频超分处理工具_2106869306951819265.json、视频生成/图生视频/MiniMax H3电影MV一键生成 图生视频创作工具_2098834260370219009.json、视频生成/图生视频/RH Upscale视频极速高清放大工作流，PR插件适配视频超分工具_2106535133057740802.json、视频生成/图生视频/minimaxH3电影MV一键成片工作流｜图生视频直出大片质感_2099107946394378241.json、视频生成/图生视频/视频高清RH_Upscale双模式工作流，数字人视频生视频超分处理工具_2109815199111925761.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 4/5 个有
- `孤海注释` —— 4/5 个有
- `LoadVideo` —— 3/5 个有
- `RH_Upscale` —— 3/5 个有
- `SaveImage` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `GetVideoComponents` —— 2/5 个有
- `NanFengH3MultiReferenceGeneratorV10` —— 2/5 个有
- `RH_RhartVideoVideoUpscaler` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SaveVideo` —— 1/5 个有

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
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
