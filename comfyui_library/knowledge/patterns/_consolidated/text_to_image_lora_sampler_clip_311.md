---
name: text_to_image_lora_sampler_clip_311
type: Text To Image
frequency: 7
level: strong
coverage: 0.870714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/全能图片G2.5双模型自由切换 文生图4K画质输出_2098708483548995586.json, 图片生成/文生图/全能图片G2.5双模型自由切换文生图4K画质_2100270591503847426.json, 图片生成/文生图/全能图片G2.5文生图经济版 低成本多风格高清出图_2099224723895971841.json, 图片生成/文生图/全能图片G2.5经济版Sunburst文生图处理生成工具_2101383650859376641.json, 图片生成/文生图/全能图片G2.5语义拟真文生图 细腻光影复杂构图生成_2099228349863391233.json, 图片生成/文生图/文生图AIGC Image 2.5九图工作流，高质量文本到图像生成方案_2107237308658446338.json, 图片生成/文生图/最强生图模型全能图片G image 2.5，文生图直出_2110840094902018050.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_311

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/全能图片G2.5双模型自由切换 文生图4K画质输出_2098708483548995586.json、图片生成/文生图/全能图片G2.5双模型自由切换文生图4K画质_2100270591503847426.json、图片生成/文生图/全能图片G2.5文生图经济版 低成本多风格高清出图_2099224723895971841.json、图片生成/文生图/全能图片G2.5经济版Sunburst文生图处理生成工具_2101383650859376641.json、图片生成/文生图/全能图片G2.5语义拟真文生图 细腻光影复杂构图生成_2099228349863391233.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
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
- `RH_RhartImageG25SunburstTextToImage` —— 5/7 个有
- `RH_RhartImageG25FlareTextToImage` —— 4/7 个有
- `ExecutionBlocker` —— 2/7 个有
- `ImpactNeg` —— 2/7 个有
- `MuyeTextEditOutput` —— 2/7 个有
- `PrimitiveBoolean` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
