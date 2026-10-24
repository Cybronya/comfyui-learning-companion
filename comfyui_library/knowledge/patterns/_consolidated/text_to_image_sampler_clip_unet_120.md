---
name: text_to_image_sampler_clip_unet_120
type: Text To Image
frequency: 6
level: weak
coverage: 0.9005
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, EmptyLatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, RH_Captioner, SaveImage, TT_img_enc, Text Input Switch, UNETLoader, VAEDecode, VAELoader, easy boolean, easy imageSwitch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image文生图与反推提示词 支持加密切换保护作品_2098102225439641602.json, 图片生成/文生图/Z-image文生图加图片反推｜T2I高速生成绅士加密切换_2088720217793974273.json, 图片生成/文生图/Z-image文生图反推去水印加密一体化 多功能图片生成_2099903911074295809.json, 图片生成/文生图/Z-image极速文生图T2I｜图片反推绅士加密切换玩法_2089060757785890818.json, 图片生成/文生图/【Z-image】文生图(T2I)+反推&去水印&加密_2029543092298194945.json, 图片生成/文生图/文生图｜Z-image支持T2I出图，反推提示词还能去水印加密_2099859670524583937.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_120

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-image文生图与反推提示词 支持加密切换保护作品_2098102225439641602.json、图片生成/文生图/Z-image文生图加图片反推｜T2I高速生成绅士加密切换_2088720217793974273.json、图片生成/文生图/Z-image文生图反推去水印加密一体化 多功能图片生成_2099903911074295809.json、图片生成/文生图/Z-image极速文生图T2I｜图片反推绅士加密切换玩法_2089060757785890818.json、图片生成/文生图/【Z-image】文生图(T2I)+反推&去水印&加密_2029543092298194945.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `RH_Captioner`
- `SaveImage`
- `TT_img_enc`
- `Text Input Switch`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy boolean`
- `easy imageSwitch`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `solarL_SaveImagesToZip` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `AILab_ImageStitch` —— 4/6 个有
- `DF_Text_Box` —— 4/6 个有
- `LatentToWidthHeight` —— 4/6 个有
- `ResizeImageNode` —— 4/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 6 | 68% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 6 | 67% |
| 采样算法 | er_sde | - | 6 | 83% |
| 调度器 | beta | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 1200 | 6 | 0% |
| 高度 | 80 | 80 - 1600 | 6 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，6 个样本
- 采样算法 最常用 er_sde，6 个样本，一致性 83%
- 调度器 最常用 beta，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1200，6 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1600，6 个样本，取值分散，一致性仅 0%
- 高发问题（11/6 个样本）：Steps较低可能导致细节不足
