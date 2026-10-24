---
name: text_to_image_lora_sampler_clip_398
type: Text To Image
frequency: 4
level: strong
coverage: 0.90775
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein图像编辑API｜图生图精准局部修改_2098712100834205698.json, 图片生成/图生图/Z IMAGE增加皮肤细节 图生图单张处理工具_2099594269966290945.json, 图片生成/图生图/qwen_image_edit_2511三视图｜角色一致性设计图生成_2093135891593256962.json, 图片生成/图生图/图生图图片编辑多图编辑 多张输入精准改图_2109786356653322241.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_398

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein图像编辑API｜图生图精准局部修改_2098712100834205698.json、图片生成/图生图/Z IMAGE增加皮肤细节 图生图单张处理工具_2099594269966290945.json、图片生成/图生图/qwen_image_edit_2511三视图｜角色一致性设计图生成_2093135891593256962.json、图片生成/图生图/图生图图片编辑多图编辑 多张输入精准改图_2109786356653322241.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `CFGNorm` —— 2/4 个有
- `ReferenceLatent` —— 2/4 个有
- `TextEncodeQwenImageEditPlus` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `CR Value` —— 1/4 个有
- `EmptyFlux2LatentImage` —— 1/4 个有
- `FluxKontextImageScale` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `图像缩放V2_孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（10/4 个样本）：Steps较低可能导致细节不足
