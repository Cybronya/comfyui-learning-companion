---
name: text_to_image_lora_sampler_clip_243
type: Text To Image
frequency: 8
level: strong
coverage: 0.854375
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, GetImagesFromBatchIndexed, GetVideoComponents, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/H3角色四视图设计 写实风格图生图角色造型参考_2098644114316292097.json, 图片生成/图生图/H3角色四视图设计批量版 图生图多角色造型同时生成_2098663693901979650.json, 图片生成/图生图/h3角色四视图批量设计｜图生图多角度一次成型_2098734489211068418.json, 图片生成/图生图/h3角色四视图设计流｜图生图三视图标准出图_2098760570882318337.json, 视频生成/图生视频/Minimax h3高一致性故事多分镜图处理 漫画分镜批量生成_2104667473604866050.json, 视频生成/图生视频/Minimax h3高一致性故事多分镜图处理 漫画分镜批量生成_2105069400066969601.json, 视频生成/图生视频/Minimax h3高一致性故事多分镜图处理 漫画分镜批量生成_2105401727510990850.json, 视频生成/图生视频/故事多分镜图处理工作流｜Minimax h3图生图分镜生成_2096719495321710593.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_243

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/H3角色四视图设计 写实风格图生图角色造型参考_2098644114316292097.json、图片生成/图生图/H3角色四视图设计批量版 图生图多角色造型同时生成_2098663693901979650.json、图片生成/图生图/h3角色四视图批量设计｜图生图多角度一次成型_2098734489211068418.json、图片生成/图生图/h3角色四视图设计流｜图生图三视图标准出图_2098760570882318337.json、视频生成/图生视频/Minimax h3高一致性故事多分镜图处理 漫画分镜批量生成_2104667473604866050.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `GetImagesFromBatchIndexed`
- `GetVideoComponents`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 6/8 个有
- `LoadImage` —— 6/8 个有
- `VAEDecodeAudio` —— 6/8 个有
- `VHS_VideoCombine` —— 6/8 个有
- `AILab_QwenVL` —— 4/8 个有
- `HAIGC_SaveImagesToZip` —— 4/8 个有
- `ImageGrid` —— 4/8 个有
- `ModelAttentionBackend` —— 4/8 个有
- `MultiTextConcatenate` —— 4/8 个有
- `PreviewAny` —— 4/8 个有
- `easy clearCacheAll` —— 4/8 个有
- `AutoCropFaces` —— 2/8 个有
- `ImageScaleBy` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `RHBatchImages:` —— 2/8 个有
- `RHExtractImage` —— 2/8 个有
- `RHUploadZip` —— 2/8 个有
- `ZML_PreviewImage` —— 2/8 个有
- `easy forLoopEnd` —— 2/8 个有
- `easy forLoopStart` —— 2/8 个有
- `easy imageCount` —— 2/8 个有
- `easy showAnything` —— 2/8 个有

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
| Steps较低可能导致细节不足 | 11/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（11/8 个样本）：Steps较低可能导致细节不足
