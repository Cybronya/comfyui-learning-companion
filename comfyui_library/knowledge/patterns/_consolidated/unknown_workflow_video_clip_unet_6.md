---
name: unknown_workflow_video_clip_unet_6
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.9733
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/wan2.2-i2v-rapid-aio-最快图生视频_1950686610079830017.json, 视频生成/图生视频/wan2.2-i2v图生视频_1951804301834440706.json, 视频生成/图生视频/wan2.2-ti2v-5B图生视频-与小时候的自己一起散步_1987307533339701250.json, 视频生成/图生视频/wan2.2-ti2v-5B图生视频_1951277844100009986.json, 视频生成/图生视频/wan2.2-ti2v-5B文生视频摆尾猫_1952539360614920193.json, 视频生成/图生视频/图生视频工作流_1991844034222288897.json, 视频生成/图生视频/视频用这个_2023300078865223682.json, 视频生成/文生视频/Wan2.2_14B_图生视频 (稳定加速版) 丨提示词生成视频_1968987843408379906.json, 视频生成/文生视频/wan2.2视频工作流_2013120474653401089.json, 视频生成/文生视频/【优化版】最强图生视频万相wan2.2_1952999225413070849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/wan2.2-i2v-rapid-aio-最快图生视频_1950686610079830017.json、视频生成/图生视频/wan2.2-i2v图生视频_1951804301834440706.json、视频生成/图生视频/wan2.2-ti2v-5B图生视频-与小时候的自己一起散步_1987307533339701250.json、视频生成/图生视频/wan2.2-ti2v-5B图生视频_1951277844100009986.json、视频生成/图生视频/wan2.2-ti2v-5B文生视频摆尾猫_1952539360614920193.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `WanImageToVideo` —— 7/10 个有
- `KSampler` —— 6/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `KSamplerAdvanced` —— 4/10 个有
- `Wan22ImageToVideoLatent` —— 3/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `RIFE VFI` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17 | 4 - 30 | 6 | 24% |
| Prompt 约束强度(CFG) | 5 | 1 - 14 | 10 | 23% |
| 采样算法 | sa_solver | - | 10 | 30% |
| 调度器 | euler | - | 10 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17，观测区间 4 - 30，6 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 14，10 个样本，取值分散，一致性仅 23%
- 采样算法 最常用 sa_solver，10 个样本，一致性 30%
- 调度器 最常用 euler，10 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
