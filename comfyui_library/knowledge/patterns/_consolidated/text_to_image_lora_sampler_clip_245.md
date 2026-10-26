---
name: text_to_image_lora_sampler_clip_245
type: Text To Image
frequency: 8
level: strong
coverage: 0.889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, EmptySD3LatentImage, JjkText, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2四视图角色资产库 角色卡人物卡片设计工具_2099202764437024770.json, 图片生成/图生图/Krea2四视图角色资产库 角色卡人物卡片设计工具_2099570188235657217.json, 图片生成/图生图/Krea2多风格单图编辑｜图生图风格转换_2089711798994948098.json, 图片生成/图生图/一键动态角色设计表｜Krea2全能图生图生成_2090550347252191234.json, 图片生成/图生图/动态角色设计表一键出｜Krea2全能图生图_2090850864838823937.json, 图片生成/图生图/四视图生成 角色设定图批量产出高效稳定出图_2109076636594434049.json, 图片生成/图生图/四视图生成模板｜MiniMaxH3图生图角色设计_2090230844425326594.json, 图片生成/图生图/四视图角色资产库｜Krea2图生图MiniMaxH3、Seedance视频参考专用_2092546636454125569.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_245

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Krea2四视图角色资产库 角色卡人物卡片设计工具_2099202764437024770.json、图片生成/图生图/Krea2四视图角色资产库 角色卡人物卡片设计工具_2099570188235657217.json、图片生成/图生图/Krea2多风格单图编辑｜图生图风格转换_2089711798994948098.json、图片生成/图生图/一键动态角色设计表｜Krea2全能图生图生成_2090550347252191234.json、图片生成/图生图/动态角色设计表一键出｜Krea2全能图生图_2090850864838823937.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `JjkText`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 5/8 个有
- `CheckpointLoaderSimple` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `WujiCleaner` —— 3/8 个有
- `WujiSampler` —— 3/8 个有
- `WujiUpscaler` —— 3/8 个有
- `PreviewAny` —— 2/8 个有
- `TextGenerate` —— 2/8 个有
- `ConditioningKrea2Rebalance` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `ResizeImageMaskNode` —— 1/8 个有
- `easy stylesSelector` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
