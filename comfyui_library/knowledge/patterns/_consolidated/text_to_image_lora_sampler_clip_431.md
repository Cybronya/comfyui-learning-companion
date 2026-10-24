---
name: text_to_image_lora_sampler_clip_431
type: Text To Image
frequency: 4
level: strong
coverage: 0.85425
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/透明抠图一键导出｜AI透明背景图像提取图生图_2093833685442326529.json, 图片生成/图生图/透明抠图一键快速生成｜老孙AI图生图高清处理_2094043648282415105.json, 图片生成/文生图/G2.5 Sunburst文生图 4K画质经济型高效输出_2098290011564240898.json, 图片生成/文生图/全能图片G image 2.5文生图｜最强生图模型直出高清_2110691325665439746.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_431

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/透明抠图一键导出｜AI透明背景图像提取图生图_2093833685442326529.json、图片生成/图生图/透明抠图一键快速生成｜老孙AI图生图高清处理_2094043648282415105.json、图片生成/文生图/G2.5 Sunburst文生图 4K画质经济型高效输出_2098290011564240898.json、图片生成/文生图/全能图片G image 2.5文生图｜最强生图模型直出高清_2110691325665439746.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Anything Everywhere` —— 2/4 个有
- `LayerMask: BiRefNetUltraV2` —— 2/4 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/4 个有
- `LayerMask: MaskPreview` —— 2/4 个有
- `Mute / Bypass Relay (rgthree)` —— 2/4 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/4 个有
- `RH_RhartImageG25FlareTextToImage` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
