---
name: text_to_image_sampler_clip_unet_11
type: Text To Image
frequency: 25
level: weak
coverage: 0.94604
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ernie文生图质感_2044774941454766081.json, 图片生成/文生图/ideogram4_2062708650468265986.json, 图片生成/文生图/krea2 turbo文生图 极致美学_2069948625094012930.json, 图片生成/文生图/krea2 turbo文生图_2069631042172055554.json, 图片生成/文生图/krea2 turbo文生图_2069632468088606722.json, 图片生成/文生图/krea2 turbo文生图_2069636296083075074.json, 图片生成/文生图/krea2 turbo文生图（最新开源，质量极高，速度极快）_2069769763433304066.json, 图片生成/文生图/krea2 文生图 无LORA_2093341821593284609.json, 图片生成/文生图/krea2 文生图 无LORA_2111016861499486209.json, 图片生成/文生图/krea2-Afterlight（光影美学文生图）_2083839367738642434.json, 图片生成/文生图/krea2_ID13_v2_融合prompt_单分支_2086591602310602754.json, 图片生成/文生图/krea2_turbo_基础文生图工作流_2078078374207115266.json, 图片生成/文生图/krea2_对比流_官方vsAnima配方_random_2086586562653024257.json, 图片生成/文生图/krea2基础文生图_2071164326781734914.json, 图片生成/文生图/krea2基础文生图文生图工作流_2089571734700773377.json, 图片生成/文生图/krea2基础文生图高清出图工作流_2089673479443533826.json, 图片生成/文生图/krea2文生图_2087794601284431873.json, "图片生成/文生图/图图的 8D 极光黑丝 Z-Image 工作流_Tutu's Aurora 8D HiSilk Z-Image workflow_2070753635646136322.json", "图片生成/文生图/图图的 PVC 护士服 Z-Image 工作流_Tutu's PVC Nurse Outfit Z-Image workflow_2070438619709526017.json", "图片生成/文生图/图图的大网渔网袜 Z-Image 工作流_Tutu's HiSilk Fishnet Z-Image workflow_2070751109303586818.json", "图片生成/文生图/图图的洛丽塔黑江雫服装工作流_Tutu's Lolita Shizuku Kuroe Outfit workflow_2070374570158284801.json", "图片生成/文生图/图图的长款旗袍风蕾丝连衣裙工作流_Tutu's Long Qipao Lace Dress workflow_2070419601577570306.json", "图片生成/文生图/图图的黑色配饰连体服 Z-Image 工作流_Tutu's HiSilk Black Accessories Z-Image workflow_2070527635050033153.json", "图片生成/文生图/图图的黑色配饰连体服 Z-Image 工作流_Tutu's HiSilk Black Accessories Z-Image workflow_2070749678974627841.json", 图片生成/文生图/（贞贞版）Z image Art文生图_2017605115783421953.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/文生图/ernie文生图质感_2044774941454766081.json、图片生成/文生图/ideogram4_2062708650468265986.json、图片生成/文生图/krea2 turbo文生图 极致美学_2069948625094012930.json、图片生成/文生图/krea2 turbo文生图_2069631042172055554.json、图片生成/文生图/krea2 turbo文生图_2069632468088606722.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

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
- `ConditioningZeroOut` —— 19/25 个有
- `LoraLoaderModelOnly` —— 16/25 个有
- `ConditioningKrea2Rebalance` —— 2/25 个有
- `PrimitiveInt` —— 2/25 个有
- `CompressImages` —— 1/25 个有
- `TextConcat` —— 1/25 个有
- `Textbox` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 40 | 25 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 25 | 0% |
| 采样算法 | er_sde | - | 25 | 36% |
| 调度器 | simple | - | 25 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 宽度 | 1080 | 752 - 1920 | 25 | 77% |
| 高度 | 1536 | 1024 - 1920 | 25 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 40，25 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，25 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 er_sde，25 个样本，一致性 36%
- 调度器 最常用 simple，25 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 752 - 1920，25 个样本
- 高度 中位数 1536，观测区间 1024 - 1920，25 个样本，取值集中（一致性 83%）
