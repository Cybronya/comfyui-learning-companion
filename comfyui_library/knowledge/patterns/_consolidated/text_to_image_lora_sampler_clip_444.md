---
name: text_to_image_lora_sampler_clip_444
type: Text To Image
frequency: 4
level: strong
coverage: 0.84525
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/SeedVR2.5视频超分｜高清放大视频生视频画质增强_2089400018850639874.json, 图片生成/图生图/SeedVR2视频超分新升级｜2K分辨率放大一键出片v1_2107641334705250306.json, 图片生成/图生图/宫格图故事板分割｜高清放大图生图一键拆分处理_2092901712502812674.json, 视频生成/文生视频/SeedVR2.5视频高清放大流｜老片新看画质逆袭_2098771107917688833.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_444

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/SeedVR2.5视频超分｜高清放大视频生视频画质增强_2089400018850639874.json、图片生成/图生图/SeedVR2视频超分新升级｜2K分辨率放大一键出片v1_2107641334705250306.json、图片生成/图生图/宫格图故事板分割｜高清放大图生图一键拆分处理_2092901712502812674.json、视频生成/文生视频/SeedVR2.5视频高清放大流｜老片新看画质逆袭_2098771107917688833.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SeedVR2` —— 3/4 个有
- `SeedVR2BlockSwap` —— 3/4 个有
- `SeedVR2ExtraArgs` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `SeedVR2LoadDiTModel` —— 2/4 个有
- `SeedVR2LoadVAEModel` —— 2/4 个有
- `SeedVR2VideoUpscaler` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `VHS_VideoInfo` —— 2/4 个有
- `GuHaiAutoImageSplit` —— 1/4 个有
- `Int` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `VHS_VideoInfoSource` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
