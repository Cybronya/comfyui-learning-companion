---
name: text_to_image_lora_sampler_clip_80
type: Text To Image
frequency: 15
level: strong
coverage: 0.887267
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/手办创建_2108026254615203841.json, 图片生成/图生图/手办创建图生图，照片一键变收藏级手办模型_2112272916351111169.json, 图片生成/图生图/批量图片高清放大zip多图加SeedVR2，电商主图详情页印刷素材批量高清_2106816793737256962.json, 图片生成/图生图/换下装裤子裙子替换生成｜Image2下装设计_2094556599502327810.json, 图片生成/图生图/正面全身去头强制右侧高清特写面部特征文生图处理工具_2102164933382332417.json, 图片生成/图生图/照片光影重构十种风格图生图处理生成工作流工具_2101763548941733889.json, 图片生成/图生图/照片渲染灯光自由控｜图生图按心意调整光源氛围_2101542677861986306.json, 图片生成/图生图/空白工作流_2112112425230225410.json, 图片生成/图生图/英国饰品海报生成工作流｜图生图英伦风饰品图批量出_2099165549824663554.json, 图片生成/图生图/越南饰品海报快速生成｜图生图东南亚风格电商海报一步到位_2099162981023182849.json, 图片生成/图生图/软装搭配分析工作流 室内设计方案辅助生成_2105427749509881858.json, 图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图一键出图_2093788695898968066.json, 图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图直出_2093455106091077633.json, 图片生成/文生图/全能图片G IMAGE 2.5 Sunburst编辑流｜一致性在线，改图不跑偏_2099524674781794306.json, 图片生成/文生图/全能图片全能图片G2.5文生图与图生图 角色一致性高质量创作_2098123716503891970.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_80

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/手办创建_2108026254615203841.json、图片生成/图生图/手办创建图生图，照片一键变收藏级手办模型_2112272916351111169.json、图片生成/图生图/批量图片高清放大zip多图加SeedVR2，电商主图详情页印刷素材批量高清_2106816793737256962.json、图片生成/图生图/换下装裤子裙子替换生成｜Image2下装设计_2094556599502327810.json、图片生成/图生图/正面全身去头强制右侧高清特写面部特征文生图处理工具_2102164933382332417.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 14/15 个有
- `孤海注释` —— 14/15 个有
- `RH_RhartImageG2ImageToImage` —— 9/15 个有
- `RH_RhartImageG25SunburstImageToImage` —— 5/15 个有
- `CR Prompt Text` —— 4/15 个有
- `Fast Groups Bypasser (rgthree)` —— 2/15 个有
- `CheckpointLoaderSimple` —— 1/15 个有
- `RHUploadZip_V2` —— 1/15 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/15 个有
- `SeedVR2` —— 1/15 个有
- `TextEncodeQwenImageEditPlus` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（17/15 个样本）：Steps较低可能导致细节不足
