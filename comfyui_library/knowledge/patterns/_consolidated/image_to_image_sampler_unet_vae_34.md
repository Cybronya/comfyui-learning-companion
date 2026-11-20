---
name: image_to_image_sampler_unet_vae_34
type: Image To Image
frequency: 8
level: weak
coverage: 0.882
common_nodes: [CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2096490894571687937.json, 图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2097045177390166018.json, 图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2097051371597033473.json, 图片生成/图生图/动漫头像 漫画头像  真人转动漫  真人转卡通  真人转漫画_2095747766894022658.json, 图片生成/图生图/千问2511_任意物体360°视角随心切换_手动滑块操作更便捷_2010697372224987138.json, 图片生成/图生图/千问2512图生图洗图+SeedVR2高清工作流_2020867500254175234.json, 图片生成/图生图/千问2512洗图+SeedVR2高清放大工作流_2069347143063789569.json, 图片生成/图生图/千问Qwen Edit 2511任意切换视觉_2010756226547716098.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_34

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2096490894571687937.json、图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2097045177390166018.json、图片生成/图生图/动漫 真人转动漫  真人转卡通  真人转漫画_2097051371597033473.json、图片生成/图生图/动漫头像 漫画头像  真人转动漫  真人转卡通  真人转漫画_2095747766894022658.json、图片生成/图生图/千问2511_任意物体360°视角随心切换_手动滑块操作更便捷_2010697372224987138.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `CFGNorm` —— 6/8 个有
- `PIP_图像联结` —— 5/8 个有
- `SeedVR2LoadDiTModel` —— 4/8 个有
- `SeedVR2LoadVAEModel` —— 4/8 个有
- `SeedVR2VideoUpscaler` —— 4/8 个有
- `TextEncodeQwenImageEdit` —— 4/8 个有
- `CLIPTextEncode` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `QwenMultiangleCameraNode` —— 2/8 个有
- `ShowText|pysssss` —— 2/8 个有
- `TextEncodeQwenImageEditPlus` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `ImpactSwitch` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 8 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 28% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 8 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，8 个样本
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
