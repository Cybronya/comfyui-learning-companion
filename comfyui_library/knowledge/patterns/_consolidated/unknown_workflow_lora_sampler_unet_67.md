---
name: unknown_workflow_lora_sampler_unet_67
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9444
common_nodes: [CLIPLoader, KSampler, LoraLoaderModelOnly, PainterFluxImageEdit, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/klein人像全身白底图 _ 测试中_2090653357085122562.json, 图片生成/图生图/【服装行业】模特服装提取白底图_2017380216762540033.json, 图片生成/图生图/溶图2_2102275717336756225.json, 图片生成/图生图/鞋子换色_2063808483375542273.json, 图片生成/文生图/Flux-Klein去除ai感优化光影效果去水印输入提示词_2071089227948969985.json, 图片生成/文生图/可过小红书FLUX2-Klein去除ai感_2055920772278956034.json, 平台全量/Flux-Klein去除ai感优化光影效果去水印_2071763149207982081.json, 平台全量/Klein_4步自适应光照溶图打光_2020706993845047297.json, 平台全量/flux-2-klein-9b 服饰改颜色  电商产品换颜色 万能真实换色 指定颜色改色 服饰定向换_2045769530487611394.json, 平台全量/服饰改颜色  电商产品换颜色 万能真实换色 指定颜色改色 服饰定向换色 保持材质不变_2045775739311628289.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_67

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/klein人像全身白底图 _ 测试中_2090653357085122562.json、图片生成/图生图/【服装行业】模特服装提取白底图_2017380216762540033.json、图片生成/图生图/溶图2_2102275717336756225.json、图片生成/图生图/鞋子换色_2063808483375542273.json、图片生成/文生图/Flux-Klein去除ai感优化光影效果去水印输入提示词_2071089227948969985.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 9/10 个有
- `GetImageSize+` —— 8/10 个有
- `Image Comparer (rgthree)` —— 8/10 个有
- `CR Text` —— 7/10 个有
- `LoadImage` —— 6/10 个有
- `ImageLoader` —— 5/10 个有
- `ImageStitch` —— 3/10 个有
- `Int` —— 3/10 个有
- `JoinStrings` —— 3/10 个有
- `DetailTransfer` —— 1/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 10 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 10 | 96% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，10 个样本，取值集中（一致性 96%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
