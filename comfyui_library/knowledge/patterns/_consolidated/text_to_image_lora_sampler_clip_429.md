---
name: text_to_image_lora_sampler_clip_429
type: Text To Image
frequency: 4
level: strong
coverage: 0.892
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/无损放大人像专用｜图生图细节增强画质不缩水_2110763959346360321.json, 图片生成/图生图/服装模特姿势复刻全能PRO官方稳定版工作流，服装展示图生图工具_2107203791136321538.json, 图片生成/图生图/服装模特姿势复刻全能PRO版｜官方稳定图生图服装展示_2106933544365940738.json, 图片生成/图生图/服装模特姿势复刻全能PRO版｜官方稳定图生图服装展示_2107649602324357121.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_429

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/无损放大人像专用｜图生图细节增强画质不缩水_2110763959346360321.json、图片生成/图生图/服装模特姿势复刻全能PRO官方稳定版工作流，服装展示图生图工具_2107203791136321538.json、图片生成/图生图/服装模特姿势复刻全能PRO版｜官方稳定图生图服装展示_2106933544365940738.json、图片生成/图生图/服装模特姿势复刻全能PRO版｜官方稳定图生图服装展示_2107649602324357121.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `OpenposePreprocessor` —— 3/4 个有
- `RH_RhartImageNProOfficialEdit` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `DF_Integer` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `Int` —— 1/4 个有
- `JWFloat` —— 1/4 个有
- `LG_Color_Match_V2` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
