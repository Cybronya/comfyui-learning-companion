---
name: text_to_image_lora_sampler_clip_312
type: Text To Image
frequency: 3
level: strong
coverage: 0.846333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/一句话图像编辑Flux kontext黑森林RunningHub专用节点工作流文生图图生图_2088432747160367105.json, 图片生成/文生图/全能图片G IMAGE 2.5 Sunburst编辑流｜一致性在线，改图不跑偏_2099524674781794306.json, 图片生成/文生图/全能图片G2.5多宫格故事板 Seedance2.0_2.5与H3通用分镜_2098702107397414913.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_312

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/一句话图像编辑Flux kontext黑森林RunningHub专用节点工作流文生图图生图_2088432747160367105.json、图片生成/文生图/全能图片G IMAGE 2.5 Sunburst编辑流｜一致性在线，改图不跑偏_2099524674781794306.json、图片生成/文生图/全能图片G2.5多宫格故事板 Seedance2.0_2.5与H3通用分镜_2098702107397414913.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
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
- `RH_RhartImageG25SunburstImageToImage` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `Bjornulf_ShowStringText` —— 1/3 个有
- `Comfly_Flux_Kontext` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RH_ComfyFluxKontext` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
