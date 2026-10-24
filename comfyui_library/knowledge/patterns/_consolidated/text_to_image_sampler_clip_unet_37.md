---
name: text_to_image_sampler_clip_unet_37
type: Text To Image
frequency: 13
level: weak
coverage: 0.984231
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FinePorn_Krea2基础工作流V3_2098728252046135298.json, 图片生成/文生图/KOOK_Zimage_底膜直出_2016539613388607489.json, 图片生成/文生图/Kook_Zimage_真实幻想_Turbo_1995721892386451457.json, 图片生成/文生图/Qwen2512文生图基础款_2024281731670482946.json, 图片生成/文生图/Qwen2512日系少女甜妹美女_2019045029121101826.json, 图片生成/文生图/Qwen2512油亮丝袜马油连裤袜美女_2018144682206826497.json, 图片生成/文生图/Qwen2512长腿背影美女壁纸_2019744706971832322.json, 图片生成/文生图/Qwen2512黑丝大雷JK美女_2018170744202600449.json, 图片生成/文生图/Qwen2512黑丝甜妹JK美女_2018135200768724993.json, 图片生成/文生图/Qwen文生图_2058621505726144513.json, 图片生成/文生图/Y-qwen_image_2512_workflow_2006635024417824770.json, 图片生成/文生图/Zimage_真实幻想_2049416827402457090.json, 图片生成/文生图/（贞贞版）Z-image-Kook真实幻想文生图V1_1995736528510922753.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_37

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/FinePorn_Krea2基础工作流V3_2098728252046135298.json、图片生成/文生图/KOOK_Zimage_底膜直出_2016539613388607489.json、图片生成/文生图/Kook_Zimage_真实幻想_Turbo_1995721892386451457.json、图片生成/文生图/Qwen2512文生图基础款_2024281731670482946.json、图片生成/文生图/Qwen2512日系少女甜妹美女_2019045029121101826.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 11/13 个有
- `ModelSamplingAuraFlow` —— 11/13 个有
- `HFEPostProcessor (lrzjason)` —— 3/13 个有
- `VAEEncode` —— 3/13 个有
- `Power Lora Loader (rgthree)` —— 1/13 个有
- `SDXL Resolutions (JPS)` —— 1/13 个有
- `easy positive` —— 1/13 个有
- `easy promptConcat` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 8 - 50 | 13 | 30% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 13 | 32% |
| 采样算法 | euler | - | 13 | 77% |
| 调度器 | simple | - | 13 | 46% |
| 重绘幅度 | 1 | 0.2 - 1 | 13 | 77% |
| 宽度 | 832 | 768 - 1168 | 13 | 83% |
| 高度 | 1024 | 1024 - 1920 | 13 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，观测区间 8 - 50，13 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，13 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，13 个样本，一致性 77%
- 调度器 最常用 simple，13 个样本，一致性 46%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，13 个样本
- 宽度 中位数 832，观测区间 768 - 1168，13 个样本，取值集中（一致性 83%）
- 高度 中位数 1024，观测区间 1024 - 1920，13 个样本
- 高发问题（7/13 个样本）：Steps较低可能导致细节不足
