---
name: text_to_image_lora_sampler_clip_115
type: Text To Image
frequency: 12
level: strong
coverage: 0.884417
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/DeepSeek最新单品工作流， 处理方案_2105805028530409473.json, 图片生成/图生图/G2.5全能图片编辑经济版 低成本图像处理方案_2098301672375283713.json, 图片生成/图生图/Image-2.5九图图生图版本 多图编辑处理_2098304496907669505.json, 图片生成/图生图/qk多场景图工作流 多场景批量生成方案一键搞定_2105133139034202113.json, 图片生成/图生图/qk适用步骤图工作流 分步骤出图方案高效稳定_2105027127480512514.json, 图片生成/图生图/全能图片2.5电商低成本生图 单张低至0.21元_2098862195231772674.json, 图片生成/图生图/全能图片G-2.5低价版图片编辑｜角色设计与分镜生成出图，图生图成本打下来_2100423600812679170.json, 图片生成/图生图/全能图片G2.5图片编辑低价版 图生图处理工具_2100688455109009410.json, 图片生成/图生图/最新单品deepseek 图像编辑方案高质量_2109433966536253442.json, 图片生成/文生图/全能图片G-2.5低价版｜文生图局部重绘图片编辑_2101197387636236289.json, 图片生成/文生图/全能图片G-image-2.5 文生图与图生图双模图像处理_2098633491339636738.json, 图片生成/文生图/全能图片G-image-2.5｜文生图图生图一应俱全_2098719464136204289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_115

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/DeepSeek最新单品工作流， 处理方案_2105805028530409473.json、图片生成/图生图/G2.5全能图片编辑经济版 低成本图像处理方案_2098301672375283713.json、图片生成/图生图/Image-2.5九图图生图版本 多图编辑处理_2098304496907669505.json、图片生成/图生图/qk多场景图工作流 多场景批量生成方案一键搞定_2105133139034202113.json、图片生成/图生图/qk适用步骤图工作流 分步骤出图方案高效稳定_2105027127480512514.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
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
- `RH_RhartImageG25SunburstImageToImage` —— 8/12 个有
- `RH_RhartImageG25FlareImageToImage` —— 7/12 个有
- `RH_RhartImageG25SunburstTextToImage` —— 6/12 个有
- `RH_RhartImageG25FlareTextToImage` —— 5/12 个有
- `JWStringConcat` —— 4/12 个有
- `Text` —— 4/12 个有
- `Fast Groups Muter (rgthree)` —— 3/12 个有
- `MuyeTextEditOutput` —— 3/12 个有
- `JjkShowText` —— 2/12 个有
- `RH_LLMAPI_NODE` —— 2/12 个有
- `SaveText` —— 2/12 个有
- `VRGDG_LocalLLM` —— 2/12 个有
- `CR Prompt Text` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
