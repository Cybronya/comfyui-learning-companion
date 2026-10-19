---
name: unknown_workflow_video_sampler_clip_45
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.972909
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1950019885810278402.json, 视频生成/图生视频/1949871936315768833.json, 视频生成/图生视频/1950015972724883458.json, 视频生成/图生视频/1949853817082961922.json, 视频生成/图生视频/1956284069929734146.json, 视频生成/图生视频/1993849830151749634.json, 视频生成/图生视频/2000856000670429186.json, 视频生成/图生视频/1956256627454300162.json, 视频生成/图生视频/1950049214580572162.json, 视频生成/图生视频/1952322555396984834.json, 视频生成/图生视频/1952825876464529410.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1950019885810278402.json、视频生成/图生视频/1949871936315768833.json、视频生成/图生视频/1950015972724883458.json、视频生成/图生视频/1949853817082961922.json、视频生成/图生视频/1956284069929734146.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 9/11 个有
- `LayerUtility: PurgeVRAM` —— 9/11 个有
- `PathchSageAttentionKJ` —— 9/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `TeaCache` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `ImageUpscaleWithModel` —— 2/11 个有
- `InversionDemoLazyIndexSwitch` —— 2/11 个有
- `LoadAudio` —— 2/11 个有
- `RIFE VFI` —— 2/11 个有
- `Random Number` —— 2/11 个有
- `UpscaleModelLoader` —— 2/11 个有
- `CR Seed` —— 1/11 个有
- `PreviewImage` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 64% |
| Prompt 约束强度(CFG) | 8 | 6 - 20 | 11 | 47% |
| 采样算法 | 1 | 1 - 3.5 | 11 | 37% |
| 调度器 | lcm | - | 11 | 64% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 64%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 20，11 个样本，取值分散，一致性仅 47%
- 采样算法 中位数 1，观测区间 1 - 3.5，11 个样本，取值分散，一致性仅 37%
- 调度器 最常用 lcm，11 个样本，一致性 64%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
