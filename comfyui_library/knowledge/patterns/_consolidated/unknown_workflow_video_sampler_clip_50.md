---
name: unknown_workflow_video_sampler_clip_50
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.972909
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 14B+Teacache+Sage 2.5图生视频加速版+视频放大_1950019885810278402.json, 视频生成/图生视频/Wan2.2 14B+Teacache+Sage 2.5速加速图生视频V1（无污染）_1949871936315768833.json, 视频生成/图生视频/Wan2.2 14B图生视频+视频放大_1950015972724883458.json, 视频生成/图生视频/Wan2.2 14B图生视频工作流_1949853817082961922.json, 视频生成/图生视频/Wan2.28步超极速高质量图生视频_1956284069929734146.json, 视频生成/图生视频/Wan2.2极速图生视频_1993849830151749634.json, 视频生成/图生视频/Wan2.2极速版_2000856000670429186.json, 视频生成/图生视频/[极速生成] Wan2.2 1分钟 81帧6步 图生视频 影视级真实效果_1956256627454300162.json, 视频生成/图生视频/wan2.2图生视频官方工作流加速版_1950049214580572162.json, 视频生成/图生视频/wan2.2图生视频美女跳舞6步极速版预置多段背景音乐随机_1952322555396984834.json, 视频生成/图生视频/灵动传媒短视频生成_1952825876464529410.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 14B+Teacache+Sage 2.5图生视频加速版+视频放大_1950019885810278402.json、视频生成/图生视频/Wan2.2 14B+Teacache+Sage 2.5速加速图生视频V1（无污染）_1949871936315768833.json、视频生成/图生视频/Wan2.2 14B图生视频+视频放大_1950015972724883458.json、视频生成/图生视频/Wan2.2 14B图生视频工作流_1949853817082961922.json、视频生成/图生视频/Wan2.28步超极速高质量图生视频_1956284069929734146.json…）

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
