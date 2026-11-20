---
name: unknown_workflow_lora_sampler_clip_50
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.848667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/nunchaku-FLUX.1-Krea_1951667086886121474.json, 图片生成/文生图/nunchaku-flux.1(Lora加速与滤镜)-dev_1947113386972327938.json, 图片生成/文生图/文生图 — Flux 女孩二次元快速出图工作流 v 1.5_1915672810759589889.json, 图片生成/文生图/文生图 — Flux 女孩二次元快速出图工作流_1910229372215750657.json, 图片生成/文生图/文生图 — Flux 美女摄影快速出图工作流 v1.5_1910272215428886529.json, 图片生成/文生图/文生图 — Flux 美女摄影快速出图工作流_1909854047942209538.json, 图片生成/文生图/文生图基础款V1_1910318940827123714.json, 图片生成/文生图/文生图基础款_1910140152096747522.json, 图片生成/文生图/最新Flux5秒文生图  Nunchaku_1914304383847231490.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/nunchaku-FLUX.1-Krea_1951667086886121474.json、图片生成/文生图/nunchaku-flux.1(Lora加速与滤镜)-dev_1947113386972327938.json、图片生成/文生图/文生图 — Flux 女孩二次元快速出图工作流 v 1.5_1915672810759589889.json、图片生成/文生图/文生图 — Flux 女孩二次元快速出图工作流_1910229372215750657.json、图片生成/文生图/文生图 — Flux 美女摄影快速出图工作流 v1.5_1910272215428886529.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `ClownOptions_DetailBoost_Beta` —— 1/9 个有
- `ClownOptions_SwapSampler_Beta` —— 1/9 个有
- `ClownsharKSampler_Beta` —— 1/9 个有
- `LatentUpscaleBy` —— 1/9 个有
- `SharkOptions_Beta` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | bong_tangent | - | 1 | 100% |
| Prompt 约束强度(CFG) | 10 | - | 1 | 100% |
| 采样算法 | -1 | - | 1 | 100% |
| 调度器 | -0.67 | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：重绘幅度 观测到 1，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
