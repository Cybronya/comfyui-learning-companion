---
name: unknown_workflow_lora_sampler_unet_129
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8344
common_nodes: [Any Switch (rgthree), CLIPLoader, Fast Groups Bypasser (rgthree), FastCanvas, FastCanvasTool, GetImageSize+, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MuyeTextEditOutput, PainterFluxImageEdit, RH_Translator, RMBG, SaveImage, UNETLoader, VAEDecode, VAELoader, easy int, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux_Klein_4步自适应光照溶图打光｜合并模式+分层模式｜ 可控产品大小位置_2033938465968099329.json, 图片生成/图生图/Flux_Klein_4步自适应光照溶图打光｜合并模式+分层模式｜ 可控产品大小位置_2087368260277850114.json, 图片生成/图生图/Flux_Klein_4步自适应光照溶图打光｜合并模式+分层模式｜_可控产品大小位置_2087384692252299266.json, 图片生成/图生图/Flux_Klein_4步自适应光照溶图打光｜合并模式+分层模式｜_可控产品大小位置_2096783273878970369.json, 图片生成/图生图/Flux_Klein_4步自适应光照溶图打光｜合并模式+分层模式｜_可控产品大小位置_2096884009337974786.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_129

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux_Klein_4步自适应光照溶图打光｜合并模式+分层模式｜ 可控产品大小位置_2033938465968099329.json、图片生成/图生图/Flux_Klein_4步自适应光照溶图打光｜合并模式+分层模式｜ 可控产品大小位置_2087368260277850114.json、图片生成/图生图/Flux_Klein_4步自适应光照溶图打光｜合并模式+分层模式｜_可控产品大小位置_2087384692252299266.json、图片生成/图生图/Flux_Klein_4步自适应光照溶图打光｜合并模式+分层模式｜_可控产品大小位置_2096783273878970369.json、图片生成/图生图/Flux_Klein_4步自适应光照溶图打光｜合并模式+分层模式｜_可控产品大小位置_2096884009337974786.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FastCanvas`
- `FastCanvasTool`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MuyeTextEditOutput`
- `PainterFluxImageEdit`
- `RH_Translator`
- `RMBG`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
