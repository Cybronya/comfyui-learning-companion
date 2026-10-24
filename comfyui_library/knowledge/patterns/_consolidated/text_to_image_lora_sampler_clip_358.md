---
name: text_to_image_lora_sampler_clip_358
type: Text To Image
frequency: 5
level: strong
coverage: 0.8108
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图像颜色匹配处理｜图生图色调统一工作流制作_2096325676101099521.json, 图片生成/图生图/服装模特换装多图融合官方稳定版工作流，服装展示图生图处理工具_2107211199963295745.json, 图片生成/图生图/服装模特换装多图融合｜官方稳定版服装展示图生图_2106968194085904385.json, 图片生成/文生图/官方稳定版超强一致性｜全能图片G-2.0图生图直出_2093812472296853505.json, 图片生成/文生图/超强一致性官方稳定版｜全能图片G-2.0图生图替换_2094031047418802178.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_358

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/图像颜色匹配处理｜图生图色调统一工作流制作_2096325676101099521.json、图片生成/图生图/服装模特换装多图融合官方稳定版工作流，服装展示图生图处理工具_2107211199963295745.json、图片生成/图生图/服装模特换装多图融合｜官方稳定版服装展示图生图_2106968194085904385.json、图片生成/文生图/官方稳定版超强一致性｜全能图片G-2.0图生图直出_2093812472296853505.json、图片生成/文生图/超强一致性官方稳定版｜全能图片G-2.0图生图替换_2094031047418802178.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG2OfficialImageToImage` —— 4/5 个有
- `PreviewImage` —— 2/5 个有
- `RH_RhartImageNProOfficialEdit` —— 2/5 个有
- `ColorMatchPro` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `InvertMask` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `区域颜色匹配` —— 1/5 个有

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
