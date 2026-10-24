---
name: text_to_image_lora_sampler_clip_304
type: Text To Image
frequency: 6
level: strong
coverage: 0.8985
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21Cache, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1批量一键抠图透明背景生成 自动识别主体电商产品图_2105354969548419074.json, 图片生成/图生图/Qwen-2.1五视图透明背景版｜角色多角度展示底图随意换_2103686363605454849.json, 图片生成/图生图/Qwen-2.1图片编辑利器｜局部修改元素增删图生图全能王_2103684849763700737.json, 图片生成/图生图/Qwen-Image-2.1批量一键抠图，透明背景电商产品图_2111562469469679618.json, 图片生成/图生图/Qwen-Image-2.1批量抠图神器｜自动识别主体一键透明背景电商图_2105112588618125313.json, 图片生成/图生图/真2K白底图产品图生成 电商产品展示背景处理方案_2109740581042876418.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_304

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1批量一键抠图透明背景生成 自动识别主体电商产品图_2105354969548419074.json、图片生成/图生图/Qwen-2.1五视图透明背景版｜角色多角度展示底图随意换_2103686363605454849.json、图片生成/图生图/Qwen-2.1图片编辑利器｜局部修改元素增删图生图全能王_2103684849763700737.json、图片生成/图生图/Qwen-Image-2.1批量一键抠图，透明背景电商产品图_2111562469469679618.json、图片生成/图生图/Qwen-Image-2.1批量抠图神器｜自动识别主体一键透明背景电商图_2105112588618125313.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 5/6 个有
- `HAIGC_SaveImagesToZip` —— 4/6 个有
- `ImageScaleToTotalPixels` —— 4/6 个有
- `LoadImage` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `RHHiddenNodes` —— 3/6 个有
- `RHUploadZip_V2` —— 3/6 个有
- `ResolutionSelector` —— 3/6 个有
- `easy imageSize` —— 3/6 个有
- `CR Prompt List` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `MultiTextConcatenate` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
