---
name: text_to_image_lora_sampler_clip_298
type: Text To Image
frequency: 7
level: strong
coverage: 0.897286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图通用转换工作流｜图像再生成高质量处理_2095095993237860353.json, 图片生成/图生图/图生图｜Seedream 5.0 Pro重绘高质量，细节还原度拉满_2099869989200293890.json, 图片生成/图生图/埃及饰品海报图生图方案｜古埃及风饰品宣传图批量产出_2099164243470938113.json, 图片生成/图生图/基础产品展示图生图 商品素材图生成处理工具_2099227769531097089.json, 图片生成/图生图/沙特饰品海报工作流｜图生图批量做沙特风珠宝宣传图_2099161734425694210.json, 图片生成/图生图/西班牙饰品海报制作神器｜图生图欧式风情饰品海报量产_2099166819130105858.json, 图片生成/文生图/全自动电商出图工作流，文生图电商产品图像处理工具_2107249551341080578.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_298

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/图生图通用转换工作流｜图像再生成高质量处理_2095095993237860353.json、图片生成/图生图/图生图｜Seedream 5.0 Pro重绘高质量，细节还原度拉满_2099869989200293890.json、图片生成/图生图/埃及饰品海报图生图方案｜古埃及风饰品宣传图批量产出_2099164243470938113.json、图片生成/图生图/基础产品展示图生图 商品素材图生成处理工具_2099227769531097089.json、图片生成/图生图/沙特饰品海报工作流｜图生图批量做沙特风珠宝宣传图_2099161734425694210.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/7 个有
- `RH_RhartImageG2ImageToImage` —— 4/7 个有
- `RH_RhartImageG2OfficialImageToImage` —— 3/7 个有
- `DisplayImageFromURL` —— 2/7 个有
- `Text` —— 2/7 个有
- `ImageScaleBy` —— 1/7 个有
- `LayerUtility: ImageAutoCrop V2` —— 1/7 个有
- `RH_SeedreamV5ProImageToImage` —— 1/7 个有
- `easy imageConcat` —— 1/7 个有
- `easy promptLine` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
