---
name: image_to_image_upscale_lora_sampler_18
type: Image To Image
frequency: 8
level: strong
coverage: 0.904
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/白底转场景-叠高清放大-cr大雄_1998636955619483650.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2059925156805562369.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2089746856464183297.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096643115598831618.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096654007803666433.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096831045206364161.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2100329081756803073.json, 视频生成/图生视频/Qwen-Edit-2509-光线迁移 (1)_2058721719896076290.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/白底转场景-叠高清放大-cr大雄_1998636955619483650.json、图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2059925156805562369.json、图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2089746856464183297.json、图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096643115598831618.json、图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096654007803666433.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/8 个有
- `TextEncodeQwenImageEdit` —— 6/8 个有
- `PIP_图像联结` —— 5/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `ImageScaleBy` —— 2/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `TextEncodeQwenImageEditPlus` —— 2/8 个有
- `ImageBlend` —— 1/8 个有
- `Mask Fill Holes` —— 1/8 个有
- `MaskToImage` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
