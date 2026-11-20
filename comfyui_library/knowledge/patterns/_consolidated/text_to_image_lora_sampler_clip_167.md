---
name: text_to_image_lora_sampler_clip_167
type: Text To Image
frequency: 10
level: strong
coverage: 0.8908
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2局部重绘编辑 图生图精修处理工具_2099912102348681217.json, 图片生成/图生图/Krea2角色四视图生成 图生图处理工具_2100647471348277249.json, 图片生成/图生图/Qwen Image 2.1万物移除工作流，局部重绘擦除图生图处理工具_2106122541428461569.json, 图片生成/图生图/Qwen image 2.1二合一工作流｜万物移除与局部重绘，擦除修复全能_2104547539398778881.json, 图片生成/图生图/Qwen-image2.1万物移除工作流｜图生图一键抹除多余物体无痕迹_2104023831454244865.json, 图片生成/图生图/krea2角色四视图生成｜图生图一套出正面侧面背面，角色设定图省事_2100467137897910274.json, 图片生成/图生图/krea2角色四视图生成｜角色设定图生图工作流_2095573849994784770.json, 图片生成/图生图/万物移除加局部重绘二合一 Qwen image 2.1图像编辑工作流_2104778416783446018.json, 图片生成/图生图/局部重绘｜Krea2-edit精准编辑，改哪画哪不伤原图_2099879932771000322.json, 图片生成/图生图/画面杂物一键清除 Qwen image2.1万物移除图生图编辑_2104261593684074497.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_167

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Krea2局部重绘编辑 图生图精修处理工具_2099912102348681217.json、图片生成/图生图/Krea2角色四视图生成 图生图处理工具_2100647471348277249.json、图片生成/图生图/Qwen Image 2.1万物移除工作流，局部重绘擦除图生图处理工具_2106122541428461569.json、图片生成/图生图/Qwen image 2.1二合一工作流｜万物移除与局部重绘，擦除修复全能_2104547539398778881.json、图片生成/图生图/Qwen-image2.1万物移除工作流｜图生图一键抹除多余物体无痕迹_2104023831454244865.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 7/10 个有
- `Mask Fill Holes` —— 7/10 个有
- `Int` —— 5/10 个有
- `Krea2EditGroundedEncode` —— 5/10 个有
- `Krea2EditModelPatch` —— 5/10 个有
- `TextEncodeQwenImage21` —— 5/10 个有
- `VAEEncode` —— 5/10 个有
- `easy int` —— 5/10 个有
- `CR Text` —— 3/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `ImpactSwitch` —— 2/10 个有
- `kkPadImageToCanvas` —— 2/10 个有
- `ImagePadForOutpaint` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（15/10 个样本）：Steps较低可能导致细节不足
