---
name: text_to_image_lora_sampler_clip_39
type: Text To Image
frequency: 17
level: weak
coverage: 0.913118
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-双采大胸版_2089250736138964993.json, 图片生成/文生图/Krea2-模糊感美女生成_2091102588728074241.json, 图片生成/文生图/Krea2-百变美女2_2094969323881320450.json, 图片生成/文生图/Krea2-百变美女_2093983095182684161.json, 图片生成/文生图/Krea2-美女生成双采_2088668185955491842.json, 图片生成/文生图/Krea2-美女生成语义增强版_2089887983045533698.json, 图片生成/文生图/Krea2模糊感美女生成｜文生图一键直出创作_2091289552974598145.json, 图片生成/文生图/Krea2美女生成双采｜文生图高清直出创作_2091314568529276929.json, 图片生成/文生图/Krea2美女生成语义增强版｜文生图一键生成直出_2091315805886697473.json, 图片生成/文生图/冷冬圣诞夜漫画风出图｜动漫角色分镜文生图_2096901929984151554.json, 图片生成/文生图/动漫二次元风格文生图｜创意插画一键生成工具_2101181321061167106.json, 图片生成/文生图/动漫女孩文生图工作流｜动漫角色插画配图｜小说插图轻松出图_2101862601419481090.json, 图片生成/文生图/双采自用版｜Krea2文生图大胸写真生成_2089470548073078786.json, 图片生成/文生图/百变美女一键生成｜Krea2文生图高清工作流_2094343906937888769.json, 图片生成/文生图/百变美女不锁脸文生图 Krea2 多样人像lora生成_2094219223668191233.json, 图片生成/文生图/精致漫画风文生图工作流｜动漫角色封面插图｜叙事感拉满出片_2101869067136233474.json, 图片生成/文生图/视频跟练｜文生图打造跟练画面素材，健身舞蹈教学好帮手_2107363684484993025.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/Krea2-双采大胸版_2089250736138964993.json、图片生成/文生图/Krea2-模糊感美女生成_2091102588728074241.json、图片生成/文生图/Krea2-百变美女2_2094969323881320450.json、图片生成/文生图/Krea2-百变美女_2093983095182684161.json、图片生成/文生图/Krea2-美女生成双采_2088668185955491842.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleBy` —— 12/17 个有
- `PrimitiveBoolean` —— 12/17 个有
- `PrimitiveStringMultiline` —— 12/17 个有
- `Switch string [Crystools]` —— 12/17 个有
- `JjkText` —— 11/17 个有
- `solarL_SaveImagesToZip` —— 11/17 个有
- `孤海注释` —— 11/17 个有
- `CheckpointLoaderSimple` —— 5/17 个有
- `KSamplerAdvanced` —— 4/17 个有
- `ConditioningRebalanceKrea2` —— 2/17 个有
- `StringConcatenate` —— 2/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 16 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 2.5 - 8 | 17 | 69% |
| 采样算法 | er_sde | - | 17 | 65% |
| 调度器 | beta | - | 17 | 65% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 1024 | 17 | 0% |
| 高度 | 80 | 80 - 1536 | 17 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 31/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，16 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 2.5 - 8，17 个样本
- 采样算法 最常用 er_sde，17 个样本，一致性 65%
- 调度器 最常用 beta，17 个样本，一致性 65%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，17 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，17 个样本，取值分散，一致性仅 0%
- 高发问题（31/17 个样本）：Steps较低可能导致细节不足
