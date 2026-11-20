---
name: text_to_image_lora_sampler_clip_174
type: Text To Image
frequency: 10
level: strong
coverage: 0.9069
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问3.5 LLAMA大模型对话工作流｜接入指南附飞书文档_2111267612377309186.json, 图片生成/图生图/千问3.5 LLAMA接入工作流｜大模型能力加持其他场景｜玩法自由拓展_2102276173383421953.json, 图片生成/图生图/千问3.5 LLAMA本地推理，动画剧本辅助生成_2111519934110064642.json, 图片生成/图生图/图生图实用重绘工具｜全能图片2.0一键出图_2090818490918854657.json, 图片生成/图生图/埃及饰品海报图生图方案｜古埃及风饰品宣传图批量产出_2099164243470938113.json, 图片生成/图生图/墨西哥风格饰品海报生成 适配海外营销活动审美_2098842391431176193.json, 图片生成/图生图/墨西哥饰品海报批量出图｜图生图一键生成异域风电商素材_2099157197157658626.json, 图片生成/图生图/多视角衣物4张图输入｜服装多角度还原细节不糊_2111814232412086274.json, 图片生成/图生图/沙特饰品海报工作流｜图生图批量做沙特风珠宝宣传图_2099161734425694210.json, 图片生成/图生图/西班牙饰品海报制作神器｜图生图欧式风情饰品海报量产_2099166819130105858.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_174

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/千问3.5 LLAMA大模型对话工作流｜接入指南附飞书文档_2111267612377309186.json、图片生成/图生图/千问3.5 LLAMA接入工作流｜大模型能力加持其他场景｜玩法自由拓展_2102276173383421953.json、图片生成/图生图/千问3.5 LLAMA本地推理，动画剧本辅助生成_2111519934110064642.json、图片生成/图生图/图生图实用重绘工具｜全能图片2.0一键出图_2090818490918854657.json、图片生成/图生图/埃及饰品海报图生图方案｜古埃及风饰品宣传图批量产出_2099164243470938113.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 8/10 个有
- `RH_RhartImageG2ImageToImage` —— 7/10 个有
- `RH_RhartImageG2OfficialImageToImage` —— 3/10 个有
- `easy saveText` —— 3/10 个有
- `llama_cpp_instruct_adv` —— 3/10 个有
- `llama_cpp_model_loader` —— 3/10 个有
- `llama_cpp_parameters` —— 3/10 个有
- `BatchImagesNode` —— 2/10 个有
- `ImpactMakeImageList` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
