---
name: text_to_image_lora_sampler_clip_247
type: Text To Image
frequency: 8
level: strong
coverage: 0.89175
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2局部重绘编辑 图生图精修处理工具_2099912102348681217.json, 图片生成/图生图/Krea2角色四视图生成 图生图处理工具_2100647471348277249.json, 图片生成/图生图/Krea2角色四视图生成2.0 图生图处理工具_2100269060750663682.json, 图片生成/图生图/Qwen Image 2.1万物移除工作流，局部重绘擦除图生图处理工具_2106122541428461569.json, 图片生成/图生图/krea2角色四视图生成｜图生图一套出正面侧面背面，角色设定图省事_2100467137897910274.json, 图片生成/图生图/krea2角色四视图生成｜角色设定图生图工作流_2095573849994784770.json, 图片生成/图生图/局部重绘｜Krea2-edit精准编辑，改哪画哪不伤原图_2099879932771000322.json, 图片生成/图生图/角色四视图一键生成｜krea2图生图设计_2095816777677758466.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_247

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Krea2局部重绘编辑 图生图精修处理工具_2099912102348681217.json、图片生成/图生图/Krea2角色四视图生成 图生图处理工具_2100647471348277249.json、图片生成/图生图/Krea2角色四视图生成2.0 图生图处理工具_2100269060750663682.json、图片生成/图生图/Qwen Image 2.1万物移除工作流，局部重绘擦除图生图处理工具_2106122541428461569.json、图片生成/图生图/krea2角色四视图生成｜图生图一套出正面侧面背面，角色设定图省事_2100467137897910274.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `CR Prompt Text` —— 7/8 个有
- `Krea2EditGroundedEncode` —— 7/8 个有
- `VAEEncode` —— 7/8 个有
- `Krea2EditModelPatch` —— 6/8 个有
- `easy int` —— 6/8 个有
- `DrawMaskOnImage` —— 3/8 个有
- `Mask Fill Holes` —— 3/8 个有
- `kkPadImageToCanvas` —— 3/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `ImagePadForOutpaint` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/8 个有
- `Int` —— 1/8 个有
- `Krea2OstrisEditModelPatch` —— 1/8 个有
- `TextEncodeQwenImage21` —— 1/8 个有

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
| Steps较低可能导致细节不足 | 15/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（15/8 个样本）：Steps较低可能导致细节不足
