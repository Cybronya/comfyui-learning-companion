---
name: text_to_image_video_lora_sampler_85
type: Text To Image
frequency: 9
level: weak
coverage: 0.831222
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Work-Fisher出品AI短剧制作全流程｜热门IP一键改编_2111070378704596993.json, 图片生成/图生图/【拓拓】AI短剧制作全流程_2114263270419951617.json, 图片生成/文生图/AI短剧制作全流程工作流｜文生图到图生视频一条龙｜短剧创作省心方案_2112118425899323393.json, 图片生成/文生图/AI短剧制作全流程视频_2111655145577734145.json, 视频生成/图生视频/minimaxH3 多参考视频PV工作流｜备用方案图生视频更稳妥_2097504953928605697.json, 视频生成/图生视频/【Gensor】AI短剧制作工具合集工作流_2111079570249183234.json, 视频生成/图生视频/【Work-Fisher】AI短剧制作全流程_2109735475824123905.json, 视频生成/图生视频/【创客训练营】AI短剧制作全流程_2110597688004792322.json, 视频生成/图生视频/多参生成视频工作流｜多图参考生视频通用稳定版_2113978436757843969.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_85

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Work-Fisher出品AI短剧制作全流程｜热门IP一键改编_2111070378704596993.json、图片生成/图生图/【拓拓】AI短剧制作全流程_2114263270419951617.json、图片生成/文生图/AI短剧制作全流程工作流｜文生图到图生视频一条龙｜短剧创作省心方案_2112118425899323393.json、图片生成/文生图/AI短剧制作全流程视频_2111655145577734145.json、视频生成/图生视频/minimaxH3 多参考视频PV工作流｜备用方案图生视频更稳妥_2097504953928605697.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 8/9 个有
- `INTConstant` —— 8/9 个有
- `LoraLoaderBypassModelOnly` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `SolAttnMiniMax` —— 8/9 个有
- `CR Prompt Text` —— 7/9 个有
- `CR Text` —— 7/9 个有
- `ComfySwitchNode` —— 7/9 个有
- `Image Comparer (rgthree)` —— 7/9 个有
- `ImageScaleToTotalPixels` —— 7/9 个有
- `SaveImage` —— 7/9 个有
- `SeedVR2LoadDiTModel` —— 7/9 个有
- `SeedVR2LoadVAEModel` —— 7/9 个有
- `SeedVR2VideoUpscaler` —— 7/9 个有
- `TextEncodeQwenImage21` —— 7/9 个有
- `忽略多组孤海` —— 5/9 个有
- `JjkText` —— 4/9 个有
- `solarL_SaveImagesToZip` —— 4/9 个有
- `孤海注释` —— 4/9 个有
- `LoadAudio` —— 3/9 个有
- `ModelPreviewOverrideKJ` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有
- `VHS_SelectImages` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1080 | 9 | 22% |
| 高度 | 1024 | 80 - 1920 | 9 | 13% |
| 采样步数 | 8 | 4 - 25 | 9 | 23% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 9 | 32% |
| 采样算法 | er_sde | - | 9 | 44% |
| 调度器 | beta | - | 9 | 44% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1080，9 个样本，取值分散，一致性仅 22%
- 高度 中位数 1024，观测区间 80 - 1920，9 个样本，取值分散，一致性仅 13%
- 采样步数 中位数 8，观测区间 4 - 25，9 个样本，取值分散，一致性仅 23%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，9 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 er_sde，9 个样本，一致性 44%
- 调度器 最常用 beta，9 个样本，一致性 44%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（18/9 个样本）：Steps较低可能导致细节不足
