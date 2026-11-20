---
name: text_to_image_sampler_clip_unet_10
type: Text To Image
frequency: 25
level: weak
coverage: 0.93044
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z_image_Doodle style 风格工作流_2014354573992927233.json, 图片生成/文生图/zimage奇幻天宫_2087361360895242241.json, 图片生成/文生图/zimage广告图直出_2016732158576041986.json, 图片生成/文生图/zimage文生图+lora仙逆姚惜雪_2005983053098991617.json, 图片生成/文生图/zimage文生图+全息翼界lora_2014158819462488066.json, 图片生成/文生图/【GUGU】CG唯美画风LORA工作流_2001845384953643010.json, 图片生成/文生图/俯视户外Z-image文生图真实人像质感御姐美女_2041474359600091138.json, 图片生成/文生图/千问qwen-image-2.1文生图_2108106051034894338.json, 图片生成/文生图/千问qwen-image-2.1文生图_2112373946829066242.json, 图片生成/文生图/千问qwen-image-2.1文生图_2113920786338770946.json, 图片生成/文生图/千问qwen-image-2.1文生图｜人像写真美少女风格随心出_2114280952854831105.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜_2107739693239590914.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜_2110564054040403969.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜_2111007985395916802.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜注意仅供学习不可商用_2104770730121588737.json, 图片生成/文生图/图图工作流人像写真｜Krea2文生图摄影出图_2095578272632496130.json, 图片生成/文生图/图图组合文生图玩法｜Krea2 多图融合一键出图_2096264881749184513.json, 图片生成/文生图/文生图ZImage工作流｜多段提示词同时出图神器_2100813214991863810.json, 图片生成/文生图/文生图全能直出｜G-2图片生成 电商平面设计利器_2089464781400002562.json, 图片生成/文生图/文生图基础流｜krea2文生图图生图双模式_2089846295853879298.json, 图片生成/文生图/极速版Krea2 Trubo文生图｜美商极高V2版 美感直接拉满_2105551057450524673.json, 图片生成/文生图/没有AI味文生图｜Z-image Turbo真实模型工作流_2093450819793408001.json, 图片生成/文生图/没有AI味的模型｜Z-image Tubro文生图一键生成_2093784427087360002.json, 平台全量/赛博玄幻修仙者文生图｜CG幻想中国风，动漫角色设计感强_2099925911368982529.json, 平台全量/赛博玄幻湘灵女主｜文生图出中国风动漫女主，幻想感拉满_2099928335701860354.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/文生图/z_image_Doodle style 风格工作流_2014354573992927233.json、图片生成/文生图/zimage奇幻天宫_2087361360895242241.json、图片生成/文生图/zimage广告图直出_2016732158576041986.json、图片生成/文生图/zimage文生图+lora仙逆姚惜雪_2005983053098991617.json、图片生成/文生图/zimage文生图+全息翼界lora_2014158819462488066.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 25 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 22/25 个有
- `LoraLoaderModelOnly` —— 22/25 个有
- `JjkText` —— 19/25 个有
- `solarL_SaveImagesToZip` —— 18/25 个有
- `PreviewImage` —— 12/25 个有
- `孤海注释` —— 12/25 个有
- `ModelSamplingAuraFlow` —— 5/25 个有
- `EmptySD3LatentImage` —— 4/25 个有
- `ZImageLoraModelOnly` —— 3/25 个有
- `PIP_StringConcatenation` —— 1/25 个有
- `PathchSageAttentionKJ` —— 1/25 个有
- `PromptBatchQueue` —— 1/25 个有
- `RH_RhartImageG2TextToImage` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 25 | 27% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 25 | 59% |
| 采样算法 | er_sde | - | 25 | 72% |
| 调度器 | beta | - | 25 | 72% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 宽度 | 80 | 80 - 1920 | 25 | 0% |
| 高度 | 80 | 80 - 1920 | 25 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 35/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，25 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，25 个样本
- 采样算法 最常用 er_sde，25 个样本，一致性 72%
- 调度器 最常用 beta，25 个样本，一致性 72%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1920，25 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，25 个样本，取值分散，一致性仅 0%
- 高发问题（35/25 个样本）：Steps较低可能导致细节不足
