---
name: text_to_image_lora_sampler_clip_458
type: Text To Image
frequency: 4
level: strong
coverage: 0.8445
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图9宫格分镜图一键铺开｜一张参考图拆九格，分镜产出效率直接翻倍_2100480078240108546.json, 图片生成/图生图/提示词优化版ProENG全能图片其它平面设计图生图其它电商产品_2087112252389421057.json, 图片生成/图生图/着装生成器全能图片V1.2｜Pro服装展示图生图_2092390958045425666.json, 图片生成/文生图/Anima文生图图生图洗图 自动提示词优化工作流_2105049035978665986.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_458

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/图生图9宫格分镜图一键铺开｜一张参考图拆九格，分镜产出效率直接翻倍_2100480078240108546.json、图片生成/图生图/提示词优化版ProENG全能图片其它平面设计图生图其它电商产品_2087112252389421057.json、图片生成/图生图/着装生成器全能图片V1.2｜Pro服装展示图生图_2092390958045425666.json、图片生成/文生图/Anima文生图图生图洗图 自动提示词优化工作流_2105049035978665986.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
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
- `CR Text` —— 3/4 个有
- `RHHiddenNodes` —— 3/4 个有
- `RH_LLMAPI_Pro_Node` —— 3/4 个有
- `RH_Nano_Banana2_Image2Image` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `Text` —— 2/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `FLS_SamplerV4` —— 1/4 个有
- `ImageStitch` —— 1/4 个有
- `Int` —— 1/4 个有
- `InversionDemoLazyIndexSwitch` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

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
