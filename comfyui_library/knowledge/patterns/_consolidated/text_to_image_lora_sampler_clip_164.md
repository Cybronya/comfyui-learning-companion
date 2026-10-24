---
name: text_to_image_lora_sampler_clip_164
type: Text To Image
frequency: 10
level: strong
coverage: 0.8987
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片去水印免蒙版｜YOLO自动检测标记，一键擦除更省心_2100192477151055873.json, 图片生成/图生图/图片去水印｜LaMa修复引擎补图，擦除痕迹几乎看不见_2099935925890543617.json, 图片生成/图生图/图片去水印｜LaMa修复引擎补图，擦除痕迹几乎看不见_2100193279357837314.json, 图片生成/图生图/墨西哥风格饰品海报生成 适配海外营销活动审美_2098842391431176193.json, 图片生成/图生图/墨西哥饰品海报批量出图｜图生图一键生成异域风电商素材_2099157197157658626.json, 图片生成/图生图/多视角衣物4张图输入｜服装多角度还原细节不糊_2111814232412086274.json, 图片生成/图生图/宠物拟人工作流｜毛孩子照片秒变拟人角色，新奇创意_2099899324359602178.json, 图片生成/图生图/角色战技连招设定卡Seedance与MiniMax H3图生图工具_2101008188308017153.json, 图片生成/图生图/角色战技连招设定卡生成｜Seedance2.0与MiniMaxH3专用_2096718130381938689.json, 图片生成/图生图/角色战技连招设定卡｜Seedance2.0与2.5及MiniMaxH3专用_2100765592633569281.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_164

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图片去水印免蒙版｜YOLO自动检测标记，一键擦除更省心_2100192477151055873.json、图片生成/图生图/图片去水印｜LaMa修复引擎补图，擦除痕迹几乎看不见_2099935925890543617.json、图片生成/图生图/图片去水印｜LaMa修复引擎补图，擦除痕迹几乎看不见_2100193279357837314.json、图片生成/图生图/墨西哥风格饰品海报生成 适配海外营销活动审美_2098842391431176193.json、图片生成/图生图/墨西哥饰品海报批量出图｜图生图一键生成异域风电商素材_2099157197157658626.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
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
- `孤海注释` —— 8/10 个有
- `RH_RhartImageG2ImageToImage` —— 6/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `LayerUtility: LaMa` —— 3/10 个有
- `WujiUpscaler` —— 3/10 个有
- `EmptyImage` —— 2/10 个有
- `ImageToMask` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `RH_SeedreamV5ProImageToImage` —— 1/10 个有
- `WatermarkDetector` —— 1/10 个有
- `WatermarkDetectorLoader` —— 1/10 个有

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
