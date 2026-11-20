---
name: text_to_image_lora_sampler_clip_135
type: Text To Image
frequency: 12
level: strong
coverage: 0.901583
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片后期四合一套餐｜加文字加水印手动溶图指定放置_2101519901524578306.json, 图片生成/图生图/图生图AIGC Image 2.5九图工作流，高质量图像到图像处理方案_2107238746419716097.json, 图片生成/图生图/图生图手办创建工作流，人像照片秒变潮玩模型摆件_2112347977149927425.json, 图片生成/图生图/多场景图生成工作流， 一次产出多种场景效果_2102863110943105026.json, 图片生成/图生图/多场景图生成工作流，_一次产出多种场景效果_2105512418687414273.json, 图片生成/图生图/服装模特姿势复刻全能PRO官方稳定版工作流，服装展示图生图工具_2107203791136321538.json, 图片生成/图生图/服装模特姿势复刻全能PRO版｜官方稳定图生图服装展示_2106933544365940738.json, 图片生成/图生图/服装模特姿势复刻全能PRO版｜官方稳定图生图服装展示_2107649602324357121.json, 图片生成/图生图/特点图提取生成工作流， 快速提取画面关键特征_2102858541479583746.json, 图片生成/图生图/特点图提取生成工作流，_快速提取画面关键特征_2105516637746196481.json, 图片生成/图生图/适用步骤图生成工作流， 拆解操作流程可视化呈现_2102860066134257665.json, 图片生成/图生图/适用步骤图生成工作流，_拆解操作流程可视化呈现_2105515184944140289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_135

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/图片后期四合一套餐｜加文字加水印手动溶图指定放置_2101519901524578306.json、图片生成/图生图/图生图AIGC Image 2.5九图工作流，高质量图像到图像处理方案_2107238746419716097.json、图片生成/图生图/图生图手办创建工作流，人像照片秒变潮玩模型摆件_2112347977149927425.json、图片生成/图生图/多场景图生成工作流， 一次产出多种场景效果_2102863110943105026.json、图片生成/图生图/多场景图生成工作流，_一次产出多种场景效果_2105512418687414273.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
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
- `RH_RhartImageG25SunburstImageToImage` —— 8/12 个有
- `孤海注释` —— 8/12 个有
- `JWStringConcat` —— 6/12 个有
- `PreviewImage` —— 6/12 个有
- `Text` —— 6/12 个有
- `CR Text` —— 4/12 个有
- `OpenposePreprocessor` —— 3/12 个有
- `RH_RhartImageNProOfficialEdit` —— 3/12 个有
- `EmptyImage` —— 2/12 个有
- `BiRefNetRMBG` —— 1/12 个有
- `CR Prompt Text` —— 1/12 个有
- `FastCanvas` —— 1/12 个有
- `FastCanvasTool` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
