---
name: image_to_image_upscale_lora_sampler_19
type: Image To Image
frequency: 8
level: strong
coverage: 0.909375
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/z-Image 智能高清修复与放大工作流_2036626914529513473.json, 图片生成/图生图/动漫头像 漫画头像  真人转动漫  真人转卡通  真人转漫画_2095747766894022658.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2059925156805562369.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2089746856464183297.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096643115598831618.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096654007803666433.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096831045206364161.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2100329081756803073.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_19

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/z-Image 智能高清修复与放大工作流_2036626914529513473.json、图片生成/图生图/动漫头像 漫画头像  真人转动漫  真人转卡通  真人转漫画_2095747766894022658.json、图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2059925156805562369.json、图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2089746856464183297.json、图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096643115598831618.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
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
- `CFGNorm` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `TextEncodeQwenImageEdit` —— 7/8 个有
- `PIP_图像联结` —— 6/8 个有
- `CLIPTextEncode` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `Qwen3_VQA` —— 1/8 个有
- `RepeatLatentBatch` —— 1/8 个有
- `ShowAnything|Mie` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 8 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 0.88 - 1 | 8 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，8 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.88 - 1，8 个样本，取值集中（一致性 96%）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
