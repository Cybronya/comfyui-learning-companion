---
name: text_to_image_lora_sampler_clip_141
type: Text To Image
frequency: 11
level: strong
coverage: 0.888636
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/全能图片G2.5双模型自由切换 文生图4K画质输出_2098708483548995586.json, 图片生成/文生图/全能图片G2.5双模型自由切换文生图4K画质_2100270591503847426.json, 图片生成/文生图/全能图片G2.5文生图经济版 低成本多风格高清出图_2099224723895971841.json, 图片生成/文生图/全能图片G2.5经济版Sunburst文生图处理生成工具_2101383650859376641.json, 图片生成/文生图/全能图片G2.5语义拟真文生图 细腻光影复杂构图生成_2099228349863391233.json, 图片生成/文生图/冷冬圣诞夜漫画风出图｜动漫角色分镜文生图_2096901929984151554.json, 图片生成/文生图/动漫二次元风格文生图｜创意插画一键生成工具_2101181321061167106.json, 图片生成/文生图/动漫女孩文生图工作流｜动漫角色插画配图｜小说插图轻松出图_2101862601419481090.json, 图片生成/文生图/咖啡馆漫画风文生图工作流｜动漫角色场景插图｜氛围感出图利器_2101873892548759553.json, 图片生成/文生图/文生图AIGC Image 2.5九图工作流，高质量文本到图像生成方案_2107237308658446338.json, 图片生成/文生图/最强生图模型全能图片G image 2.5，文生图直出_2110840094902018050.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_141

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/全能图片G2.5双模型自由切换 文生图4K画质输出_2098708483548995586.json、图片生成/文生图/全能图片G2.5双模型自由切换文生图4K画质_2100270591503847426.json、图片生成/文生图/全能图片G2.5文生图经济版 低成本多风格高清出图_2099224723895971841.json、图片生成/文生图/全能图片G2.5经济版Sunburst文生图处理生成工具_2101383650859376641.json、图片生成/文生图/全能图片G2.5语义拟真文生图 细腻光影复杂构图生成_2099228349863391233.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
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
- `RH_RhartImageG25SunburstTextToImage` —— 5/11 个有
- `CheckpointLoaderSimple` —— 4/11 个有
- `RH_RhartImageG25FlareTextToImage` —— 4/11 个有
- `ExecutionBlocker` —— 2/11 个有
- `ImpactNeg` —— 2/11 个有
- `MuyeTextEditOutput` —— 2/11 个有
- `PrimitiveBoolean` —— 2/11 个有
- `CR Prompt Text` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
