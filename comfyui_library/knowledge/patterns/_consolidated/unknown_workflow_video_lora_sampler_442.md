---
name: unknown_workflow_video_lora_sampler_442
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.900571
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/AI脑洞狮--图生视频_2035035563962671105.json, 视频生成/图生视频/Smooth Mix i2V v2.0图生视频8步加速版_2026835055515017218.json, 视频生成/图生视频/Smooth Mix i2V v2.0图生视频8步加速版_2056759291427778562.json, 视频生成/图生视频/Wan2.2_图生视频_4步极速版_ComfyUI官方流_2017158021029306369.json, 视频生成/图生视频/Wan2.2_图生视频_4步极速版_ComfyUI官方流_2044039756232790017.json, 视频生成/图生视频/Wan2_2_I2V_org_api_1971438384981983234.json, 视频生成/图生视频/图生视频工作流_2066459393683705858.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_442

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/AI脑洞狮--图生视频_2035035563962671105.json、视频生成/图生视频/Smooth Mix i2V v2.0图生视频8步加速版_2026835055515017218.json、视频生成/图生视频/Smooth Mix i2V v2.0图生视频8步加速版_2056759291427778562.json、视频生成/图生视频/Wan2.2_图生视频_4步极速版_ComfyUI官方流_2017158021029306369.json、视频生成/图生视频/Wan2.2_图生视频_4步极速版_ComfyUI官方流_2044039756232790017.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `ImpactImageInfo` —— 1/7 个有
- `Int` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `VAEDecodeTiled` —— 1/7 个有
- `easy clearCacheAll` —— 1/7 个有
- `wanBlockSwap` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 71% |
| Prompt 约束强度(CFG) | 6 | 4 - 12 | 7 | 65% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 71%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 12，7 个样本
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
