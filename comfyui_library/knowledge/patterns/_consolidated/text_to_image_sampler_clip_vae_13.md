---
name: text_to_image_sampler_clip_vae_13
type: Text To Image
frequency: 11
level: weak
coverage: 0.901273
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/分镜图生成_2093149514755559425.json, 视频生成/文生视频/Boogu-Image Base 文生图工作流_2067856528262127617.json, 视频生成/文生视频/Qwen2512领军模型｜完美中文文生图图生图生成_2090530166060707841.json, 视频生成/文生视频/Qwen2512领军模型｜完美中文文生图图生图生成_2094308048687951873.json, 视频生成/文生视频/RH Upscale视频极速高清放大工作流PR插件适配，视频超分高清增强工具_2107260285441634305.json, 视频生成/文生视频/RH Upscale视频极速高清放大工作流，PR插件适配视频超分工具_2106535133057740802.json, 视频生成/文生视频/Seedance 2.5图生视频处理生成工具_2102525837089263617.json, 视频生成/文生视频/Seedance 2.5文生视频处理生成工具_2102527398846754817.json, 视频生成/文生视频/Seedance2.0 Fast全能参考视频 图片音频视频三参考输入_2104694435845070849.json, 视频生成/文生视频/全能参考生真人视频｜Seedance2.0 文生视频图生视频一站搞定_2105499577867653122.json, 视频生成/文生视频/全能参考生真人视频｜Seedance2.0文生视频生视频_2095870248128958465.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_13

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/分镜图生成_2093149514755559425.json、视频生成/文生视频/Boogu-Image Base 文生图工作流_2067856528262127617.json、视频生成/文生视频/Qwen2512领军模型｜完美中文文生图图生图生成_2090530166060707841.json、视频生成/文生视频/Qwen2512领军模型｜完美中文文生图图生图生成_2094308048687951873.json、视频生成/文生视频/RH Upscale视频极速高清放大工作流PR插件适配，视频超分高清增强工具_2107260285441634305.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `JjkText` —— 9/11 个有
- `solarL_SaveImagesToZip` —— 9/11 个有
- `孤海注释` —— 9/11 个有
- `SaveVideo` —— 7/11 个有
- `SaveImage` —— 6/11 个有
- `LoadVideo` —— 5/11 个有
- `LoadImage` —— 4/11 个有
- `RH_RhartVideoSparkvideo20FastMultimodalVideo` —— 3/11 个有
- `RH_Upscale` —— 2/11 个有
- `EnhancedLoadDiffusionModel` —— 1/11 个有
- `LoadAudio` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `RH_BytedanceSeedance25TokenImageToVideo` —— 1/11 个有
- `RH_BytedanceSeedance25TokenTextToVideo` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 11 | 0% |
| 高度 | 80 | 80 - 1536 | 11 | 0% |
| 采样步数 | 4 | 4 - 35 | 11 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 3.5 - 4.5 | 11 | 93% |
| 采样算法 | er_sde | - | 11 | 82% |
| 调度器 | beta | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，11 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 35，11 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 3.5 - 4.5，11 个样本，取值集中（一致性 93%）
- 采样算法 最常用 er_sde，11 个样本，一致性 82%
- 调度器 最常用 beta，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（10/11 个样本）：Steps较低可能导致细节不足
