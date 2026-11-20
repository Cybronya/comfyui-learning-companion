---
name: unknown_workflow_sampler_clip_unet_261
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8822
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LayerUtility: PurgeVRAM V2, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, SeedVR2, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/SROP-细节修复-洗图工作流_1971806203087155202.json, 图片生成/图生图/SRPO FLUX超真实感洗图_1969353764324995074.json, 图片生成/图生图/SRPO-image-fix-workflow_1967519002291474434.json, 图片生成/图生图/SRPO-image-fix-图像精修-高清放大-电影级皮肤质感-图生图_1973764334977462274.json, 图片生成/文生图/写实人像、电影质感画质-文生图-2K直出_1989660235738607618.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_261

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/SROP-细节修复-洗图工作流_1971806203087155202.json、图片生成/图生图/SRPO FLUX超真实感洗图_1969353764324995074.json、图片生成/图生图/SRPO-image-fix-workflow_1967519002291474434.json、图片生成/图生图/SRPO-image-fix-图像精修-高清放大-电影级皮肤质感-图生图_1973764334977462274.json、图片生成/文生图/写实人像、电影质感画质-文生图-2K直出_1989660235738607618.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `EmptySD3LatentImage` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `Float` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `ImpactInt` —— 2/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `CustomAddLabel` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `KSampler` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `SeedVR2BlockSwap` —— 1/5 个有
- `SeedVR2ExtraArgs` —— 1/5 个有
- `TeaCache` —— 1/5 个有
- `Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
