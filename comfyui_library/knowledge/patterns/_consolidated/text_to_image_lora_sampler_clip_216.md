---
name: text_to_image_lora_sampler_clip_216
type: Text To Image
frequency: 9
level: strong
coverage: 0.829444
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/素材贴图工作流｜图生图图片合成贴合一键处理_2093822524541984769.json, 图片生成/图生图/美国风格饰品海报生成 适配海外营销活动审美_2098843930614915074.json, 图片生成/图生图/美国饰品海报生成器｜图生图快速产出美式风格电商主图_2099158449912377345.json, 图片生成/图生图/老照片修复全能｜Gimage20高清图像图生图_2092930600964546562.json, 图片生成/图生图/英国饰品海报生成工作流｜图生图英伦风饰品图批量出_2099165549824663554.json, 图片生成/图生图/贴图工作流，图生图实现纹理贴图与材质合成_2102891450584358913.json, 图片生成/图生图/贴图工作流，图生图实现纹理贴图与材质合成_2104744667005939714.json, 图片生成/图生图/贴图素材一键工作流｜图生图贴图处理高清生成_2094036639810154498.json, 图片生成/文生图/GGPPTT-image2全能图片组件｜文生图图片编辑工作流_2097808293908541441.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_216

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/素材贴图工作流｜图生图图片合成贴合一键处理_2093822524541984769.json、图片生成/图生图/美国风格饰品海报生成 适配海外营销活动审美_2098843930614915074.json、图片生成/图生图/美国饰品海报生成器｜图生图快速产出美式风格电商主图_2099158449912377345.json、图片生成/图生图/老照片修复全能｜Gimage20高清图像图生图_2092930600964546562.json、图片生成/图生图/英国饰品海报生成工作流｜图生图英伦风饰品图批量出_2099165549824663554.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 8/9 个有
- `RH_RhartImageG2ImageToImage` —— 7/9 个有
- `CR Text` —— 4/9 个有
- `ChordLoadModel` —— 4/9 个有
- `ChordMaterialEstimation` —— 4/9 个有
- `ChordNormalToHeight` —— 4/9 个有
- `Image Comparer (rgthree)` —— 4/9 个有
- `PreviewImage` —— 3/9 个有
- `RH_RhartImageG25SunburstImageToImage` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `LayerUtility: TextBox` —— 1/9 个有
- `RH_RhartImageG2TextToImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
