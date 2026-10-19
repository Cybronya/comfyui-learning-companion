---
name: unknown_workflow_sampler_unet_vae_97
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.815286
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1 文生图  T8版 加速_2105327796250828801.json, 图片生成/文生图/Qwen image 2.1 文生图 日常出图够用啦！_2104947912215187458.json, 图片生成/文生图/Qwen-Image-2.1 文生图标准版_2104450148830109698.json, 图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（优化版）_2103650787716059138.json, 图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（图生图编辑版）_2103658795657424897.json, 图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE 文生图_2102956400250023938.json, 图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE 文生图_2104081684923772930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_97

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1 文生图  T8版 加速_2105327796250828801.json、图片生成/文生图/Qwen image 2.1 文生图 日常出图够用啦！_2104947912215187458.json、图片生成/文生图/Qwen-Image-2.1 文生图标准版_2104450148830109698.json、图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（优化版）_2103650787716059138.json、图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（图生图编辑版）_2103658795657424897.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 6/7 个有
- `QwenImage21BlockCacheT8` —— 5/7 个有
- `QwenImage21SageAttentionT8` —— 5/7 个有
- `QwenImage21SpectrumT8` —— 5/7 个有
- `CR Prompt Text` —— 4/7 个有
- `ComfySwitchNode` —— 4/7 个有
- `QwenPERewriteT8` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `SaveImageAdvanced` —— 2/7 个有
- `TextGenerateLTX2Prompt` —— 2/7 个有
- `KSamplerSelect` —— 1/7 个有
- `LTXVConcatAVLatent` —— 1/7 个有
- `LTXVSeparateAVLatent` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `ManualSigmas` —— 1/7 个有
- `SamplerCustomAdvanced` —— 1/7 个有
- `VAEEncode` —— 1/7 个有
- `VHS_VideoCombine` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 25 - 40 | 7 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 25 - 40，7 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
