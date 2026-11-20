---
name: image_to_image_sampler_clip_unet_165
type: Image To Image
frequency: 4
level: strong
coverage: 0.938
common_nodes: [CLIPLoader, CLIPTextEncode, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/全能图片 Flux2 Klein 9B Klein  自由镜头  保持人物一致  一图生多角度 全能_2027976434416885762.json, 平台全量/最新 Flux2-Klein-9B 毛坯图转效果图  室内设计  室内装修设计效果图 绿植家居_2016781076991057922.json, 平台全量/自由调节摄影机   Flux-2-klein-9B 多角度可视化控制  一键分镜 多角度镜头控制 图_2026477256801001474.json, 平台全量/角色模特人物多角度生成  最强角度编辑器 一键多角度 可自行切换角度   分镜出图 Flux2_2030847086375215106.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_165

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/全能图片 Flux2 Klein 9B Klein  自由镜头  保持人物一致  一图生多角度 全能_2027976434416885762.json、平台全量/最新 Flux2-Klein-9B 毛坯图转效果图  室内设计  室内装修设计效果图 绿植家居_2016781076991057922.json、平台全量/自由调节摄影机   Flux-2-klein-9B 多角度可视化控制  一键分镜 多角度镜头控制 图_2026477256801001474.json、平台全量/角色模特人物多角度生成  最强角度编辑器 一键多角度 可自行切换角度   分镜出图 Flux2_2030847086375215106.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `QwenMultiangleCameraNode` —— 3/4 个有
- `easy promptList` —— 3/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 6 | 4 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 4 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 6，4 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，4 个样本，取值集中（一致性 96%）
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足
