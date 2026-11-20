---
name: text_to_image_sampler_clip_unet_13
type: Text To Image
frequency: 23
level: weak
coverage: 0.990087
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FinePorn_Krea2基础工作流V3_2098728252046135298.json, 图片生成/文生图/KOOK_Zimage_底膜直出_2016539613388607489.json, 图片生成/文生图/Kook_Flux_klein_亚洲人像_2019704034847891458.json, 图片生成/文生图/Kook_Zimage_真实幻想_Turbo_1995721892386451457.json, 图片生成/文生图/Qwen Image 文生图，千问基础文生图_2005132413141479426.json, 图片生成/文生图/Qwen image 2512 我的50年_Qwen-Image-2512_2006650484186157057.json, 图片生成/文生图/Qwen image 2512文生图_2008433887889858562.json, 图片生成/文生图/Qwen-Image+Lightning4StepsLora-文生图工作流_1956201968337342466.json, 图片生成/文生图/Qwen-Image-2512 文生图 8步加速_2014683752181538818.json, 图片生成/文生图/Qwen-Image-2512 最新文生图_2006383515574738946.json, 图片生成/文生图/Qwen-Image-2512不用LoRA实现人物一致性_2006694730360430594.json, 图片生成/文生图/Qwen-Image-2512卡通女孩LoRA_2007803177848020993.json, 图片生成/文生图/Qwen-Image-2512四步10秒出图Qwen image 2512_2006497445919854594.json, 图片生成/文生图/Qwen-Image-2512文生图_1953006122934407170.json, 图片生成/文生图/Qwen-Image-2512文生图_2006354179845005313.json, 图片生成/文生图/Qwen-Image-2512的Bill_LoRA_2007418345481576449.json, 图片生成/文生图/Qwen-Image2512中文渲染全系列工作流_2010150714567299074.json, 图片生成/文生图/Qwen2512JK制服甜妹_2018334963661283330.json, 图片生成/文生图/Qwen2512性感迷人身材美女_2017894712933359617.json, 图片生成/文生图/Qwen大雷连体衣美女_2055856373283467265.json, 图片生成/文生图/Zimage_真实幻想_2049416827402457090.json, 图片生成/文生图/qwen2512完美魔鬼身材的美女_2018950663933267969.json, 图片生成/文生图/（贞贞版）Z-image-Kook真实幻想文生图V1_1995736528510922753.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/文生图/FinePorn_Krea2基础工作流V3_2098728252046135298.json、图片生成/文生图/KOOK_Zimage_底膜直出_2016539613388607489.json、图片生成/文生图/Kook_Flux_klein_亚洲人像_2019704034847891458.json、图片生成/文生图/Kook_Zimage_真实幻想_Turbo_1995721892386451457.json、图片生成/文生图/Qwen Image 文生图，千问基础文生图_2005132413141479426.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 21/23 个有
- `ModelSamplingAuraFlow` —— 20/23 个有
- `CompressImages` —— 3/23 个有
- `HFEPostProcessor (lrzjason)` —— 3/23 个有
- `VAEEncode` —— 3/23 个有
- `Power Lora Loader (rgthree)` —— 1/23 个有
- `easy positive` —— 1/23 个有
- `easy promptConcat` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 23 | 21% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 23 | 23% |
| 采样算法 | euler | - | 23 | 91% |
| 调度器 | simple | - | 23 | 78% |
| 重绘幅度 | 1 | 0.2 - 1 | 23 | 83% |
| 宽度 | 1024 | 720 - 1664 | 23 | 79% |
| 高度 | 1280 | 1024 - 1920 | 23 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，23 个样本，取值分散，一致性仅 21%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，23 个样本，取值分散，一致性仅 23%
- 采样算法 最常用 euler，23 个样本，一致性 91%
- 调度器 最常用 simple，23 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，23 个样本，取值集中（一致性 83%）
- 宽度 中位数 1024，观测区间 720 - 1664，23 个样本
- 高度 中位数 1280，观测区间 1024 - 1920，23 个样本
- 高发问题（19/23 个样本）：Steps较低可能导致细节不足
