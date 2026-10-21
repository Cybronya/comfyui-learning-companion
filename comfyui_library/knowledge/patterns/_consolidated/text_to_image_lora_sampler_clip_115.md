---
name: text_to_image_lora_sampler_clip_115
type: Text To Image
frequency: 9
level: strong
coverage: 0.871667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/服装模特姿势复刻全能PRO官方稳定版工作流，服装展示图生图工具_2107203791136321538.json, 图片生成/图生图/服装模特换装多图融合官方稳定版工作流，服装展示图生图处理工具_2107211199963295745.json, 图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图一键出图_2093788695898968066.json, 图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图直出_2093455106091077633.json, 图片生成/文生图/低价渠道版｜全能图片G-2.0图生图商品替换_2094033849197096961.json, 图片生成/文生图/全能图片G2.5图生图 最强生图模型文生图创作_2099903841104916481.json, 图片生成/文生图/图生图官方稳定版｜全能图片G2.0超强一致性_2093819752287399937.json, 图片生成/文生图/多图文参考出图｜电影海报电商海报设计利器_2101133331265052674.json, 视频生成/图生视频/全能图片2.0多宫格故事板 角色分镜批量出图_2098854307813740546.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_115

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/服装模特姿势复刻全能PRO官方稳定版工作流，服装展示图生图工具_2107203791136321538.json、图片生成/图生图/服装模特换装多图融合官方稳定版工作流，服装展示图生图处理工具_2107211199963295745.json、图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图一键出图_2093788695898968066.json、图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图直出_2093455106091077633.json、图片生成/文生图/低价渠道版｜全能图片G-2.0图生图商品替换_2094033849197096961.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 8/9 个有
- `RH_RhartImageG2ImageToImage` —— 7/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `CR Prompt Text` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `RH_RhartImageNProOfficialEdit` —— 2/9 个有
- `OpenposePreprocessor` —— 1/9 个有
- `Preview from image [Crystools]` —— 1/9 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/9 个有
- `easy imageSave` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
